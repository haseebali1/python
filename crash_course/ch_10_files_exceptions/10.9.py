# Silent Cats and dogs

def print_file(filename):
    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        print("Printing from " + filename)
        for line in lines:
            print ( "\t" + line.rstrip() )


print_file('files/cats.txt')
print_file('files/dogs.txt')
