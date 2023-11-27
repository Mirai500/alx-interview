#!/usr/bin/python3
"""
This script prints the metric stats at interval
"""


def print_metric(dic, total_size):
    """
    Print function
    """
    d = sorted(dic.keys())
    print("File size: {:d}".format(total_size))
    for i in d:
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))

c = 0
total_size = 0
dic = {"200": 0, "301": 0, "400": 0, "401": 0,
       "403": 0, "404": 0, "405": 0, "500": 0}

try:
    with open(0) as file:
        for line in file:
            c += 1
            arr = line.split()
            try:
                total_size += int(arr[-1])
            except:
                pass
            try:
                status = arr[-2]
                if status in dic:
                    dic[status] += 1
            except:
                pass
            if c % 10 == 0:
                print_metric(dic, total_size)
        print_metric(dic, total_size)

except KeyboardInterrupt:
    print_metric(dic, total_size)
    raise