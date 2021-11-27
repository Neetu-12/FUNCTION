def string(ch1,ch2):
    if len(ch1)==len(ch2):
        print(ch1)
        print(ch2)
    elif len(ch1)>len(ch2):
        print(ch1)
    else:
        print(ch2)
ch1=input('enter your character')
ch2=input('enter your character')
string(ch1,ch2)