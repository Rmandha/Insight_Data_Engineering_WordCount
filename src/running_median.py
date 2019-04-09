import glob
import os
import csv
import re
import statistics

word_count = []
curr_median = []

#myfiledir = os.getcwd()

myfiledir = '/Users/ravikiranmandha/Wc_input/'

inputfiles = sorted(glob.glob(os.path.join(myfiledir, '*.txt')))

for inputfile in inputfiles:
    with open (inputfile, 'r') as f:
        for line in f:
            line_count = len(line.split())
            word_count.append(line_count)
            running_median=statistics.median(word_count)
            curr_median.append(running_median)  

        try:
            os.makedirs("/Users/ravikiranmandha/Wc_Output/")
        except FileExistsError:
    # directory already exists
            pass
   
    with open("/Users/ravikiranmandha/Wc_Output/med_result.txt", "a") as f: 
            for row in curr_median:
                print(row, file=f)
