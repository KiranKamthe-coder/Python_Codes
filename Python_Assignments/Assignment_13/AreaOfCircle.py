# Write a progrme to accept the radius of cirle print the area

from math import pi

def main():
    print("Enter the radius : ")
    Lenght = float(input())

    Area = pi * Lenght *Lenght

    print("Area of cirle is : ", Area)


if(__name__ == "__main__"):
    main()