# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:   Kam se kam uski length 6 honi chaiye
# Jada se jada length 16 se jyada na ho
# Kam se kam ek dollar ka sign ($) hona chaiye
# Kam se kam password mein 2 ya 8 hona chaiye
# Password mein capital A ya capital Z hona chaiye
# Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, nahi toh "Weak Password" type karo
# Edit
passward=input('enetr your passward of 6-16 digit')
if len(passward)>=6 and len(passward)<=16:
     if '$' in passward:
         if '2' in passward or '8' in passward:
             if 'A' in passward or 'Z' in passward:
               print('strong password')
             else:
                print('weak password')
         else:
                 print('weak password')
     else:
                print('weak password')
else:
                print('weak password')