def read_in():
    x = raw_input('?')
    print x
    return x

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

filename = "D:\\Documents\\GitHub" + \
           "\\CSci226.Fall13\\python\\tutorial" + \
           "\\output.txt"

f = open(filename, "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()
