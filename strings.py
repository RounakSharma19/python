# name = "Rounak"
# print("Hello," + name)
# name1 = ''' Hi Rounak
# Hi Siri!! How are you?
# I am great Rounak, Thanks for asking '''

# print(name1)


# print("Lets use a for loop with strings\n")
# for character in name1 :
    # print(character)


    # slicing in string

    # fruit = "Mango"
    # mangoLen = len(fruit)
    # print(mangoLen)
    # print(fruit[0:4])
    # print(fruit[1:4])
    # print(fruit[:5])
    # print(fruit[:])
    # print(fruit[0: -3])
    # print(fruit[0:len(fruit) -3])
    # print(fruit[-3: -1])


    # nm="Harry"
    # print(nm[-4:-2])

    # STINGS METHODS

str1 = " Rounak Sharman"
print(str1.upper())
print(str1.lower())
print(str1.strip())

str2 ="Rounak Sharma !!!!!!!!"
print(str2.rstrip("!"))
print(str2.endswith("!!!!!!!!"))

print(str1.replace("Rounak", "John"))
print(str1.split(" "))
str3 = "introduction to Python"
print(str3.capitalize())
print(str3.find("to"))
print(str3.index("to"))
str4 = "introductiontoPython"
print(str4.isalnum())
print(str4.isalpha())
print(str4.islower())
print(str4.isprintable())
print(str4.isspace())
print(str4.istitle ())
