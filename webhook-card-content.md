# 标题组件

卡片的标题组件支持添加卡片主标题、副标题、后缀标签和标题图标。

## 注意事项

同一张卡片仅支持添加一个标题组件。

## 组件属性

### JSON 结构

标题组件的完整 JSON 2.0 结构如下所示：
```json
{
  "schema": "2.0", // 卡片 JSON 结构的版本。默认为 1.0。要使用 JSON 2.0 结构，必须显示声明 2.0。
  "header": {
    "title": {
      // 卡片主标题。必填。要为标题配置多语言，参考配置卡片多语言文档。
      "tag": "plain_text", // 文本类型的标签。可选值：plain_text 和 lark_md。
      "content": "示例标题" // 标题内容。
    },
    "subtitle": {
      // 卡片副标题。可选。
      "tag": "plain_text", // 文本类型的标签。可选值：plain_text 和 lark_md。
      "content": "示例文本" // 标题内容。
    },
    "text_tag_list": [
      // 标题后缀标签，最多设置 3 个 标签，超出不展示。可选。
      {
        "tag": "text_tag",
        "element_id": "custom_id", // 操作元素的唯一标识。用于在调用组件相关接口中指定元素。需开发者自定义。
        "text": {
          // 标签内容
          "tag": "plain_text",
          "content": "标签 1"
        },
        "color": "neutral" // 标签颜色
      }
    ],
    "i18n_text_tag_list": {
      // 多语言标题后缀标签。每个语言环境最多设置 3 个 tag，超出不展示。可选。同时配置原字段和国际化字段，优先生效多语言配置。
      "zh_cn": [],
      "en_us": [],
      "ja_jp": [],
      "zh_hk": [],
      "zh_tw": []
    },
    "template": "blue", // 标题主题样式颜色。支持 "blue"|"wathet"|"turquoise"|"green"|"yellow"|"orange"|"red"|"carmine"|"violet"|"purple"|"indigo"|"grey"|"default"。默认值 default。
    "icon": { // 前缀图标。
      "tag": "standard_icon", // 图标类型。
      "token": "chat-forbidden_outlined", // 图标的 token。仅在 tag 为 standard_icon 时生效。
      "color": "orange", // 图标颜色。仅在 tag 为 standard_icon 时生效。
      "img_key": "img_v2_38811724" // 图片的 key。仅在 tag 为 custom_icon 时生效。
    },
    "padding": "12px 8px 12px 8px" // 标题组件的内边距。JSON 2.0 新增属性。默认值 "12px"，支持范围 [0,99]px。    
  }
}
```

### 字段说明

标题组件的字段说明如下表。

