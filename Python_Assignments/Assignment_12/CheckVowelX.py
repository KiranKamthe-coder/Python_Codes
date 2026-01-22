# Write a progrme to accept on character and check whether it is vowel or consonant input a op vowel

def main():
    print("Enter one character : ")

    ch = input()

    if ch.lower() in ('a','e','i','o','u'):
        print("Character is vowel : ",ch)
    else:
        print("Character in consonant : ",ch)


if(__name__ == "__main__"):
    main()