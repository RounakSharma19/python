def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is graeter")

def isLesser(a,b):
    if(a<b):
        print("First number is lesser")
    else:
        print("Second number is lesser")




# Default argument

def average(a=9, b=1):
    print("The average is ", (a+b)/2)

average()

#  keyword argument

average(b=9, a=21) # here the order does not matter



# Arbitary arguments

def name(*name):
    print("Hello,", name[0],name[1],name[2])

name("James","Buchaan","Barnes")


# Keyword arbitraray arguments
def name1(**name):
    print("Hello,", name["fname"],name["mname"],name["lname"])

name1(mname="Buchaan", lname="Barnes", fname="James")


# return statement
def name2(fname,mname,lname):
    return "Hello," +fname+ " " + mname + " " + lname
    
print(name("James","Buchaan", "Barnes"))