名称 | 必填 | 类型 | 说明
---|---|---|---
title | 是 | Object | 配置卡片的主标题信息。<br>**注意**：如果只配置副标题，则实际展示为主标题效果。
└ tag | 是 | String | 文本类型的标签。可取值：<br>- `plain_text`：普通文本内容或[表情](https://www.feishu.cn/docx/doxcnG6utI72jB4eHJF1s5IgVJf)<br>- `lark_md`：支持以下 Markdown 语法的文本内容：<br>- @指定人：<br>```<br><at id=open_id></at><br><at id=user_id></at><br><at ids=id_01,id_02,xxx></at><br><at email=test@email.com></at><br>```<br>- @所有人：`<at id=all></at>`<br>- emoji：😁😢🌞💼🏆❌✅。直接复制表情即可。了解更多 emoji 表情，参考 [Emoji 表情符号大全](https://www.feishu.cn/docx/doxcnG6utI72jB4eHJF1s5IgVJf)。<br>- 飞书表情：如 `:OK:`。参考[表情文案说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-reaction/emojis-introduce)。
└ content | 否 | String | 卡片主标题内容。要为标题配置多语言，参考[配置卡片多语言](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/configure-multi-language-content)。<br>**注意**：主标题内容最多四行，超出四行的内容用 `...` 省略。
subtitle | 否 | Object | 配置卡片的副标题信息。<br>**注意**：如果只配置副标题，则实际展示为主标题效果。
└ tag | 是 | String | 文本类型的标签。可取值：<br>- `plain_text`：普通文本内容或[表情](https://www.feishu.cn/docx/doxcnG6utI72jB4eHJF1s5IgVJf)<br>- `lark_md`：支持以下 Markdown 语法的文本内容：<br>- @指定人：<br>```<br><at id=open_id></at><br><at id=user_id></at><br><at ids=id_01,id_02,xxx></at><br><at email=test@email.com></at><br>```<br>- @所有人：`<at id=all></at>`<br>- emoji：😁😢🌞💼🏆❌✅。直接复制表情即可。了解更多 emoji 表情，参考 [Emoji 表情符号大全](https://www.feishu.cn/docx/doxcnG6utI72jB4eHJF1s5IgVJf)。<br>- 飞书表情：如 `:OK:`。参考[表情文案说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-reaction/emojis-introduce)。
└ content | 否 | String | 卡片副标题内容。要为标题配置多语言，参考[配置卡片多语言](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/configure-multi-language-content)。<br>**注意**：副标题内容最多一行，超出一行的内容用 `...` 省略。
text_tag_list | 否 | TextTagList | 添加标题的后缀标签。最多可添加 3 个标签内容，如果配置的标签数量超过 3 个，则取前 3 个标签进行展示。标签展示顺序与数组顺序一致。<br>**注意**：<br>`text_tag_lis`t 和 `i18n_text_tag_list` 只能配置其中之一。如果同时配置仅生效 `i18n_text_tag_list`。
└ tag | 是 | String | 后缀标签的标识。固定取值：`text_tag`。
└ element_id | 否 | String | 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用[组件相关接口](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/cardkit-v1/card-element/create)中指定组件。在同一张卡片内，该字段的值全局唯一。仅允许使用字母、数字和下划线，必须以字母开头，不得超过 20 字符。
└ text | 否 | Text Object | 后缀标签的内容。基于文本组件的 plain_text 模式定义内容。<br>示例值：<br>```JSON<br>"text": {<br>"tag": "plain_text",<br>"content": "这里是标签"<br>}<br>```
└ color | 否 | String | 后缀标签的颜色，默认为蓝色（blue）。可选值与示例效果参见下文的后缀标签颜色枚举。
i18n_text_tag_list | 否 | Object | 配置后缀标签的多语言属性，在所需语种字段下添加完整的后缀标签结构体即可。每个语言最多可配置 3 个标签内容，如果配置的标签数量超过 3 个，则取前 3 个标签进行展示。标签展示顺序与数组顺序一致。支持设置的多语言枚举值如下：<br>- zh_cn：简体中文<br>- en_us：英文<br>- ja_jp：日文<br>- zh_hk：繁体中文（中国香港）<br>- zh_tw：繁体中文（中国台湾）<br>- id_id: 印尼语<br>- vi_vn: 越南语<br>- th_th: 泰语<br>- pt_br: 葡萄牙语<br>- es_es: 西班牙语<br>- ko_kr: 韩语<br>- de_de: 德语<br>- fr_fr: 法语<br>- it_it: 意大利语<br>- ru_ru: 俄语<br>- ms_my: 马来语<br>示例配置：<br>```json<br>"i18n_text_tag_list": {<br>"zh_cn": [<br>{<br>"tag": "text_tag",<br>"text": {<br>"tag": "plain_text",<br>"content": "标签内容"<br>},<br>"color": "carmine"<br>}<br>],<br>"en_us": [<br>{<br>"tag": "text_tag",<br>"text": {<br>"tag": "plain_text",<br>"content": "Tag content"<br>},<br>"color": "carmine"<br>}<br>]<br>}<br>```<br>**注意**：<br>`text_tag_list` 和 `i18n_text_tag_list` 只能配置其中之一。如果同时配置两个字段，则优先生效多语言配置。
template | 否 | String | 配置标题主题颜色。可选值与示例效果参见下文的标题主题样式枚举。
icon | 否 | Object | 添加图标作为文本前缀图标。支持自定义或使用图标库中的图标。
└ tag | 否 | String | 图标类型的标签。可取值：<br>- `standard_icon`：使用图标库中的图标。<br>- `custom_icon`：使用用自定义图片作为图标。
└ token | 否 | String | 图标库中图标的 token。当 `tag` 为 `standard_icon` 时生效。枚举值参见[图标库](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-icons)。
└ color | 否 | String | 图标的颜色。支持设置线性和面性图标（即 token 末尾为 `outlined` 或 `filled` 的图标）的颜色。当 `tag` 为 `standard_icon` 时生效。枚举值参见[颜色枚举值](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color)。
└ img_key | 否 | String | 自定义前缀图标的图片 key。当 `tag` 为 `custom_icon` 时生效。<br>图标 key 的获取方式：调用[上传图片](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/create)接口，上传用于发送消息的图片，并在返回值中获取图片的 image_key。
padding | 否 | String | 标题组件的内边距。默认为 12px。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示容器的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示容器的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示容器的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。

## 枚举

### 标题主题样式枚举

`template` 字段支持的枚举值：`blue`、`wathet`、`turquoise`、`green`、`yellow`、`orange`、`red`、`carmine`、`violet`、`purple`、`indigo`、`grey`、`default`。

### 后缀标签颜色枚举

`text_tag_list` 或 `i18n_text_tag_list` 中的 `color` 字段支持的枚举值：`neutral`、`blue`、`turquoise`、`lime`、`orange`、`violet`、`indigo`、`wathet`、`green`、`yellow`、`red`、`purple`、`carmine`。

## 标题主题样式建议

- 群聊中可使用彩色标题，配置为品牌色或语义色增强视觉锚点。
- 单聊中建议根据卡片状态配置：
  - `green`：完成或成功
  - `orange`：警告或警示
  - `red`：错误或异常
  - `grey`：失效


# 富文本组件

JSON 2.0 结构卡片的富文本（Markdown）组件支持渲染标题、表情、表格、图片、代码块、分割线等元素。

## 组件属性

### JSON 结构

富文本组件的完整 JSON 2.0 结构如下所示：
```json
{
  "schema": "2.0", // 卡片 JSON 结构的版本。默认为 1.0。要使用 JSON 2.0 结构，必须显示声明 2.0。
  "body": {
    "elements": [
      {
        "tag": "markdown",
        "element_id": "custom_id", // 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用组件相关接口中指定组件。需开发者自定义。
        "margin": "0px 0px 0px 0px", // 组件的外边距，JSON 2.0 新增属性。默认值 "0"，支持范围 [-99,99]px。
        "content": "人员<person id = 'ou_449b53ad6aee526f7ed311b216aabcef' show_name = true show_avatar = true style = 'normal'></person>", // 采用 mardown 语法编写的内容。2.0 结构不再支持 "[差异化跳转]($urlVal)" 语法
        "text_size": "normal", // 文本大小。默认值 normal。支持自定义在移动端和桌面端的不同字号。
        "text_align": "left", // 文本对齐方式。默认值 left。
        "icon": {
          // 前缀图标。
          "tag": "standard_icon", // 图标类型。
          "token": "chat-forbidden_outlined", // 图标的 token。仅在 tag 为 standard_icon 时生效。
          "color": "orange", // 图标颜色。仅在 tag 为 standard_icon 时生效。
          "img_key": "img_v2_38811724" // 图片的 key。仅在 tag 为 custom_icon 时生效。
        }
      }
    ]
  }
}
```

### 字段说明

富文本组件包含的参数说明如下表所示。

字段名称 | 是否必填 | 类型 | 默认值 | 说明
---|---|---|---|---
tag | 是 | String | / | 组件的标签。富文本组件固定取值为 `markdown`。
element_id | 否 | String | 空 | 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用[组件相关接口](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/cardkit-v1/card-element/create)中指定组件。在同一张卡片内，该字段的值全局唯一。仅允许使用字母、数字和下划线，必须以字母开头，不得超过 20 字符。
margin | 否 | String | 0 | 组件的外边距。JSON 2.0 新增属性。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示组件的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示组件的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示组件的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
text_align | 否 | String | left | 设置文本内容的对齐方式。可取值有：<br>* left：左对齐<br>* center：居中对齐<br>* right：右对齐
text_size | 否 | String | normal | 文本大小。可取值如下所示。如果你填写了其它值，卡片将展示为 `normal` 字段对应的字号。<br>- heading-0：特大标题（30px）<br>- heading-1：一级标题（24px）<br>- heading-2：二级标题（20 px）<br>- heading-3：三级标题（18px）<br>- heading-4：四级标题（16px）<br>- heading：标题（16px）<br>- normal：正文（14px）<br>- notation：辅助信息（12px）<br>- xxxx-large：30px<br>- xxx-large：24px<br>- xx-large：20px<br>- x-large：18px<br>- large：16px<br>- medium：14px<br>- small：12px<br>- x-small：10px
icon | 否 | Object | / | 添加图标作为文本前缀图标。支持自定义或使用图标库中的图标。
└ tag | 否 | String | / | 图标类型的标签。可取值：<br>-   `standard_icon`：使用图标库中的图标。<br>-   `custom_icon`：使用用自定义图片作为图标。
└ token | 否 | String | / | 图标库中图标的 token。当 `tag` 为 `standard_icon` 时生效。枚举值参见[图标库](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-icons)。
└ color | 否 | String | / | 图标的颜色。支持设置线性和面性图标（即 token 末尾为 `outlined` 或 `filled` 的图标）的颜色。当 `tag` 为 `standard_icon` 时生效。枚举值参见[颜色枚举值](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color)。
└ img_key | 否 | String | / | 自定义前缀图标的图片 key。当 `tag` 为 `custom_icon` 时生效。<br>图标 key 的获取方式：调用[上传图片](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/create)接口，上传用于发送消息的图片，并在返回值中获取图片的 image_key。
content | 是 | String | / | Markdown 文本内容。了解支持的语法，参考下文。

### 特殊字符转义说明
如果要展示的字符命中了 markdown 语法使用的特殊字符（例如 `*、~、>、<` 这些特殊符号），需要对特殊字符进行 HTML 转义，才可正常展示。常见的转义符号对照表如下所示。查看更多转义符，参考 [HTML 转义通用标准](https://www.w3school.com.cn/charsets/ref_html_8859.asp)实现，转义后的格式为 `&#实体编号;`。

| **特殊字符** | **转义符** | **描述** |
| --- | --- | --- |
| ` ` | `&nbsp;        ` | 不换行空格 |
| ` ` | `&ensp;` | 半角空格 |
| `  ` | `&emsp;` | 全角空格 |
| `>` | `&#62;` | 大于号 |
| `<` | `&#60;` | 小于号 |
| `~` | `&sim;` | 飘号 |
| `-` | `&#45;` | 连字符 |
| `!` | `&#33;` | 惊叹号 |
| `*` | `&#42;` | 星号 |
| `/` | `&#47;` | 斜杠 |
| `\` | `&#92;` | 反斜杠 |
| `[` | `&#91;` | 中括号左边部分 |
| `]` | `&#93;` | 中括号右边部分 |
| `(` | `&#40;` | 小括号左边部分 |
| `)` | `&#41;` | 小括号右边部分 |
| `#` | `&#35;` | 井号 |
| `:` | `&#58;` | 冒号 |
| `+` | `&#43;` | 加号 |
| `"` | `&#34;` | 英文引号 |
| `'` | `&#39;` | 英文单引号 |
| \`  | `&#96;` | 反单引号 |
| `$` | `&#36;` | 美金符号 |
| `_` | `&#95;` | 下划线 |
| `-` | `&#45;` | 无序列表 |

# 图片组件

飞书卡片支持图片组件。

## 注意事项

-   在 JSON 2.0 结构中，图片组件的 `size` 属性不再支持传入 `stretch_without_padding` 实现通栏效果，你需设置 `margin` 属性为负数实现通栏效果：

```json
    {
      "schema": "2.0", // 卡片 JSON 结构的版本。默认为 1.0。要使用 JSON 2.0 结构，必须显示声明 2.0。
      "body": {
        "elements": [
          {
            "tag": "img",
            "img_key": "img_v3_0238_073f1823-df2b-4377-86c6-e293f183622j",
            "scale_type": "crop_center",
            "margin": "4px -12px"
          }
        ]
      }
    }
    ```
为保证图片在聊天窗口中呈现的清晰度，建议你在组件中上传的图片遵从以下规范：

- 图片尺寸在 1500 × 3000 px 的范围内。
- 图片大小不超过 10 M。
- 图片的 `高度:宽度` 不超过 `16:9`。

## JSON 结构

图片组件的完整 JSON 2.0 结构如下所示：
```json
{
  "schema": "2.0", // 卡片 JSON 结构的版本。默认为 1.0。要使用 JSON 2.0 结构，必须显示声明 2.0。
  "body": {
    "elements": [
      {
        "tag": "img",
        "element_id": "custom_id", // 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用组件相关接口中指定组件。需开发者自定义。
        "margin": "0px 0px 0px 0px", // 组件的外边距。JSON 2.0 新增属性。默认值 "0"，支持范围 [-99,99]px。
        "img_key": "img_v3_0238_073f1823-df2b-4377-86c6-e293f18abcef", // 图片的 Key。可通过上传图片接口或在搭建工具中上传图片后获得。
        "alt": {
          // 光标悬浮（hover）在图片上时展示的说明。
          "tag": "plain_text",
          "content": ""
        },
        "title": {
          // 图片标题。
          "tag": "plain_text",
          "content": ""
        },
        "corner_radius": "5px", // 图片的圆角半径。
        "scale_type": "crop_top", // 图片的裁剪模式，当 size 字段的比例和图片的比例不一致时会触发裁剪。
        "size": "100px 100px", // 图片尺寸。仅在 scale_type 字段为 crop_center 或 crop_top 时生效。
        "transparent": false, // 是否为透明底色。默认为 false，即图片为白色底色。
        "preview": false, // 点击后是否放大图片。默认值为 true。
        // 历史属性
        "mode": "large", // 图片尺寸模式。
        "custom_width": "300px", // 自定义图片的最大展示宽度。
        "compact_width": false // 是否展示为紧凑型的图片。
      }
    ]
  }
}
```

# 分割线组件

你可以在卡片中添加分割线组件，使卡片内容更清晰。

本文档介绍分割线组件的 JSON 2.0 结构，要查看历史 JSON 1.0 结构，参考[分割线](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-components/content-components/divider)。

![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/062d8c93b9b67ee9fb8c4188c19097d5_6kwLHW7Hfi.png?height=224&lazyload=true&maxWidth=300&width=559)

## JSON 结构

分割线的完整 JSON 2.0 结构如下所示：
```json
{
    "schema": "2.0",
    "body": {
        "elements": [
            {
                "tag": "hr",
                "element_id": "custom_id", // 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用组件相关接口中指定组件。需开发者自定义。
                "margin": "0px 0px 0px 0px" // 组件的外边距。JSON 2.0 新增属性。默认值 "0"，支持范围 [-99,99]px。
            }
        ]
    }
}
```