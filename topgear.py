######1


urls = input().split(" ")

domain = ["edu","com","org","in"]

result_dict ={

    "1": [],

    "2": [],

    "3": [],

    "4": []

}

result = []



for i in urls:

    temp = i.split(".")

    index = domain.index(temp[-1])

    result_dict[str(index+1)].append(i)


for i in range(1,5):
    for j in result_dict[str(i)]:

        result.append(j)



print(result)
    

    



#####2


strings = input().split(" ")

count = 0


for i in strings:

    if len(i) >= 2:

        if i[0] == i[-1]:

            count += 1


print(count)

#####3
strings = input().split(" ")

withx = []

without = []

result = []



for i in strings:

    if i[0] == 'x':

        withx.append(i)

    else:

        without.append(i)

withx = sorted(withx)

without = sorted(without)


for i in withx:

    result.append(i)

for i in without:

    result.append(i)



print(result)


#####4

inp = []

n = int(input())


for i in range(n):

    x = input().split()

    for j in range(len(x)):

        x[j] = int(x[j])

    inp.append(tuple(x))



for i in range(len(inp)-1):

    for j in range(len(inp)-1):

        if inp[j][len(inp[j])-1]>inp[j+1][len(inp[j+1])-1]:

            inp[j], inp[j+1] = inp[j+1], inp[j]



print(inp)



#####5
inp = input().split(" ")

for i in range(len(inp)):

    inp[i] = int(inp[i])


result = [inp[0]]


for i in inp:

    if i != result[-1]:

        result.append(i)

print(result)

#####6
def printbook(bookstore):

    print("BOOKSTORE\n\n")

    print("'"+bookstore["New Arrivals"]["WEB"][0]+"','", bookstore["New Arrivals"]["WEB"][1]+"','",bookstore["New Arrivals"]["WEB"][2]+"','", bookstore["New Arrivals"]["WEB"][3]+"'",sep="")

    print("'"+bookstore["New Arrivals"]["COOKING"][0]+"','", bookstore["New Arrivals"]["COOKING"][1]+"','",bookstore["New Arrivals"]["COOKING"][2]+"','", bookstore["New Arrivals"]["COOKING"][3]+"'",sep="")

    print("'"+bookstore["New Arrivals"]["CHILDREN"][0]+"','", bookstore["New Arrivals"]["CHILDREN"][1]+"','",bookstore["New Arrivals"]["CHILDREN"][2]+"','", bookstore["New Arrivals"]["CHILDREN"][3]+"'",sep="")

    


bookstore = {

    "New Arrivals":{

        "COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],

        "CHILDREN":["Harry Potter", "J K. Rowling","2005","29.99"],

        "WEB":["Learning XML","Erik T. Ray","2003","39.95"]

    }

}


printbook(bookstore)

    



######7
str1="""Python is a widely used high-level programming language for general-purpose programming, created 
by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy 
which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than
 curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code 
than possible in languages such as C++ or Java. The language provides constructs intended to enable writing 
clear programs on both a small and large scale. Python features a dynamic type system and automatic memory 
management and supports multiple programming paradigms, including object-oriented, imperative, functional 
programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters 
are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, 
the reference implementation of Python, is open source software and has a community-based development model, 
as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""


str1 = str1.replace(".","")

str1 = str1.replace(",","")

str1 = str1.replace(")","")

str1 = str1.replace("("," ")

lstr1 = str1.split(" ")

result = {}


for i in lstr1:

    count = 0

    if i not in result:

        for j in lstr1:

            if j == i:

                count += 1

        result[i] = count

temp = []

for key, value in sorted(result.items(), key=lambda item: item[1]):

    temp.append(key)



print(temp[-1], temp[-2],temp[-3],temp[-4],temp[-5], sep="\n")  


#####8

str1="""Python is a widely used high-level programming language for general-purpose programming, created 
by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy 
which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than
 curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code 
than possible in languages such as C++ or Java. The language provides constructs intended to enable writing 
clear programs on both a small and large scale. Python features a dynamic type system and automatic memory 
management and supports multiple programming paradigms, including object-oriented, imperative, functional 
programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters 
are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, 
the reference implementation of Python, is open source software and has a community-based development model, 
as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""




str1 = str1.replace(".","")

str1 = str1.replace(",","")

str1 = str1.replace(")","")

str1 = str1.replace("("," ")

lstr1 = str1.split(" ")

result = {}


for i in lstr1:

    if i not in result:

        result[i] = []

    for j in range(len(lstr1)-1):

        if lstr1[j] == i:

            if lstr1[j+1] not in result[i]:

                result[i].append(lstr1[j+1])

print(result)             
         
