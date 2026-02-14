# 图表组件

飞书卡片提供的图表组件基于 [VChart]的图表定义，支持折线图、面积图、柱状图、饼图、词云等多种数据呈现方式，帮助你可视化各类信息，提高信息沟通效率。

## 注意事项

- 单张卡片建议最多放置五个图表组件。

## 功能特性

基于图表组件绘制的图表，支持以下功能：
- **图表可交互**：用户可通过点击图表展示数据标签、点击图例实现数据过滤、拖拽缩略轴进行数据筛选。
- **样式自适应**：支持图表多种样式的呈现，并在不同设备端、不同色彩模式下有良好的自适应展示效果；
- **支持放大查看**：PC 端上，图表支持独立窗口查看；移动端上，图表支持点击后全屏查看。

## 组件属性

### JSON 结构

图表组件的完整 JSON 2.0 结构如下所示：
```json
{
    "schema": "2.0", // 卡片 JSON 结构的版本。默认为 1.0。要使用 JSON 2.0 结构，必须显示声明 2.0。
    "body": {
        "elements": [
            // 飞书客户端 7.1 及之后版本支持的属性
            {
                "tag": "chart", // 组件的标签。
                "element_id": "custom_id", // 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用组件相关接口中指定组件。需开发者自定义。
                "margin": "0px 0px 0px 0px", // 组件的外边距。JSON 2.0 新增属性。默认值 "0"，支持范围 [-99,99]px。
                "aspect_ratio": "16:9", // 图表宽高比。
                "color_theme": "brand", // 图表主题。默认值 brand。
                "chart_spec": {}, // 基于 VChart 的图表定义，详细用法参考 VChart 官方文档。
                "preview": false, // 是否支持独立窗口查看，默认值 true。
                "height": "auto" // 图表组件的高度，默认值 auto，即根据宽高比自动计算。
            }
        ]
    }
}
```

### 字段说明

图表组件的字段说明如下表。

