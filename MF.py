#!/usr/bin/env python3
# Author: Lev Tsarin

import vcf
import pandas as pd
import argparse

parser = argparse.ArgumentParser(
        prog="GC_VCF_PARSER",
        usage="%(prog)s[options]",
        description="Made to make vcf files analysis easier.Script filters GC>CG mutations by region"
    )
parser.add_argument("--config", "-c", metavar="", type=str, help = "path to config file(with extension); table with regions of interest")
parser.add_argument("--vcf", "-v", metavar="", type=str, help = "path to vcf file to analyse(with extension)")

args = parser.parse_args()




df = pd.read_excel(args.config)
vcf_reader = vcf.Reader(open(args.vcf), "r")
for record  in vcf_reader:
    if (record.REF == "C" or record.REF == "G") and ("C" in record.ALT or "G" in record.ALT):
        for index,probe in df.iterrows():
            chromosome, coordinates = probe["Coordinates"].split(":")
            start,end = coordinates.split("-")
            if record.POS in range(int(start),(int(end))):
                print(f"probe #{index+1} {record.CHROM}:{record.POS}  {record.REF} > {record.ALT}")






