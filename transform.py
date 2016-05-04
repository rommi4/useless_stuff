#!/usr/bin/env python

import sys
import re


def read_lines(input_file):
    with open(input_file, 'rb') as IF:
        IF_lines = IF.readlines()
    return IF_lines


def get_numbers(raw_line):
    PhoneMatch = re.compile(r'\d*/TYPE=PLMN')
    try:
        FROM_RAW, TO_RAW = re.findall(PhoneMatch, raw_line)
    except:
        sys.exit()
    FROM_ = FROM_RAW[:-10]
    TO_ = TO_RAW[:-10]
    return (FROM_, TO_)


def get_picture(input_lines):
    lines_to_process = input_lines
    while lines_to_process:
        JFIF_Position = lines_to_process[0].find('JFIF')
        if JFIF_Position < 0:
            lines_to_process.pop(0)
        else:
            lines_to_process[0] = lines_to_process[0][JFIF_Position - 6:]
            break
    else:
        sys.exit()

    return lines_to_process


def dump_picture(from_msisdn, to_msisdn, randN, picture_lines):
    OutFileName = "from%sto%s_%s.jpg" % (from_msisdn, to_msisdn, randN)
    with open(OutFileName, 'wb') as OutFile:
        OutFile.writelines(picture_lines)


def main():
    InFile = sys.argv[1]
    randN = InFile.split('.')[0]
    Lines = read_lines(InFile)
    FROM, TO = get_numbers(Lines[0])
    Picture = get_picture(Lines)
    dump_picture(FROM, TO, randN, Picture)

if __name__ == '__main__':
    main()
