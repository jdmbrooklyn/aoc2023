# DAY 1 PART ONE
# data = open('input_data.txt', 'r')
# totalnumber = 0
# while True:
#     content=data.readline()
#     if not content:
#         break
#     print(content)
#     digit_list = []
#     for item in content:
#         if item.isdigit():
#             digit_list.append(item)
#     print(digit_list)
#     double_digit = int(digit_list[0] + digit_list[-1])
#     print("The double digit for this line is: ", double_digit)
#     totalnumber = totalnumber + double_digit
# data.close()
# print("The total sum of all the numbers with double digits is: ", totalnumber)

#DAY ONE PART TWO
data = open('input_data.txt', 'r')
totalnumber = 0
numwords = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
while True:
    content=data.readline()
    if not content:
        break
    print(content)
    digit_dict = {}
    digit_list = []
    for word in numwords.keys():
        x = 0
        while x < len(content):
            if content[x:].find(word) != -1:
                digit_dict[content[x:].find(word)+x] = numwords[word]
                x = content[x:-1].find(word) + x + 1
            else:
                x = x + 1
    print(digit_dict)

    for y in range(0, len(content)):
        if content[y].isdigit():
            digit_dict[y] = int(content[y])
    print(digit_dict)

    for z in sorted(digit_dict.keys()):
        digit_list.append(digit_dict[z])
    print(digit_list)
    double_digit = int(str(digit_list[0]) + str(digit_list[-1]))
    print("The double digit for this line is: ", double_digit)
    totalnumber = totalnumber + double_digit
data.close()
print("The total sum of all the numbers with double digits is: ", totalnumber)
