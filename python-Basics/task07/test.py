#fileName
def putInfoToDict():
    with open('file1.txt','r') as f:
        print(f.read())
        print(type(f.read()))

putInfoToDict()