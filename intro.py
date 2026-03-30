# int 
# bool 
# float 
# str

var = 12
print(var + 11)

var = "Hello"
print(var)

# Conditions

if True:
    pass
elif False:
    pass
else:
    pass

a = "True" if 5 > 10 else "False"
print(a)

while True:
    print("While")
    break

# Exceptions

for i in range(3):
    print("Range")

try:
    raise Exception("Unnexcepted situation")
except Exception as e:
    print(e)
finally:
    print("Finalize")


# Functions

def sample():
    print("sample function")

sample()

print(sample()) # None

def sample_with_params(arg1:int|float, arg2:int)-> tuple | None:
    print("arg1: ", arg1, "arg2: ", arg2)
    return None

# sample_with_params(arg2="Hello", arg1=12)

sample_with_params(12, arg2="Hello")



