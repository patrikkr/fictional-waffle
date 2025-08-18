def my_function(animal, feeling):
    print(f"The {animal} is {feeling}.")

my_function("lion", "tired")

def add(x, y):
    return x + y

three = add(1,2)

print("svar: ",three)


name = "Christoffer"

def setName(name):
    print(f"Hej {name}")

def add(x, y):
    my_sum = x + y
    return x + y

setName("Ada")
print(name)
my_sum = add(1,1)
print(my_sum)

total_sum = lambda x, y: x + y

print("")
print(f" totalsum är")