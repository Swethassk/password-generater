import random #To choose things randomly
import string #To get all the characters

characters=string.ascii_letters+string.digits+string.punctuation+string.ascii_uppercase+string.ascii_lowercase
N=int(input("Enter the password length:"))
if N==0:
      print("Invalid length")
else:
    password="".join(random.choice(characters) for i in range(N))
    print(password)
