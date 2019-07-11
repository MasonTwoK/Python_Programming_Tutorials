'''
file1 = open('file.txt' , 'w')
some_text = file1.write("BLo blo blo blo \n" )
some_text = file1.write("A lo ololo\n")
'''
def wil_reader(file):
    file1 = open(file,'r')
    a = file1.read()

    file1.close()
    return a


a1 = wil_reader("file.txt")
print(a1)


