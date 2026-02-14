# 分栏组件
分栏组件提供卡片内布局的能力，并提供对齐方式、容器宽度、交互方式等属性。你可以使用分栏组件横向排布多个列容器，在列容器内自由组合图文内容，搭建出如数据表、商品或文章列表、差旅信息等图文并茂、交互友好的卡片。

## 注意事项

分栏组件最多支持嵌套五层组件。建议你避免在分栏中嵌套多层组件。多层嵌套会压缩内容的展示空间，影响卡片的展示效果。

## 应用场景

- 分栏的使用场景非常广泛，在卡片中适当使用分栏，可以使信息排布更合理、主次更分明。常见场景如下所示。推荐你直接前往卡片搭建工具，查看[分栏示例](https://open.larkoffice.com/cardkit?catalogId=10015&templateId=AAqBEj6y7tTLV)。

- **数据报表推送：** 使用分栏可以快速构建整齐、自适应屏幕的多列数据表，解决了传统报表构建时繁琐的排版过程，以及无法自适应各类屏幕的样式问题。
    - **图文混排**：分栏灵活的横纵列排版能力，使你可以快速构建理想的图文卡片。有效降低手动调整图文排版的耗时。
    - **表单收集**：表单容器中内嵌分栏组件，将相关字段放在同一列，可有效提升内容的逻辑性和可读性。
- 分栏中还可配置点击链接、变量，推荐你直接前往卡片搭建工具，查看[分栏配置链接案例](https://open.larkoffice.com/cardkit?catalogId=10015&templateId=AAqBEj6y7tTLV)。

## 组件属性

### JSON 结构

分栏组件的完整 JSON 2.0 结构如下所示：

```JSON
{
    "schema": "2.0",
    "body": {
        "elements": [
            {
                "tag": "column_set", // 分栏的标签。
                "element_id": "custom_id", // 操作组件的唯一标识。用于在调用组件相关接口中指定组件。需开发者自定义。
                "margin": "4px", // 分栏的外边距，默认值 "0"，支持范围 [-99,99]px。
                "horizontal_spacing": "large", // 分栏内组件之间的间距，可选值："small"(4px)、"medium"(8px)、"large"(12px)、"extra_large"(16px)或[0,99]px。默认 8px。
                "horizontal_align": "left", // 分栏内组件水平对齐的方式，可选值："left"、"center"、"right"，默认值为 "left"。
                "flex_mode": "none", // 移动端和 PC 端的窄屏幕下，各列的自适应方式。默认值 none。
                "background_style": "default", // 分栏的背景色样式。默认值 default。
                "action": { // 在此处设置点击分栏时的交互配置。
                    "multi_url": {
                        "url": "https://open.feishu.cn",
                        "pc_url": "https://open.feishu.com",
                        "ios_url": "https://developer.apple.com/",
                        "android_url": "https://developer.android.com/"
                    }
                },
                "columns": [
                    // 列配置
                    {
                        "tag": "column",
                        "element_id": "custom_id", // 操作组件的唯一标识。用于在调用组件相关接口中指定组件。需开发者自定义。
                        "background_style": "default", // 列的背景色样式。默认值 default。
                        "width": "auto", // 列的宽度。默认值 auto。
                        "weight": 1, // 当 width 取值 weighted 时生效，表示当前列的宽度占比。
                        "horizontal_spacing": "large", // 列内组件之间的间距，可选值："small"(4px)、"medium"(8px)、"large"(12px)、"extra_large"(16px)或[0,99]px。默认 8px。
                        "horizontal_align": "left", // 列内组件水平对齐的方式，可选值："left"、"center"、"right"，默认值为 "left"。
                        "vertical_align": "center", // 列内组件的垂直对齐方式，可选值："top"、"center"、"bottom"，默认值为 "top"。
                        "vertical_spacing": "4px", // 列内子组件纵向间距。默认值 default（8px）。
                        "direction": "vertical", // 列的排列方向。可选值："vertical"（垂直排列）、"horizontal"（水平排列）。默认为 "vertical"。
                        "padding": "8px", // 列的内边距。默认值 0px。支持范围 [0,99]px。
                        "margin": "4px", // 列的外边距，默认值 0px。支持范围 [-99,99]px。
                        "action": {
                            // 在此处设置点击列时的交互配置。
                            "multi_url": {
                                "url": "https://www.baidu.com",
                                "pc_url": "https://www.baidu.com",
                                "ios_url": "https://www.google.com",
                                "android_url": "https://www.apple.com.cn"
                            }
                        },
                        "elements": [] // 列容器内嵌的组件，不支持内嵌表格和表单容器。
                    }
                ]
            }
        ]
    }
}
```

### 分栏字段说明

分栏（column_set）各属性字段说明如下表所示。

名称 | 必填 | 类型 | 默认值 | 说明
---|---|---|---|---
tag | 是 | String | / | 组件的标签。分栏组件的固定值为 column_set。
element_id | 否 | String | 空 | 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用[组件相关接口](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/cardkit-v1/card-element/create)中指定组件。在同一张卡片内，该字段的值全局唯一。仅允许使用字母、数字和下划线，必须以字母开头，不得超过 20 字符。
horizontal_spacing | 否 | String | 8px | 分栏内组件的水平间距，可选值：<br>- small：小间距，4px<br>- medium：中等间距，8px<br>- large：大间距，12px<br>- extra_large：超大间距，16px<br>- 具体数值，如 20px。取值范围为 [0,99]px
horizontal_align | 否 | String | left | 分栏内组件在水平方向上的对齐方式。可取值：<br>- left：左对齐<br>- center：居中对齐<br>- right：右对齐
margin | 否 | String | 0px | 分栏的外边距。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示分栏的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示分栏的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示分栏的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
flex_mode | 否 | String | none | 移动端和 PC 端的窄屏幕下，各列的自适应方式。取值：<br>- none：不做布局上的自适应，在窄屏幕下按比例压缩列宽度<br>- stretch：列布局变为行布局，且每列（行）宽度强制拉伸为 100%，所有列自适应为上下堆叠排布<br>- flow：列流式排布（自动换行），当一行展示不下一列时，自动换至下一行展示<br>- bisect：两列等分布局<br>- trisect：三列等分布局
background_style | 否 | String | default | 分栏的背景色样式。可取值：<br>- default：默认的白底样式，客户端深色主题下为黑底样式<br>- 卡片支持的颜色枚举值和 RGBA 语法自定义颜色。参考[颜色枚举值](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color)。<br>**注意**：当存在分栏的嵌套时，上层分栏的颜色覆盖下层分栏的颜色。
action | 否 | Action | / | 设置点击分栏时的交互配置。当前仅支持跳转交互。如果布局容器内有交互组件，则优先响应交互组件定义的交互。
└ multi_url | 否 | Struct | 空 | 配置各个端的链接地址。
└└ url | 否 | String | 空 | 兜底的跳转链接。
└└ android_url | 否 | String | 空 | Android 端的跳转链接。可配置为 `lark://msgcard/unsupported_action` 声明当前端不允许跳转。
└└ ios_url | 否 | String | 空 | iOS 端的跳转链接。可配置为 `lark://msgcard/unsupported_action` 声明当前端不允许跳转。
└└ pc_url | 否 | String | 空 | PC 端的跳转链接。可配置为 `lark://msgcard/unsupported_action` 声明当前端不允许跳转。
columns | 是 | column[] | 空 | 分栏中列的配置。详情参考下文。

### 列字段说明

分栏中列（column）的各属性字段说明如下表所示。

名称 | 必填 | 类型 | 默认值 | 说明
---|---|---|---|---
tag | 是 | String | / | 列的标签，固定取值为 `column`。
element_id | 否 | String | 空 | 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用[组件相关接口](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/cardkit-v1/card-element/create)中指定组件。在同一张卡片内，该字段的值全局唯一。仅允许使用字母、数字和下划线，必须以字母开头，不得超过 20 字符。
background_style | 否 | String | default | 列的背景色样式。可取值：<br>- default：默认的白底样式，客户端深色主题下为黑底样式<br>- 卡片支持的颜色枚举值和 RGBA 语法自定义颜色。参考[颜色枚举值](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color)
width | 否 | String | auto | 列宽度。仅 `flex_mode` 为 `none` 时，生效此属性。取值：<br>- auto：列宽度与列内元素宽度一致<br>- weighted：列宽度按 `weight` 参数定义的权重分布<br>- 具体数值，如 100px。取值范围为 [16,600]px。V7.4 及以上版本支持该枚举
weight | 否 | Number | 1 | 当 `width` 字段取值为 `weighted` 时生效，表示当前列的宽度占比。取值范围为 1 ~ 5 之间的整数。
horizontal_spacing | 否 | String | 8px | 列内组件的水平间距，可选值：<br>- small：小间距，4px<br>- medium：中等间距，8px<br>- large：大间距，12px<br>- extra_large：超大间距，16px<br>- 具体数值，如 20px。取值范围为 [0,99]px
horizontal_align | 否 | String | left | 列内组件在水平方向上的对齐方式。可取值：<br>- left：左对齐<br>- center：居中对齐<br>- right：右对齐
vertical_align | 否 | String | top | 列内组件在垂直方向上的对齐方式。可取值：<br>- top：上对齐<br>- center：居中对齐<br>- bottom：下对齐
vertical_spacing | 否 | String | 8px | 列内组件的纵向间距。可选值：<br>- small：小间距，4px<br>- medium：中等间距，8px<br>- large：大间距，12px<br>- extra_large：超大间距，16px<br>- 具体数值，如 20px。取值范围为 [0,99]px
direction | 否 | String | vertical | 列的排列方向。可选值：<br>- vertical：垂直排列<br>- horizontal：水平排列
padding | 否 | String | 0px | 列的内边距。值的取值范围为 [0,99]px。可选值：<br>- 单值，如 "10px"，表示列的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示列的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示列的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
margin | 否 | String | 0px | 列的外边距。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示容器的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示容器的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示容器的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
elements | 否 | Element 或 ColumnSet[] | 空 | 列中内嵌的组件。可内嵌组件参考上文嵌套关系。
action | 否 | Action | / | 设置点击列时的交互配置。当前仅支持跳转交互。如果布局容器内有交互组件，则优先响应交互组件定义的交互。
└ multi_url | 否 | Struct | 空 | 配置各个端的链接地址。
└└ url | 否 | String | 空 | 兜底的链接地址。
└└ android_url | 否 | String | 空 | Android 端的链接地址。可配置为 `lark://msgcard/unsupported_action` 声明当前端不允许跳转。
└└ ios_url | 否 | String | 空 | iOS 端的链接地址。可配置为 `lark://msgcard/unsupported_action` 声明当前端不允许跳转。
└└ pc_url | 否 | String | 空 | PC 端的链接地址。可配置为 `lark://msgcard/unsupported_action` 声明当前端不允许跳转。

# 折叠面板

折叠面板允许在卡片中折叠次要信息，如备注、较长文本等，以突出主要信息。

## 注意事项

- 折叠面板仅支持通过撰写卡片 JSON 代码的方式使用，暂不支持在卡片搭建工具上构建使用。
- 容器类组件最多支持嵌套五层组件。建议你避免在折叠面板中嵌套多层组件。多层嵌套会压缩内容的展示空间，影响卡片的展示效果。

## 嵌套规则

折叠面板不支持内嵌表单容器（form）组件。

## 组件属性

本小节介绍折叠面板的属性。

### JSON 结构

折叠面板组件的完整 JSON 2.0 结构如下所示：
```json
{
  "schema": "2.0", // 卡片 JSON 结构的版本。默认为 1.0。要使用 JSON 2.0 结构，必须显示声明 2.0。
  "body": {
    "elements": [
      {
        "tag": "collapsible_panel", // 折叠面板的标签。
        "element_id": "custom_id", // 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用组件相关接口中指定组件。需开发者自定义。
        "direction": "vertical", // 面板内组件的排列方向。JSON 2.0 新增属性。可选值："vertical"（垂直排列）、"horizontal"（水平排列）。默认为 "vertical"。
        "vertical_spacing": "8px", // 面板内组件的垂直间距。JSON 2.0 新增属性。可选值："small"(4px)、"medium"(8px)、"large"(12px)、"extra_large"(16px)或[0,99]px。
        "horizontal_spacing": "8px", // 面板内组件内的垂直间距。JSON 2.0 新增属性。可选值："small"(4px)、"medium"(8px)、"large"(12px)、"extra_large"(16px)或[0,99]px。
        "vertical_align": "top", // 面板内组件的垂直居中方式。JSON 2.0 新增属性。默认值为 top。
        "horizontal_align": "left", // 面板内组件的水平居中方式。JSON 2.0 新增属性。默认值为 left。
        "padding": "8px 8px 8px 8px", // 折叠面板的内边距。JSON 2.0 新增属性。支持范围 [0,99]px。
        "margin": "0px 0px 0px 0px", // 折叠面板的外边距。JSON 2.0 新增属性。默认值 "0"，支持范围 [-99,99]px。
        "expanded": true, // 面板是否展开。默认值 false。
        "background_color": "grey", // 折叠面板的背景色，默认为透明。
        "header": {
          // 折叠面板的标题设置。
          "title": {
            // 标题文本设置。支持 plain_text 和 markdown。
            "tag": "markdown",
            "content": "**面板标题文本**"
          },
          "background_color": "grey", // 标题区的背景色，默认为透明。
          "vertical_align": "center", // 标题区的垂直居中方式。
          "padding": "4px 0px 4px 8px", // 标题区的内边距。
          "position": "top", // 标题区的位置。
          "width": "auto", // 标题区的宽度。默认值为 fill。
          "icon": {
            // 标题前缀图标
            "tag": "standard_icon", // 图标类型.
            "token": "chat-forbidden_outlined", // 图标库中图标的 token。当 tag 为 standard_icon 时生效。
            "color": "orange", // 图标的颜色。当 tag 为 standard_icon 时生效。
            "img_key": "img_v2_38811724", // 自定义前缀图标的图片 key。当 tag 为 custom_icon 时生效。
            "size": "16px 16px" // 图标的尺寸。默认值为 10px 10px。
          },
          "icon_position": "follow_text", // 图标的位置。默认值为 right。
          "icon_expanded_angle": -180 // 折叠面板展开时图标旋转的角度，正值为顺时针，负值为逆时针。默认值为 180。
        },
        "border": {
          // 边框设置。默认不显示边框。
          "color": "grey", // 边框的颜色。
          "corner_radius": "5px" // 圆角设置。
        },
        "elements": [
          // 此处可添加各个组件的 JSON 结构。暂不支持表单（form）组件。
          {
            "tag": "markdown",
            "content": "很长的文本"
          }
        ]
      }
    ]
  }
}
```

### 字段说明

折叠面板各字段说明如下表所示：

名称 | 必填 | 类型 | 默认值 | 说明
---|---|---|---|---
tag | 否 | string | / | 组件的标签。折叠面板取固定值为 <code>collapsible_panel</code>。
expanded | 否 | Boolean | false | 面板是否展开。可选值：<br>- <code>true</code>：面板为展开状态<br>- <code>false</code>：面板为折叠状态。默认为折叠状态
element_id | 否 | String | 空 | 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用[组件相关接口](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/cardkit-v1/card-element/create)中指定组件。在同一张卡片内，该字段的值全局唯一。仅允许使用字母、数字和下划线，必须以字母开头，不得超过 20 字符。
margin | 否 | String | 0px | 容器的外边距。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示容器的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示容器的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示容器的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
horizontal_spacing | 否 | String | 8px | 容器内组件的水平间距，可选值：<br>- small：小间距，4px<br>- medium：中等间距，8px<br>- large：大间距，12px<br>- extra_large：超大间距，16px<br>- 具体数值，如 20px。取值范围为 [0,99]px
horizontal_align | 否 | String | left | 容器内组件水平对齐的方式。可取值：<br>- left：左对齐<br>- center：居中对齐<br>- right：右对齐
vertical_spacing | 否 | String | 12px | 容器内组件的水平间距，可选值：<br>- small：小间距，4px<br>- medium：中等间距，8px<br>- large：大间距，12px<br>- extra_large：超大间距，16px<br>- 具体数值，如 20px。取值范围为 [0,99]px
vertical_align | 否 | String | top | 容器内组件垂直对齐的方式。可取值：<br>- top：上对齐<br>- center：居中对齐<br>- bottom：下对齐
direction | 否 | String | vertical | 容器的排列方向。可选值：<br>- vertical：垂直排列<br>- horizontal：水平排列
padding | 否 | String | 0px | 容器的内边距。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示容器的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示容器的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示容器的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
background_color | 否 | String | 空 | 折叠面板的背景色，默认为透明。枚举值参见[颜色枚举值](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color)。
header | 是 | Object | - | 折叠面板的标题设置。
└ title | 否 | Object | - | 标题文本设置。
└└ tag | 是 | String | 空 | 文本类型的标签。可取值：<br>- <code>plain_text</code>：普通文本内容<br>- <code>markdown</code>：富文本内容。了解支持的 Markdown 语法，参考[富文本组件](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-components/content-components/rich-text)。
└└ content | 否 | String | 空 | 折叠面板标题的内容。
└ background_color | 否 | String | 空 | 折叠面板标题区域的背景颜色设置，默认为透明色。枚举值参见[颜色枚举值](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color)。<br>**注意**：如果你未设置此字段，则折叠面板的标题区域的背景色由 <code>background_color</code> 字段决定。
└ width | 否 | String | fill | 标题元素的宽度。JSON 2.0 新增属性。支持飞书客户端 7.32 及以上版本。<br>- `fill`：标题和折叠面板等宽<br>- `auto`：标题自适应文本长度<br>- `auto_when_fold`：仅在折叠面板收起后，标题自适应文本长度
└ vertical_align | 否 | String | center | 标题区域的垂直居中方式。可取值：<br>- <code>top</code>：标题区域垂直居中于面板区域的顶部<br>- <code>center</code>：标题区域垂直居中于面板区域的中间<br>- <code>bottom</code>：标题区域垂直居中于面板区域的底部
└ padding | 否 | String | 0 | 标题区域的内边距。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示标题区的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示标题区的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示标题区的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
└ icon | 否 | Object | / | 添加图标作为标题前缀或后缀图标。支持自定义或使用图标库中的图标。示例代码如下：<br>```json<br>"icon": {<br>"tag": "standard_icon",<br>"token": "down-small-ccm_outlined",<br>"color": "",<br>"size": "16px 16px"<br>}<br>```
└└ tag | 否 | String | / | 图标类型的标签。可取值：<br>- <code>standard_icon</code>：使用图标库中的图标<br>- <code>custom_icon</code>：使用用自定义图片作为图标
└ └ token | 否 | String | / | 图标库中图标的 token。当 <code>tag</code> 为 <code>standard_icon</code> 时生效。枚举值参见[图标库](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-icons)。
└└ color | 否 | String | / | 图标的颜色。支持设置线性和面性图标（即 token 末尾为 <code>outlined</code> 或 <code>filled</code> 的图标）的颜色。当 <code>tag</code> 为 <code>standard_icon</code> 时生效。枚举值参见[颜色枚举值](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color)。
└└ img_key | 否 | String | / | 自定义前缀图标的图片 key。当 <code>tag</code> 为 <code>custom_icon</code> 时生效。图标 key 的获取方式：调用[上传图片](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/create)接口，上传用于发送消息的图片，并在返回值中获取图片的 image_key。
└ └ size | 否 | String | 10px 10px | 图标的尺寸。支持 "[1,999] [1,999]px"。
└ icon_position | 否 | String | right | 图标的位置。可选值：<br>- <code>left</code>：图标在标题区域最左侧<br>- <code>right</code>：图标在标题区域最右侧<br>- <code>follow_text</code>：图标在文本右侧
└ icon_expanded_angle | 否 | Number | 180 | 折叠面板展开时图标旋转的角度，正值为顺时针，负值为逆时针。可选值：<br>- <code>-180</code>：逆时针旋转 180 度<br>- <code>-90</code>：逆时针旋转 90 度<br>- <code>90</code>：顺时针旋转 90 度<br>- <code>180</code>：顺时针旋转 180 度
border | 否 | Object | 空 | 边框设置。默认不显示边框。
└ color | 否 | String | grey | 边框颜色设置。枚举值参见[颜色枚举值](https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/enumerations-for-fields-related-to-color)。
└ corner_radius | 否 | String | 5px | 圆角设置。
elements | 否 | Array | 空 | 各个组件的 JSON 结构。暂不支持表单（form）组件。