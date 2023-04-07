# MutFilter - tool to filter GC>CG mutations in vcf files

## Setup
Find a location where you want to locate the script and clone the script using git:

    git clone <link>

You should install *python* manually, other requirements will be installed with the following command:

    pip install -r requirements.txt

## Usage example

What is needed:

* Config.xlsx file

It has to contain column called "Coordinates", where you store regions of interest in the following format:

    chr1:4745001-4745460 
    chr2:7800608-78000027

* VCF file

Run following command in terminal to see acceptable arguments:

    ./MF.py -h

Run script:

    ./MF.py -c <path to config file> -v <path to vcf file>

As output you receive following prompt in terminal window:

    probe #101 chr1:55987858  G > [C]
    probe #4 chr1:84273289  C > [G]
    probe #57 chr10:78589270  G > [C]
    probe #21 chr4:4336281  C > [G]