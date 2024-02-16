#str.format() = optional method that gives users 
#               more control when displaying output

animal = "cow"
item = "moon"

print("the "+animal+" jumped over the "+item)
print("the {} jumped over the {}".format(animal,item))
print("the {1} jumped over the {0}".format(animal,item))   #position argument
print("the {animal} jumped over the {item}".format(animal="bimbim",item="bambam"))

text = "the {} jumped over the {}"
print(text.format(animal,item))

name="amine"
print("Hello, my name is {}".format(name))
print("hello, my name is {:<10}. nice to meet you".format(name))
print("hello, my name is {:>10}. nice to meet you".format(name))
print("hello, my name is {:^10}. nice to meet you".format(name))

number= 3.14159

print("the number pi is {:.2f}".format(number))

num = 1000

print("the number pi is {:,}".format(num))
print("the number pi is {:b}".format(num))
print("the number pi is {:o}".format(num))
print("the number pi is {:x}".format(num))
print("the number pi is {:X}".format(num))
print("the number pi is {:e}".format(num))