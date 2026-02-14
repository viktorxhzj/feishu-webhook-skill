# 上传图片

调用本接口将图片上传至飞书开放平台，支持上传 JPG、JPEG、PNG、WEBP、GIF、BMP、ICO、TIFF、HEIC 格式的图片，但需要注意 TIFF、HEIC 上传后会被转为 JPG 格式。

## 使用限制

- 上传的图片大小不能超过 10 MB，且不支持上传大小为 0 的图片。
- 上传图片的分辨率限制：
	- GIF 图片分辨率不能超过 2000 x 2000，其他图片分辨率不能超过 12000 x 12000。
	- 用于设置头像的图片分辨率不能超过 4096 x 4096。

如需上传高分辨率图片，可使用[上传文件](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/file/create)接口，将图片作为文件进行上传。注意该方式不支持将图片文件设置为头像。

## 认证

**必须**先尝试从环境变量 `FEISHU_TENANT_ACCESS_TOKEN` 中获取 `tenant_access_token`。如果环境变量中不存在，则需要显式向用户询问获取。

## 请求

基本 | &nbsp;
---|---
HTTP URL | https://open.feishu.cn/open-apis/im/v1/images
HTTP Method | POST

### 请求头

名称 | 类型 | 必填 | 描述
---|---|---|---
Authorization | string | 是 | `tenant_access_token`<br>**值格式**："Bearer `access_token`"<br>**示例值**："Bearer t-7f1bcd13fc57d46bac21793a18e560"
Content-Type | string | 是 | **示例值**："multipart/form-data; boundary=---7MA4YWxkTrZu0gW"

### 请求体

名称 | 类型 | 必填 | 描述
---|---|---|---
image_type | string | 是 | 图片类型<br>**示例值**："message"<br>**可选值有**：<br>- message：用于发送消息<br>- avatar：用于设置头像
image | file | 是 | 图片内容。传值方式可以参考请求体示例。<br>**注意**：<br>- 上传的图片大小不能超过 10 MB，也不能上传大小为 0 的图片。<br>- 分辨率限制：<br>- GIF 图片分辨率不能超过 2000 x 2000，其他图片分辨率不能超过 12000 x 12000。<br>- 用于设置头像的图片分辨率不能超过 4096 x 4096。<br>**示例值**：二进制文件

### 调用方式

直接使用`scripts/upload_image.py` 脚本上传图片：

```bash
# 基本用法（token 从环境变量 FEISHU_TENANT_ACCESS_TOKEN 获取）
uv run upload_image.py <image_path>

# 指定 token
uv run upload_image.py <image_path> --token <tenant_access_token>
```

## 响应

### 响应体

名称 | 类型 | 描述
---|---|---
code | int | 错误码，非 0 表示失败
msg | string | 错误描述
data | \- | \-
image_key | string | 图片的 Key

### 响应体示例
```json
{
    "code": 0,
    "data": {
        "image_key": "img_v2_xxx"
    },
    "msg": "success"
}
```

### 错误码

HTTP状态码 | 错误码 | 描述 | 排查建议
---|---|---|---
400 | 232096 | Meta writing has stopped, please try again later. | 应用信息被停写，请稍后再试。
400 | 234001 | Invalid request param. | 请求参数无效，请根据接口文档描述检查请求参数是否正确。
401 | 234002 | Unauthorized. | 接口鉴权失败，请咨询[技术支持](https://applink.feishu.cn/TLJpeNdW)。
400 | 234006 | The file size exceed the max value. | 资源大小超出限制。<br>- 文件限制：不超过 30 MB<br>- 图片限制：不超过 10 MB
400 | 234007 | App does not enable bot feature. | 应用没有启用机器人能力。启用方式参见[如何启用机器人能力](https://open.feishu.cn/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-enable-bot-ability)。
400 | 234010 | File's size can't be 0. | 请勿上传大小为 0 的文件。
400 | 234011 | Can't regonnize the image format. | 不支持的图片格式。目前仅支持上传 JPG、JPEG、PNG、WEBP、GIF、BMP、ICO、TIFF、HEIC 格式的图片。
400 | 234039 | Image resolution exceeds limit. | 分辨率超出限制。<br>- GIF 图片分辨率不能大于 2000 x 2000<br>- 其他图片分辨率不能大于 12000 x 12000<br>- 用于设置头像的图片分辨率不能超过 4096 x 4096<br>如有需要，请使用[上传文件](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/file/create)接口以文件形式上传高分辨率图片。
400 | 234041 | Tenant master key has been deleted, please contact the tenant administrator. | 租户加密密钥被删除，请联系租户管理员。
400 | 234042 | Hybrid deployment tenant storage error, such as full storage space, please contact tenant administrator. | 请求出现混部租户存储错误，如存储空间已满等，请联系租户管理员或[技术支持](https://applink.feishu.cn/TLJpeNdW)。

更多错误码信息，参见[通用错误码](https://open.feishu.cn/document/ukTMukTMukTM/ugjM14COyUjL4ITN)。
