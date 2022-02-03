s = input("Enter a string to be alphabetically sorted, separated by hyphens:  ")

def Alphabetically_Sorter(s):
    words = s.split("-")
    words.sort()

    print("The sorted words are:")
    for word in words:
        print(word)
Alphabetically_Sorter(s)