# Iss program mein hum students ki ginti aur ek student ke kharche se hisaab se pure NavGurukul ka ek mahine ka kharcha nikalenge input ka use kar ke do values ka input lo: * Number of students

# Ek student ka kharcha
# Iss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya usse kam hai toh print karein "Hum budget ke andar hain" nahi toh print karo ki hum budget ke bahar hain
number_of_student=int(input('enter the number of girls in campus'))
money_spent=int(input('enetr the money spent on one girl'))
budget=(number_of_student*money_spent)
if budget>=50000:
    print('under the budget')
else:
    print('out of budget')