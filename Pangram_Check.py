def ispangram(s):

   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for letter in alphabet:
      if letter not in s.lower():
         return False
   return True

ispangram("wqeqw")

if (ispangram == True):
   print("Yes")
else:
   print("No")
