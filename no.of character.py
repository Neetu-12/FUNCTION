def function(character):
    a=list(character)
    i=0
    c1=0
    C2=0
    while i<len(a):
        if a[i] >='A' and a[i]<='Z':
            c1=c1+1
        elif a[i] >='a' and a[i]<='z':
            C2=C2+1
        i=i+1
    print(c1,'upper case')
    print(C2,'lower case')
character='The quick Brown Fox'
function(character)