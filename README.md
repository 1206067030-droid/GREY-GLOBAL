# GREY GLOBAL LIMITED - 高品质手机壳定制网站

## 网站概览

这是一个为 GREY GLOBAL LIMITED 设计的企业展示 + 产品销售型官网，专注于高品质苹果、华为、三星手机壳定制。

## 主要功能

1. **响应式设计** - 完美适配手机、平板、电脑等各种设备
2. **深色/浅色模式切换** - 默认跟随系统设置
3. **中英文语言切换** - 支持繁体中文和英文双语
4. **产品展示** - 按品牌筛选产品，支持排序功能
5. **产品详情页** - 展示详细的产品信息、特性和规格
6. **联系表单** - 方便客户咨询
7. **品牌展示** - 专业的企业介绍和信息展示

## 文件结构

```
格瑞環球/
├── index.html              # 首页
├── products.html           # 产品列表页
├── product-detail.html     # 产品详情页
├── generate-icons.html     # 图标生成工具
├── site.webmanifest        # PWA manifest配置
├── images/                 # 产品图片文件夹
│   ├── [产品图片1.jpg]
│   ├── [产品图片2.jpg]
│   └── ...
└── README.md               # 本文件
```

## 使用说明

### 1. 生成网站图标

1. 在浏览器中打开 `generate-icons.html`
2. 点击各个按钮下载所需的图标文件
3. 将下载的文件保存到网站根目录

需要的图标文件：
- `apple-touch-icon.png` (180x180)
- `favicon-32x32.png` (32x32)
- `favicon-16x16.png` (16x16)

### 2. 查看网站

直接在浏览器中打开 `index.html` 即可查看网站效果。

### 3. 页面导航

- **首页** - 英雄区、特性展示、精选产品、关于我们、联系表单
- **产品页** - 完整产品列表，支持品牌筛选和排序
- **产品详情页** - 从产品列表点击查看详情，支持URL参数指定产品ID

## 技术特点

- 使用 HTML5 + Tailwind CSS 构建
- 原生 JavaScript 实现交互功能
- 语义化 HTML 结构，代码清晰易维护
- 深色模式支持
- 本地存储用户偏好设置
- 响应式布局，适配各种屏幕

## 定制说明

### 修改公司信息

在各个 HTML 文件中搜索以下内容进行修改：
- 公司名称: "GREY GLOBAL LIMITED"
- 联系人: "林一心"
- 电话: "852 9047 2207"
- 邮箱: "RichardGonzalez1721@outlook.com"

### 添加新产品

在 `product-detail.html` 的 `productData` 对象中添加新产品信息，并确保在 `index.html` 和 `products.html` 中添加相应的产品卡片。

### 修改主题颜色

在各个 HTML 文件的 Tailwind 配置部分修改 `colors` 对象中的定义。

## 浏览器兼容性

- Chrome/Edge 最新版本
- Firefox 最新版本
- Safari 最新版本
- 移动端浏览器 (iOS Safari, Android Chrome)

## 部署说明

将所有文件上传到网站服务器即可。无需额外的后端服务支持，完全是静态网站。
