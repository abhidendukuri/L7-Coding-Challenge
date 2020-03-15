import csv
import pandas as pd
import re


def findTargetValues(textFile):
    leadDigits = dict()
    count = 0
    fin = open(textFile, "r")
    
    for line in fin:
        # Find the numbers in each line 
        # since the findall returns a list, we'll pop the element to extract a string
        n = re.findall(r'\d+', line).pop()
        
        # equation to find the lead digit of each value
        lead = int(n) // 10 ** (len(n) - 1)

        # add each lead digit to dictionary
        if lead in leadDigits:
            leadDigits[lead] += 1
        else:
            leadDigits[lead] = 1

        # get the total values count
        count += 1

    fin.close()    
    
    return leadDigits, count


def main():
    txt = r'census_2009.txt'
    
    leads, numCount = findTargetValues(txt)

    print(leads)
    print(numCount)


if __name__ == "__main__":
    main()
    



# i // 10 ** (len(str(i)) - 1) = leading integer
# add leading integer to count dictionary
