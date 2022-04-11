import glob
import os

import wosfile
from collections import Counter
import Paper

input_file = "data/download.txt"
out_file = "result/Papers.xlsx"

if __name__ == '__main__':
    filedir = os.getcwd() + '/raw_data'
    filenames = os.listdir(filedir)

    for filename in filenames:
        filepath = filedir + '/' + filename
        paper_list = Paper.read_paper(filepath)
        Paper.write_excel_file(out_file, paper_list)
