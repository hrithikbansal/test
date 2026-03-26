import os
import sys


def main():
    n= int(input("Enter pyramid dimension: "))
    for i in range(0,n):
        for j in range(0,n):
            if (i+j)<(n-1):
                print(" ",end="")
            else:
                print("#", end="")
        print()
        






if __name__ == "__main__":
    main()
