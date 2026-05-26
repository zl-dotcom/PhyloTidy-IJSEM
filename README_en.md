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

* Input Requirements *
Tip labels should ideally follow this structure: [Genus] [species] [strain name] [Accession Number].

* License *
This project is open-sourced under the MIT License - see the LICENSE file for details.