名称 | 必填 | 类型 | 默认值 | 说明
---|---|---|---|---
tag | 是 | String | 空 | 组件的标签，图表组件的标签为固定值 `chart`。
element_id | 否 | String | 空 | 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用[组件相关接口](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/cardkit-v1/card-element/create)中指定组件。在同一张卡片内，该字段的值全局唯一。仅允许使用字母、数字和下划线，必须以字母开头，不得超过 20 字符。
margin | 否 | String | 0 | 组件的外边距。JSON 2.0 新增属性。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示组件的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示组件的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示组件的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
aspect_ratio | 否 | String | -   PC 端：16:9<br>- 移动端：1:1 | 图表的宽高比。支持以下比例：<br>-   1:1<br>-   2:1<br>-   4:3<br>-   16:9
color_theme | 否 | String | brand | 图表的主题样式。当图表内存在多个颜色时，可使用该字段调整颜色样式。若你在 `chart_spec` 字段中声明了样式类属性，该字段无效。<br>-   brand：默认样式，与飞书客户端主题样式一致。<br>-   rainbow：同色系彩虹色。<br>-   complementary：互补色。<br>-   converse：反差色。<br>-   primary：主色。
chart_spec | 是 | VChart spec 结构体 | 空 | 基于 VChart 的图表定义。详细用法参考 [VChart 官方文档](https://www.visactor.io/vchart/guide/tutorial_docs/Chart_Concepts/Understanding_VChart)。<br>**提示**：<br>- 在飞书 7.1 - 7.6 版本上，图表组件支持的 VChart 版本为 1.2.2；<br>- 在飞书 7.7 - 7.9 版本上，图表组件支持的 VChart 版本为 1.6.6；<br>- 在飞书 7.10 - 7.15 版本上，图表组件支持的 VChart 版本为 1.8.3；<br>- 在飞书 7.16 -7.26 版本上，图表组件支持的 VChart 版本为 1.10.1。<br>- 在飞书 7.27 及以上版本上，图表组件支持的 VChart 版本为 1.12.3。<br>了解 VChart 版本更新，参考 [VChart Changelogs](https://www.visactor.io/vchart/changelog/release)。
preview | 否 | Boolean | true | 图表是否可在独立窗口查看。可取值：<br>-   true：默认值。<br>-   PC 端：图表可在独立飞书窗口查看<br>-   移动端：图表可在点击后全屏查看<br>-   false：<br>-   PC 端：图表不支持在独立飞书窗口查看<br>-   移动端：图表不支持在点击后全屏查看
height | 否 | String | auto | 图表组件的高度，可取值：<br>-   auto：默认值，高度将根据宽高比自动计算。<br>-   [1,999]px：自定义固定图表高度，此时宽高比属性 `aspect_ratio` 失效。

## 图表类型与示例

图表组件基于 VChart 1.6.x 版本，当前支持折线图、面积图、柱状图、条形图等 13 种图表。本小节列出各个图表的卡片效果和 JSON 2.0 结构示例。要查看各类图表属性的详细说明，参考 [VChart 配置文档](https://www.visactor.io/vchart/option/barChart)。

### 折线图

折线图一般用于展示数据随时间变化的趋势。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "line",<br>"title": {<br>"text": "折线图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"xField": "time",<br>"yField": "value"<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>}<br>``` | ```json<br>[<br>{<br>"time": "2:00",<br>"value": 8<br>},<br>{<br>"time": "4:00",<br>"value": 9<br>},<br>{<br>"time": "6:00",<br>"value": 11<br>},<br>{<br>"time": "8:00",<br>"value": 14<br>},<br>{<br>"time": "10:00",<br>"value": 16<br>},<br>{<br>"time": "12:00",<br>"value": 17<br>},<br>{<br>"time": "14:00",<br>"value": 17<br>},<br>{<br>"time": "16:00",<br>"value": 16<br>},<br>{<br>"time": "18:00",<br>"value": 15<br>}<br>]

### 面积图

面积图类似于折线图，可用于展示数据随时间变化的趋势。面积图下方的填充区域可用于强调累积的总体趋势。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "area",<br>"title": {<br>"text": "面积图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"xField": "time",<br>"yField": "value"<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>}<br>``` | ```json<br>[<br>{<br>"time": "2:00",<br>"value": 8<br>},<br>{<br>"time": "4:00",<br>"value": 9<br>},<br>{<br>"time": "6:00",<br>"value": 11<br>},<br>{<br>"time": "8:00",<br>"value": 14<br>},<br>{<br>"time": "10:00",<br>"value": 16<br>},<br>{<br>"time": "12:00",<br>"value": 17<br>},<br>{<br>"time": "14:00",<br>"value": 17<br>},<br>{<br>"time": "16:00",<br>"value": 16<br>},<br>{<br>"time": "18:00",<br>"value": 15<br>}<br>]<br>```

### 柱状图

柱状图多用于比较不同组或类别之间的数据，可清晰地展示各组之间的差异。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "bar",<br>"title": {<br>"text": "柱状图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"xField": [<br>"year",<br>"type"<br>],<br>"yField": "value",<br>"seriesField": "type",<br>"legends": {<br>"visible": true,<br>"orient": "bottom"<br>}<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>} | ```json<br>[<br>{ "type": "Autoc", "year": "1930", "value": 129 },<br>{ "type": "Autoc", "year": "1940", "value": 133 },<br>{ "type": "Autoc", "year": "1950", "value": 130 },<br>{ "type": "Autoc", "year": "1960", "value": 126 },<br>{ "type": "Autoc", "year": "1970", "value": 117 },<br>{ "type": "Autoc", "year": "1980", "value": 114 },<br>{ "type": "Democ", "year": "1930", "value": 22 },<br>{ "type": "Democ", "year": "1940", "value": 13 },<br>{ "type": "Democ", "year": "1950", "value": 25 },<br>{ "type": "Democ", "year": "1960", "value": 29 },<br>{ "type": "Democ", "year": "1970", "value": 38 },<br>{ "type": "Democ", "year": "1980", "value": 41 }<br>]<br>```

### 条形图

条形图与柱状图类似，但是为横向显示(`"direction": "horizontal"`)。通常用于比较不同类别的数据，在数据标签较长或类别较多时更易于阅读。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "bar",<br>"title": {<br>"text": "条形图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"direction": "horizontal",<br>"xField": "value",<br>"yField": "name"<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>}<br>``` | ```json<br>[<br>{<br>"name": "Apple",<br>"value": 214480<br>},<br>{<br>"name": "Google",<br>"value": 155506<br>},<br>{<br>"name": "Amazon",<br>"value": 100764<br>},<br>{<br>"name": "Microsoft",<br>"value": 92715<br>},<br>{<br>"name": "Coca-Cola",<br>"value": 66341<br>},<br>{<br>"name": "Samsung",<br>"value": 59890<br>},<br>{<br>"name": "Toyota",<br>"value": 53404<br>},<br>{<br>"name": "Mercedes-Benz",<br>"value": 48601<br>}<br>]<br>```

### 环图

环图用于表示整体中各部分的相对比例。适用于展示数据的百分比分布，强调整体的结构。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "pie",<br>"title": {<br>"text": "环图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"valueField": "value",<br>"categoryField": "type",<br>"outerRadius": 0.9,<br>"innerRadius": 0.3,<br>"label": {<br>"visible": true<br>},<br>"legends": {<br>"visible": true<br>}<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>} | ```json<br>[<br>{ "type": "oxygen", "value": "46.60" },<br>{ "type": "silicon", "value": "27.72" },<br>{ "type": "aluminum", "value": "8.13" },<br>{ "type": "iron", "value": "5" },<br>{ "type": "calcium", "value": "3.63" },<br>{ "type": "potassium", "value": "2.59" },<br>{ "type": "others", "value": "3.5" }<br>]<br>```

### 饼图

饼图可用于表示整体中各部分的相对比例，但通常适用于展示几个部分的数据。适用于呈现百分比或份额。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"aspect_ratio": "4:3",<br>"chart_spec": {<br>"type": "pie",<br>"title": {<br>"text": "客户规划占比"<br>},<br>"data": {<br>"values":  mock_data // 此处传入数据。<br>},<br>"valueField": "value",<br>"categoryField": "type",<br>"outerRadius": 0.9,<br>"legends": {<br>"visible": true,<br>"orient": "right"<br>},<br>"padding": {<br>"left": 10,<br>"top": 10,<br>"bottom": 5,<br>"right": 0<br>},<br>"label": {<br>"visible": true<br>}<br>}<br>}<br>]<br>}<br>} | ```json<br>[<br>{<br>"type": "S1",<br>"value": "340"<br>},<br>{<br>"type": "S2",<br>"value": "170"<br>},<br>{<br>"type": "S3",<br>"value": "150"<br>},<br>{<br>"type": "S4",<br>"value": "120"<br>},<br>{<br>"type": "S5",<br>"value": "100"<br>}<br>]<br>```

### 组合图

组合图可将多个图表类型组合在一起，同时呈现不同性质的数据。例如，折线图与柱状图的组合，可同时展示趋势和总量。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "common",<br>"title": {<br>"text": "组合图"<br>},<br>"data": [<br>{<br>"values": mock_data_1_1 // 此处传入数据。<br>},<br>{<br>"values": mock_data_1_2 // 此处传入数据。<br>}<br>],<br>"series": [<br>{<br>"type": "bar",<br>"dataIndex": 0,<br>"label": {<br>"visible": true<br>},<br>"seriesField": "type",<br>"xField": [<br>"x",<br>"type"<br>],<br>"yField": "y"<br>},<br>{<br>"type": "line",<br>"dataIndex": 1,<br>"label": {<br>"visible": true<br>},<br>"seriesField": "type",<br>"xField": "x",<br>"yField": "y"<br>}<br>],<br>"axes": [<br>{<br>"orient": "bottom"<br>},<br>{<br>"orient": "left"<br>}<br>],<br>"legends": {<br>"visible": true,<br>"orient": "bottom"<br>}<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>} | ```json<br>// mock_data_1_1<br>[<br>{ "x": "周一", "type": "早餐", "y": 15 },<br>{ "x": "周一", "type": "午餐", "y": 25 },<br>{ "x": "周二", "type": "早餐", "y": 12 },<br>{ "x": "周二", "type": "午餐", "y": 30 },<br>{ "x": "周三", "type": "早餐", "y": 15 },<br>{ "x": "周三", "type": "午餐", "y": 24 },<br>{ "x": "周四", "type": "早餐", "y": 10 },<br>{ "x": "周四", "type": "午餐", "y": 25 },<br>{ "x": "周五", "type": "早餐", "y": 13 },<br>{ "x": "周五", "type": "午餐", "y": 20 },<br>{ "x": "周六", "type": "早餐", "y": 10 },<br>{ "x": "周六", "type": "午餐", "y": 22 },<br>{ "x": "周日", "type": "早餐", "y": 12 },<br>{ "x": "周日", "type": "午餐", "y": 19 }<br>]<br>```<br>```json<br>// mock_data_1_2<br>[<br>{ "x": "周一", "type": "饮料", "y": 22 },<br>{ "x": "周二", "type": "饮料", "y": 43 },<br>{ "x": "周三", "type": "饮料", "y": 33 },<br>{ "x": "周四", "type": "饮料", "y": 22 },<br>{ "x": "周五", "type": "饮料", "y": 10 },<br>{ "x": "周六", "type": "饮料", "y": 30 },<br>{ "x": "周日", "type": "饮料", "y": 50 }<br>]<br>```

### 漏斗图

漏斗图用于表示一系列步骤或阶段中的数据减少。适用于呈现转化率、展示销售漏斗等情况。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "funnel",<br>"title": {<br>"text": "漏斗图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"categoryField": "name",<br>"valueField": "value",<br>"isTransform": true,<br>"label": {<br>"visible": true<br>},<br>"transformLabel": {<br>"visible": true<br>},<br>"outerLabel": {<br>"visible": false<br>}<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>} | ```json<br>[<br>{<br>"value": 5676,<br>"name": "Sent"<br>},<br>{<br>"value": 3872,<br>"name": "Viewed"<br>},<br>{<br>"value": 1668,<br>"name": "Clicked"<br>},<br>{<br>"value": 565,<br>"name": "Purchased"<br>}<br>]<br>```

### 雷达图

雷达图用于比较多个变量在不同维度上的表现，也可展示多个指标之间的相对关系。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "radar",<br>"title": {<br>"text": "雷达图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"categoryField": "key",<br>"valueField": "value",<br>"area": {<br>"visible": true<br>},<br>"outerRadius": 0.8,<br>"axes": [<br>{<br>"orient": "radius",<br>"label": {<br>"visible": true,<br>"style": {<br>"textAlign": "center"<br>}<br>}<br>}<br>]<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>}<br>``` | ```json<br>[<br>{<br>"key": "力量",<br>"value": 5<br>},<br>{<br>"key": "速度",<br>"value": 5<br>},<br>{<br>"key": "射程",<br>"value": 3<br>},<br>{<br>"key": "持续",<br>"value": 5<br>},<br>{<br>"key": "精密",<br>"value": 5<br>},<br>{<br>"key": "成长",<br>"value": 5<br>}<br>]<br>```

### 条形进度

条形进度用于表示某个或多个指标的进度，如任务完成度、目标达成情况等。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"aspect_ratio": "2:1",<br>"chart_spec": {<br>"type": "linearProgress",<br>"title": {<br>"text": "条形进度图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"direction": "horizontal",<br>"xField": "value",<br>"yField": "type",<br>"seriesField": "type",<br>"axes": [<br>{<br>"orient": "left",<br>"domainLine": {<br>"visible": false<br>}<br>}<br>]<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>}<br>``` | ```json<br>[<br>{<br>"type": "Tradition Industries",<br>"value": 0.795,<br>"text": "79.5%"<br>},<br>{<br>"type": "Business Companies",<br>"value": 0.25,<br>"text": "25%"<br>}<br>]<br>```

### 环形进度

环形进度类似于条形进度，但呈环状，可强调整体进度并突出部分的完成度。

JSON 模板 | 模拟数据
---|---
```json<br>{<br>"schema": "2.0",<br>"body": {<br>"elements": [<br>{<br>"tag": "chart",<br>"chart_spec": {<br>"type": "circularProgress",<br>"title": {<br>"text": "环形进度图"<br>},<br>"data": {<br>"values": mock_data // 此处传入数据。<br>},<br>"valueField": "value",<br>"categoryField": "type",<br>"seriesField": "type",<br>"radius": 0.7,<br>"innerRadius": 0.4,<br>"cornerRadius": 20,<br>"progress": {<br>"style": {<br>"innerPadding": 5,<br>"outerPadding": 5<br>}<br>},<br>"indicator": {<br>"visible": true,<br>"trigger": "hover",<br>"title": {<br>"visible": true,<br>"field": "type",<br>"autoLimit": true<br>},<br>"content": [<br>{<br>"visible": true,<br>"field": "text"<br>}<br>]<br>},<br>"legends": {<br>"visible": true,<br>"orient": "bottom",<br>"title": {<br>"visible": false<br>}<br>}<br>}<br>}<br>]<br>},<br>"header": {<br>"template": "purple",<br>"title": {<br>"content": "卡片标题",<br>"tag": "plain_text"<br>}<br>}<br>}<br>``` | ```json<br>[<br>{<br>"type": "Industries",<br>"value": 0.795,<br>"text": "79.5%"<br>},<br>{<br>"type": "Companies",<br>"value": 0.25,<br>"text": "25%"<br>}<br>]<br>```

# 表格组件

## 注意事项

- 单张卡片最多支持放置五个表格组件。若卡片配置了多语言，则单个语言最多支持放置五个表格组件。
- 当单元格内剩余空间无法完整展示内容时，末尾将省略。在客户端，用户可通过光标悬浮或点击的方式查看被省略的内容。

## 嵌套规则

- 表格组件不可被内嵌在其它组件内，只可放在卡片根节点下。
- 表格组件不支持内嵌其它组件。

## 组件属性

### JSON 结构

表格组件的完整 JSON 2.0 结构如下所示：

```json
{
  "schema": "2.0", // 卡片 JSON 结构的版本。默认为 1.0。要使用 JSON 2.0 结构，必须显示声明 2.0。
  "body": {
    "elements": [
      {
        "tag": "table", // 组件的标签。表格组件的固定取值为 table。
        "element_id": "custom_id", // 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用组件相关接口中指定组件。需开发者自定义。
        "margin": "0px 0px 0px 0px", // 组件的外边距。JSON 2.0 新增属性。默认值 "0"，支持范围 [-99,99]px。
        "page_size": 5, // 每页最大展示的数据行数。支持[1,10]整数。默认值 5。
        "row_height": "low", // 行高设置。默认值 low。
        "row_max_height": "50px", // 当 row_height 为 auto 时，可使用该参数设置最大行高。JSON 2.0 新增属性。取值范围为 [32,999]，单位为像素。
        "freeze_first_column": true, //是否冻结首列，默认 false。
        "header_style": {
          // 在此设置表头。
          "text_align": "left", // 文本对齐方式。默认值 left。
          "text_size": "normal", // 字号。默认值 normal。
          "background_style": "none", // 背景色。默认值 none。
          "text_color": "grey", // 文本颜色。默认值 default。
          "bold": true, // 是否加粗。默认值 true。
          "lines": 1 // 文本行数。默认值 1。
        },
        "columns": [ // 在此定义列。最多支持添加 50 列，超出 50 列的内容不展示。
          { // 添加列，列的数据类型为不带格式的普通文本。
            "name": "customer_name", // 列的 key（键名）。必填。用于在行数据对象数组中，指定数据填充的单元格。
            "display_name": "客户名称", // 列的展示名称。为空时不展示列名称。
            "width": "auto", // 列宽。默认值 auto。
            "data_type": "text", // 列的数据类型。
            "vertical_align": "top", // 列内数据垂直对齐方式。默认值 center。
            "horizontal_align": "left" // 列内数据水平对齐方式。默认数字类型的数据右对齐，其它文本左对齐。
          },
          { // 添加列，列的数据类型为 lark_md 文本。
            "name": "customer_link",
            "display_name": "相关链接",
            "data_type": "lark_md"
          },
          { // 添加类型为数字的列。
            "name": "customer_arr",
            "display_name": "ARR(万元)",
            "data_type": "number",
            "format": { // 列的数据类型为 number 时的字段配置。
              "symbol": "¥", // 数字前展示的货币单位。支持 1 个字符的货币单位文本。可选。
              "precision": 2, // 数字的小数点位数。支持 [0,10] 的整数。默认不限制小数点位数。
              "separator": true // 是否生效按千分位逗号分割的数字样式。默认值 false。
            },
            "width": "120px"
          },
          { // 添加类型为选项的列。
            "name": "customer_scale",
            "display_name": "客户规模",
            "data_type": "options"
          },
          { // 添加类型为人员的列。
            "name": "customer_poc",
            "display_name": "客户对接人",
            "data_type": "persons"
          },
          { // 添加类型为日期的列。
            "name": "meeting_date",
            "display_name": "对接时间",
            "data_type": "date",
            "date_format": "YYYY/MM/DD"
          },
          { // 添加类型为 markdown 文本的列。
            "name": "company_image",
            "display_name": "企业图片",
            "data_type": "markdown"
          }
        ],
        "rows": [ // 设置好列之后，在此添加与列定义对应的行数据。用 "name":VALUE 的形式，定义每一行的数据内容。name 即列的 key（键名）。
          {
            "customer_name": "飞书科技",
            "customer_date": 1699341315000,
            "customer_scale": [
              {
                "text": "S2",
                "color": "blue"
              }
            ],
            "customer_arr": 168,
            "customer_poc": [
              "ou_14a32f1a02e64944cf19207aa43abcef",
              "ou_e393cf9c22e6e617a4332210d2aabcef"
            ],
            "customer_link": "[飞书科技](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-reaction/emojis-introduce)"
          },
          {
            "customer_name": "飞书科技_01",
            "customer_date": 1606101072000,
            "customer_scale": [
              {
                "text": "S1",
                "color": "red"
              }
            ],
            "customer_arr": 168.23,
            "customer_poc": "ou_14a32f1a02e64944cf19207aa43abcef",
            "customer_link": "[飞书科技_01](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-reaction/emojis-introduce)",
            "company_image": "![image.png](image_key)"
          },
          {
            "customer_name": "飞书科技_02",
            "customer_date": 1606101072000,
            "customer_scale": [
              {
                "text": "S3",
                "color": "orange"
              }
            ],
            "customer_arr": 168.23,
            "customer_poc": "ou_14a32f1a02e64944cf19207aa43abcef",
            "customer_link": "[飞书科技_02](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-reaction/emojis-introduce)",
            "company_image": "![image.png](image_key)"
          },
          {
            "customer_name": "飞书科技_03",
            "customer_date": 1606101072000,
            "customer_scale": [
              {
                "text": "S2",
                "color": "blue"
              }
            ],
            "customer_arr": 168.23,
            "customer_poc": "ou_14a32f1a02e64944cf19207aa43abcef",
            "customer_link": "[飞书科技_03](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-reaction/emojis-introduce)",
            "company_image": "![image.png](image_key)"
          }
        ]
      }
    ]
  }
}
```

### 字段说明

表格组件的字段说明如下表。

字段 | 是否必填 | 类型 | 默认值 | 说明
---|---|---|---|---
tag | 是 | String | / | 组件的标签。表格组件的固定取值为 `table`。
element_id | 否 | String | 空 | 操作组件的唯一标识。JSON 2.0 新增属性。用于在调用[组件相关接口](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/cardkit-v1/card-element/create)中指定组件。在同一张卡片内，该字段的值全局唯一。仅允许使用字母、数字和下划线，必须以字母开头，不得超过 20 字符。
margin | 否 | String | 0 | 组件的外边距。JSON 2.0 新增属性。值的取值范围为 [-99,99]px。可选值：<br>- 单值，如 "10px"，表示组件的四个外边距都为 10 px。<br>- 双值，如 "4px 0"，表示组件的上下外边距为 4 px，左右外边距为 0 px。使用空格间隔（边距为 0 时可不加单位）。<br>- 多值，如 "4px 0 4px 0"，表示组件的上、右、下、左的外边距分别为 4px，12px，4px，12px。使用空格间隔。
page_size | 否 | Number | 5 | 每页最大展示的数据行数。支持 [1,10] 整数。
row_height | 否 | String | low | 表格的行高。单元格高度如无法展示一整行内容，则上下裁剪内容。可取值：<br>-   low：低<br>- middle：中<br>- high：高<br>- auto：行高与自适应内容。JSON 2.0 新增枚举，V7.33 及以上客户端版本支持。<br>- [32,124]px：自定义行高，单位为像素，如 40px。取值范围是 [32,124]
row_max_height | 否 | String | 124px | 当 row_height 为 auto 时，可使用该参数设置最大行高。若内容超过该值，将被裁剪。取值范围为 [32,999]，单位为像素。JSON 2.0 新增属性，V7.33 及以上客户端版本支持。
header_style | 否 | header_style | / | 表头样式风格。详见下方 `header_style` 字段说明。
freeze_first_column | 否 | Boolean | false | 是否冻结首列。可取值：<br>- true：冻结首列。即左右滚动表格时不滚动首列，其余列叠加展示在首列底下<br>- false：不冻结首列。即左右滚动表格时所有表格均做滚动
columns | 是 | column[] | [] | 列对象数组。详见下方 `column` 字段说明。
rows | 是 | JSON | [] | 行对象数组。与列定义对应的数据。用 `"name":VALUE` 的形式，定义每一行的数据内容。`name`即你自定义的列标记。
