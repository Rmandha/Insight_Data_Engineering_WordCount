import glob
import os
import csv
import re

unique_list = []
word_dict = {}

#myfiledir = os.getcwd()

myfiledir = '/Users/ravikiranmandha/Wc_input/'

inputfiles = sorted(glob.glob(os.path.join(myfiledir, '*.txt')))

for inputfile in inputfiles:
    with open (inputfile, 'r') as f:
        #text = [word.lower() for line in f for word in line.split()]
        for line in f:
            for word in line.split():
                mod_word = re.sub(r"([—!#?,.:';]|[0-9]|[^\w\sp{P}])",'',word.lower())
                if mod_word not in unique_list:
                    unique_list.append(mod_word)
                    word_dict[mod_word] = 1
                else:
                    word_dict[mod_word] += 1

        try:
            os.makedirs("/Users/ravikiranmandha/Wc_Output/")
        except FileExistsError:
    # directory already exists
            pass

for key in sorted(word_dict.keys()):      
        with open("/Users/ravikiranmandha/Wc_Output/wc_result.txt", "a") as f: 
            print("%s        %s" % (key, word_dict[key]), file=f)


              

