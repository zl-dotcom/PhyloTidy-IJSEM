# PhyloTidy-IJSEM

[English Version](#english-version) | [简体中文 (默认)](#简体中文-chinese-version)

---

## 简体中文 (Chinese Version)

**一个轻量级的拖拽式小工具，自动为系统发育树 SVG 文件进行符合 IJSEM 期刊发表标准的标签排版。**

### 🌟 简介
在向 *International Journal of Systematic and Evolutionary Microbiology (IJSEM)* 等国际期刊提交新物种描述时，系统发育树（Phylogenetic tree）必须遵守严格的格式规则：
1. **物种名必须斜体。**
2. **模式菌株必须带有右上角标 'T'。**
3. **GenBank/EMBL 序列号需要用小括号括起来。**

在 Adobe Illustrator 或 Inkscape 中手动逐一修改 SVG 文本既枯燥又耗时。**PhyloTidy-IJSEM** 利用正则表达式自动解析并重排 SVG 的底层文本标签，为你一键解决排版难题。

### ✨ 功能特点
- **零配置体验：** 无需安装任何环境，直接将 SVG 文件拖拽到 `.exe` 图标上即可运行。
- **批量处理：** 支持同时拖入多个 SVG 文件进行一键批量排版。
- **非破坏性修改：** 自动在原目录生成带有 `_Publication_Ready.svg` 后缀的新文件，绝对安全，不覆盖原图。
- **高准确度：** 专门针对从 LPSN (List of Prokaryotic names with Standing in Nomenclature) 数据库下载的 16S 序列标签格式进行了深度优化。

### 🚀 使用方法

#### 👉 Windows 用户 (开箱即用)
1. 前往本仓库的 [Releases](#) 页面，下载最新的 `PhyloTidy-IJSEM.exe`。
2. 找到你从建树软件（如 MEGA, iTOL 等）导出的原始 SVG 文件。
3. **按住鼠标左键，将 `.svg` 文件直接拖拽到 `PhyloTidy-IJSEM.exe` 图标上并松开。**
4. 黑色控制台窗口会短暂弹出并显示处理进度。完成后，同一文件夹下会自动生成排版好的新文件。

#### 👉 开发者 (源码运行)
请确保已安装 Python 3.x。本脚本仅使用 Python 内置库（`re`, `os`, `sys`），无需额外安装任何第三方依赖。
```bash
# 克隆仓库
git clone [https://github.com/zl-dotcom/PhyloTidy-IJSEM.git](https://github.com/zl-dotcom/PhyloTidy-IJSEM.git)

# 命令行运行 (支持传入多个文件)
python format_svg.py your_tree_file.svg
