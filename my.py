import sys
from gui import  Application
import  logging

def combindList(l1 : list, l2 : list, connector : str):
    if len(l1) != len(l2):
        return None
    ret = []
    for i, value in enumerate(l1):
        ret.append(value + connector + l2[i])
    return ret

def main():
    a = ["1", "2"]
    b = ["3" ,"4"]
    c = combindList(a, b, '-')
    print(c)

if __name__ == "__main__":
    main()