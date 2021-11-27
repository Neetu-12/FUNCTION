def bmi(weight,height):
    bmi = (weight / height)
    if bmi <= 18.5:
        print(bmi,"Underweight")
    elif bmi <= 25.0:
        print(bmi,"Normal")
    elif bmi <= 30.0:
        print (bmi,"Overweight")

    elif bmi > 30 :
        print(bmi,"Obese")
weight=int(input('please enter your weight in kg'))
height=int(input('please enter your height in cm'))
bmi(weight,height)   