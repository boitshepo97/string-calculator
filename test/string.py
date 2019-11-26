import re 
from typing import List

def add(num, str):
"""
Add numbers passed, some can be in the form of a delimeter string
"""

if num == "":
        return 0
        numlis= parse_into_list(num)
    result = 0

    negs = []
    for num in numlis:
        try:
            num = int(num)
        except ValueError:
            raise ValueError("Input could not be converted to int")
        if num < 0:
            negs.append(num)
        else:
            if num <= 1000:
                result += num
    if negs:
        raise ValueError("Negatives not allowed: {0}".format(",".join(map(str, negatives))))
    return result