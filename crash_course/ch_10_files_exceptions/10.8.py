# Cats and dogs

def print_file(filename):
    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print ("The file could not be found")
    else:
        print("Printing from " + filename)
        for line in lines:
            print ( "\t" + line.rstrip() )


print_file('files/cats.txt')
print_file('files/dogs.txt')
