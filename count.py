def countwordsInFile():
    fileName=input("enter the file name: ")
    file=open(fileName,"r")
    count=0
    for line in file:
        words=line.split()
        print(words)
        count=count+len(words)
    print("the number of words are:")
    print(count)


countwordsInFile()

