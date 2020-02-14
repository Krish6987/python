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
