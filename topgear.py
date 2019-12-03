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
