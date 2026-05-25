# PhyloTidy-IJSEM

[English Version](#english-version) | [简体中文](#简体中文-chinese-version)

---

## 简体中文 (Chinese Version)

**一个轻量级的拖拽式小工具，自动为系统发育树 SVG 文件进行符合 IJSEM 期刊发表标准的标签排版。**

### 🌟 简介
在向 *International Journal of Systematic and Evolutionary Microbiology (IJSEM)* 等国际期刊提交新物种描述时，系统发育树（Phylogenetic tree）必须遵守严格的格式规则：
1. **物种名必须斜体。**
2. **模式菌株必须带有右上角标 'T'。**
3. **GenBank/EMBL 序列号需要用小括号括起来。**

在 Adobe Illustrator 或 Inkscape 中手动逐一修改 SVG 文本既枯燥又耗时。**PhyloTidy-IJSEM** 利用正则表达式自动解析并重排 SVG 的底层文本标签，为你一键解决排版难题。

### 📸 效果展示

| 修改前 (原始导出) | 修改后 (IJSEM 标准) |
| :---: | :---: |
| ![修改前](picture/修改前.png) | ![修改后](picture/修改后.png) |
| *所有字体均为正体，格式杂乱* | *物种名自动斜体，生成上标 T，序列号带括号* |

### ✨ 功能特点
- **零配置体验：** 无需安装任何环境，直接将 SVG 文件拖拽到 `.exe` 图标上即可运行。
- **批量处理：** 支持同时拖入多个 SVG 文件进行一键批量排版。
- **非破坏性修改：** 自动在原目录生成带有 `_Publication_Ready.svg` 后缀的新文件，绝对安全，不覆盖原图。
- **高准确度：** 专门针对从 LPSN 数据库下载的 16S 序列标签格式进行了深度优化。

### 🚀 使用方法

#### 👉 Windows 用户 (开箱即用)
1. 前往本仓库的 Releases 页面，下载最新的 `PhyloTidy-IJSEM.exe`。
2. 找到你从建树软件（如 MEGA, iTOL 等）导出的原始 SVG 文件。
3. **按住鼠标左键，将 `.svg` 文件直接拖拽到 `PhyloTidy-IJSEM.exe` 图标上并松开。**
4. 黑色控制台窗口会短暂弹出并显示处理进度。完成后，同一文件夹下会自动生成排版好的新文件。

#### 👉 开发者 (源码运行)
请确保已安装 Python 3.x。本脚本仅使用 Python 内置库。

```bash
# 克隆仓库
git clone [https://github.com/zl-dotcom/PhyloTidy-IJSEM.git](https://github.com/zl-dotcom/PhyloTidy-IJSEM.git)

# 命令行运行 (支持传入多个文件)
python format_svg.py your_tree_file.svg

🛠️ 原理解析

本工具直接读取 SVG 的底层 XML 结构，寻找标准的 16S 序列 FASTA 表头模式。

转换前: > Bacillus subtilis subsp. subtilis 168 AL009126

转换后: Bacillus subtilis subsp. subtilis 168T (AL009126)

⚠️ 输入文件要求

序列名称尽量遵循以下结构：[属名] [种名] [菌株名] [序列号]。

📄 开源协议

本项目基于 MIT License 开源 - 详情请查看 LICENSE 文件。

English Version

返回中文 (Back to Chinese)

A lightweight, drag-and-drop tool to automatically format phylogenetic tree SVG files for IJSEM publication standards.

🌟 Introduction

When submitting novel species descriptions to journals like the International Journal of Systematic and Evolutionary Microbiology (IJSEM), phylogenetic trees must adhere to strict formatting rules (Species names italicized, Type strains with superscript 'T', Accession numbers in parentheses). PhyloTidy-IJSEM solves this problem by using Regular Expressions to parse and reformat SVG text tags automatically in seconds.

📸 Screenshots

BeforeAfterRaw SVG export with standard formattingFormatted ready for IJSEM submission

✨ Features

Zero Configuration: Just drag and drop your SVG file(s) onto the .exe icon. No coding required.

Batch Processing: Support processing multiple SVG files simultaneously.

Non-destructive: Generates a new file with the _Publication_Ready.svg suffix, keeping your original file perfectly safe.

Highly Accurate: Optimized specifically for standard 16S sequence headers downloaded directly from the LPSN database.

🚀 How to Use

👉 For Windows Users (No installation required)

Go to the Releases page and download the latest PhyloTidy-IJSEM.exe.

Locate the phylogenetic tree SVG file exported from your software.

Drag and drop the .svg file directly onto the PhyloTidy-IJSEM.exe icon.

A formatted file will appear in the same folder.

👉 For Developers (Run from source)

Ensure you have Python 3.x installed. No external libraries required.

Bash



# Clone the repository

git clone [https://github.com/zl-dotcom/PhyloTidy-IJSEM.git](https://github.com/zl-dotcom/PhyloTidy-IJSEM.git)# Run the script

python format_svg.py your_tree_file.svg

🛠️ How it Works

Input text in SVG: > Bacillus subtilis subsp. subtilis 168 AL009126

Output visually rendered as: Bacillus subtilis subsp. subtilis 168T (AL009126)

⚠️ Requirements & License

Your tree tip labels should generally follow: [Genus] [species] [strain name] [Accession Number].

This project is licensed under the MIT License - see the LICENSE file for details.

