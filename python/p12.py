def c1():
# Generates a list of squares of the numbers 1 - 10
   my_list = [i**2 for i in range(1,11)]

   f = open("output.txt", "w")

   for item in my_list:
      f.write(str(item) + "\n")

   f.close()

def c4():
   my_file = open("output.txt","r")
   print my_file.read()
   my_file.close()

def c1b():
   my_file = open("text.txt","r")
   print my_file.readline()
   print my_file.readline()
   print my_file.readline()
   my_file.close()

def c2b():
# Open the file for reading
   read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
   write_file = open("text.txt", "w")
# Write to the file
   write_file.write("Not closing files is VERY BAD.")

   write_file.close()

# Try to read from the file
   print read_file.read()
   read_file.close()

'''
You may not know this, but file objects contain a special pair
of built-in methods: __enter__() and __exit__().
The details are not important, but what is important is that when
the __exit__() method is invoked,
it automatically closes the file.
How do we invoke this method? With with and as.
'''
def c3b():

   with open("text.txt", "w") as textfile:
       textfile.write("Success!")

   with open("text.txt", "r+") as my_file:
       my_file.write("This is a test.")

def c5b():
   with open("text.txt", "r+") as my_file:
       my_file.write("This is a test.")

   if (not my_file.closed):
      my_file.close()
   print my_file.closed

def c6():
    with open("text.txt", "r+") as my_file:
       print my_file.read()


