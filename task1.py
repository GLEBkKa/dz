#date,time,location,operator
input_file = "data/plane.csv"
import re
def getElement(line):
    result = re.split(r'"', line,maxsplit=1)
    return result[1]


'''def getName(line):
    opname, line = getElement(line)
    opname = opname[0].upper()+opname[1:].lower()
    return opname, line'''
def getDate(line):
    result = re.split(r'"', line, maxsplit=1)
    date = re.findall(r'\w+ \d{2}\, \d{4}', result[1])
    return date, result[1]
try:
    with open(input_file,encoding="utf-8",mode='r') as file:
        file.readline()
        line_number = 1
        for line in file:
            line = line.strip().rstrip()
            line_number += 1
            if not line:
                continue
            date, line = getDate(line)
            #opname , line = getName(line)
            print(date)

except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))
