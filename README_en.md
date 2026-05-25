================================================================================
                                PhyloTidy-IJSEM
================================================================================

[English Version] (Scroll down for English)
[简体中文]

--------------------------------------------------------------------------------
                                   简体中文
--------------------------------------------------------------------------------

一个轻量级的拖拽式小工具，自动为系统发育树 SVG 文件进行符合 IJSEM 期刊发表标准的标签排版。

* 简介 *
在向 International Journal of Systematic and Evolutionary Microbiology (IJSEM) 等国际期刊提交新物种描述时，系统发育树（Phylogenetic tree）必须遵守严格的格式规则：
1. 物种名必须斜体。
2. 模式菌株必须带有右上角标 'T'。
3. GenBank/EMBL 序列号需要用小括号括起来。

在 Adobe Illustrator 或 Inkscape 中手动逐一修改 SVG 文本既枯燥又耗时。PhyloTidy-IJSEM 利用正则表达式自动解析并重排 SVG 的底层文本标签，为你一键解决排版难题。

* 功能特点 *
- 零配置体验：无需安装任何环境，直接将 SVG 文件拖拽到 .exe 图标上即可运行。
- 批量处理：支持同时拖入多个 SVG 文件进行一键批量排版。
- 非破坏性修改：自动在原目录生成带有 _Publication_Ready.svg 后缀的新文件，绝对安全，不覆盖原图。
- 高准确度：专门针对从 LPSN 数据库下载的 16S 序列标签格式进行了深度优化。

* 使用方法 *

-> Windows 用户 (开箱即用)
1. 前往本仓库的 Releases 页面，下载最新的 PhyloTidy-IJSEM.exe。
2. 找到你从建树软件（如 MEGA, iTOL 等）导出的原始 SVG 文件。
3. 按住鼠标左键，将 .svg 文件直接拖拽到 PhyloTidy-IJSEM.exe 图标上并松开。
4. 黑色控制台窗口会短暂弹出并显示处理进度。完成后，同一文件夹下会自动生成排版好的新文件。

-> 开发者 (源码运行)
请确保已安装 Python 3.x。本脚本仅使用 Python 内置库，无需安装其他依赖。
运行命令：
git clone https://github.com/zl-dotcom/PhyloTidy-IJSEM.git
python format_svg.py your_tree_file.svg

* 原理解析 *
本工具直接读取 SVG 的底层 XML 结构，寻找标准的 16S 序列 FASTA 表头模式。
转换前: > Bacillus subtilis subsp. subtilis 168 AL009126
转换后: Bacillus subtilis subsp. subtilis 168T (AL009126) (SVG 将自动渲染斜体和上标)

* 输入文件要求 *
序列名称尽量遵循以下结构：[属名] [种名] [菌株名] [序列号]。

* 开源协议 *
本项目基于 MIT License 开源 - 详情请查看 LICENSE 文件。


--------------------------------------------------------------------------------
                                English Version
--------------------------------------------------------------------------------

A lightweight, drag-and-drop tool to automatically format phylogenetic tree SVG files to meet the publication standards of IJSEM.

* Introduction *
When submitting novel species descriptions to international journals like the International Journal of Systematic and Evolutionary Microbiology (IJSEM), phylogenetic trees must adhere to strict formatting rules:
1. Species names must be italicized.
2. Type strains must feature a superscript 'T'.
3. GenBank/EMBL accession numbers must be enclosed in parentheses.

Manually modifying SVG text tags one by one in Adobe Illustrator or Inkscape is both tedious and time-consuming. PhyloTidy-IJSEM uses regular expressions to automatically parse and reformat the underlying text tags of your SVG files, solving your formatting challenges in a single click.

* Features *
- Zero Configuration: No environment setup required. Simply drag and drop the SVG file onto the .exe icon to run.
- Batch Processing: Supports dragging multiple SVG files simultaneously for one-click batch formatting.
- Non-Destructive: Automatically generates a new file with a "_Publication_Ready.svg" suffix in the same directory. Your original file remains perfectly safe.
- High Accuracy: Deeply optimized for the standard 16S sequence label formats downloaded from the LPSN database.

* How to Use *

-> For Windows Users (Out of the box)
1. Go to the Releases page of this repository and download the latest PhyloTidy-IJSEM.exe.
2. Locate the raw SVG file exported from your phylogenetic tree software (e.g., MEGA, iTOL).
3. Left-click and drag the .svg file directly onto the PhyloTidy-IJSEM.exe icon, then release.
4. A black console window will briefly appear to show processing progress. Once complete, a newly formatted file will be generated in the same folder.

-> For Developers (Run from source)
Please ensure Python 3.x is installed. This script uses only Python built-in libraries; no additional dependencies are needed.
Commands:
git clone https://github.com/zl-dotcom/PhyloTidy-IJSEM.git
python format_svg.py your_tree_file.svg

* How it Works *
This tool directly reads the underlying XML structure of the SVG and searches for standard 16S sequence FASTA header patterns.
Before conversion: > Bacillus subtilis subsp. subtilis 168 AL009126
After conversion: Bacillus subtilis subsp. subtilis 168T (AL009126)

* Input Requirements *
Tip labels should ideally follow this structure: [Genus] [species] [strain name] [Accession Number].

* License *
This project is open-sourced under the MIT License - see the LICENSE file for details.
