"""飞书图片上传工具

将图片上传至飞书开放平台，返回 image_key。
支持格式：JPG、JPEG、PNG、WEBP、GIF、BMP、ICO、TIFF、HEIC（TIFF/HEIC 上传后转为 JPG）。

用法:
    uv run upload_image.py <image_path> [--token TOKEN] [--image-type {message,avatar}]

示例:
    uv run upload_image.py ./screenshot.png
    uv run upload_image.py ./avatar.jpg --image-type avatar
    uv run upload_image.py ./photo.png --token t-xxxxx
"""

import argparse
import json
import os
import sys

import requests
from requests_toolbelt import MultipartEncoder


def upload_image(
    image_path: str,
    token: str | None = None,
    image_type: str = "message",
) -> dict:
    """上传图片到飞书，返回响应 JSON。

    Args:
        image_path: 图片文件路径。
        token: tenant_access_token，为 None 时从环境变量 FEISHU_TENANT_ACCESS_TOKEN 获取。
        image_type: 图片类型，"message"（发送消息）或 "avatar"（设置头像）。

    Returns:
        飞书 API 响应的 JSON dict，成功时包含 data.image_key。

    Raises:
        ValueError: 未提供 token 且环境变量中也不存在。
        FileNotFoundError: 图片文件不存在。
    """
    # 1. 获取 token：优先使用传参，其次环境变量
    if not token:
        token = os.environ.get("FEISHU_TENANT_ACCESS_TOKEN")
    if not token:
        raise ValueError(
            "未提供 tenant_access_token。请通过 --token 参数传入，"
            "或设置环境变量 FEISHU_TENANT_ACCESS_TOKEN。"
        )

    # 2. 校验文件
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"图片文件不存在: {image_path}")

    # 3. 构建请求
    url = "https://open.feishu.cn/open-apis/im/v1/images"
    with open(image_path, "rb") as f:
        form = MultipartEncoder(
            fields={
                "image_type": image_type,
                "image": (os.path.basename(image_path), f, "application/octet-stream"),
            }
        )
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": form.content_type,
        }
        response = requests.post(url, headers=headers, data=form, timeout=30)

    result = response.json()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="上传图片到飞书开放平台")
    parser.add_argument("image_path", help="要上传的图片文件路径")
    parser.add_argument(
        "--token",
        default=None,
        help="tenant_access_token（不传则从环境变量 FEISHU_TENANT_ACCESS_TOKEN 获取）",
    )
    parser.add_argument(
        "--image-type",
        choices=["message", "avatar"],
        default="message",
        help="图片类型：message（发送消息，默认）或 avatar（设置头像）",
    )
    args = parser.parse_args()

    try:
        result = upload_image(args.image_path, token=args.token, image_type=args.image_type)
    except (ValueError, FileNotFoundError) as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, ensure_ascii=False, indent=2))

    if result.get("code") == 0:
        image_key = result.get("data", {}).get("image_key", "")
        print(f"\n上传成功! image_key: {image_key}")
    else:
        print(f"\n上传失败: {result.get('msg', '未知错误')}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
