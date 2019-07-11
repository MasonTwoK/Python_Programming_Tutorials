from operator import itemgetter

dictionary = [
    {'fname' : 'Lebron', 'lname' : 'James'},
    {'fname' : 'Kobe', 'lname' : 'Braynt'},
    {'fname' : 'Dwayne', 'lname' : 'Wade'},
    {'fname' : 'Shaquille', 'lname' : 'O \'Neal'},
    {'fname' : 'Vince', 'lname' : 'Carter'},
    {'fname' : 'James', 'lname' : 'Harden'},
    {'fname' : 'James', 'lname' : 'Jones'}
]

dsorted = []
a=0

for x in sorted(dictionary,key=itemgetter('fname','lname')):
    print(x)
