def loop1():
   print "Counting..."

   for i in range(20):
      print i

def loop2():
   numbers  = [7, 9, 12, 54, 99]

   print "This list contains: "

   for num in numbers:
      print num

   for num in numbers:
      print num**2

def loop3():
   hobbies = []

   for i in range(3):
     hobby = raw_input("Enter hobby:")
     hobbies.append(hobby)

def loop4():
   from random import randrange

   random_number = randrange(1, 10)

   count = 0

   while (count < 3):
      count +=1
      guess = int(raw_input("Enter a guess:"))
      if guess == random_number:
         print "You Win!!!"
         break
      else:
         print "Sorry, Not Right!  Try again."
   else:
      print "You Lose"
