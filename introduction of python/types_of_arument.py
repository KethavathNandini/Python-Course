# defalut parameter
def add(a, b=8):
    addition = a + b
    return addition


print(add(10, 9))
print(add(10))


# positional argument
def greeting(name, age):
    print(f"your age is {age} and your name is {name}")


greeting("john", 20)


# keyword argument
def number(a, b=10, c=12):
    return a + b + c


print(number(10, c=11))


# variable length argument - when n number of arguments to be taken
# *args - variable length positional argument (0 to n)
def add(*args):
    return sum(args)


result = add(1, 3, 6)
print(result)


# **kwargs - variable length keyword arguments
# stored in the form of dictionary and they must be last in the definition(should not before the argument )
def func(**kwargs):
    print(kwargs)


func(a=0, b=8)


def student_details(sid, sname, **marks):
    if len(marks) == 0:
        print(f"{sname} did not attend the exams")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} got {percent}")


student_details(108, "mikasa", math=90, phy=60, tel=98, chem=78)

