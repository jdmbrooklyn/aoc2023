# DAY 3 PART ONE
data = open('input3.txt', 'r')
linenumber = 1
mapping_dict = {}
while True:
    content=data.readline()
    if not content:
        break
    print(content)
    mapping_dict[linenumber]={'nums':{}, 'symbols':{}}
    x = 0
    y = 0
    while x < len(content)-1:
        if content[x].isdigit():
            startindex = x
            value = content[x]
            while content[x+1].isdigit():
                value += content[x+1]
                x += 1
            mapping_dict[linenumber]['nums'][y] = {'index':startindex, 'length':len(value), 'value':int(value)}
            y += 1
        elif content[x] != '.':
            mapping_dict[linenumber]['symbols'][x]=content[x]
        x += 1
    print(mapping_dict[linenumber])
    print(len(mapping_dict))
    linenumber += 1
data.close()

totalnumber = 0

for i in range(1, len(mapping_dict)+1):
    for num in mapping_dict[i]['nums'].keys():
        include = False
        value = mapping_dict[i]['nums'][num]['value']
        indexstart = mapping_dict[i]['nums'][num]['index']
        indexend = indexstart + mapping_dict[i]['nums'][num]['length']
        if indexstart-1 in mapping_dict[i]['symbols'].keys():
            include = True
        if indexend in mapping_dict[i]['symbols'].keys():
            include = True

        if i > 1:
            try:
                for priorLineSymbol in mapping_dict[i-1]['symbols'].keys():
                    if priorLineSymbol in range(indexstart-1,indexend+1):
                        include = True
            except:
                print("No symbols on line ", i-1)

        if i < 140:
            try:
                for nextLineSymbol in mapping_dict[i+1]['symbols'].keys():
                    if nextLineSymbol in range(indexstart-1,indexend+1):
                        include = True
            except:
                print("No symbols on line ", i+1)

        if include:
            print("Number ", value, " on line ", i, " is included in the sum.")
            totalnumber += value
            # print("The sum is currently: ", totalnumber)

print("The sum of all numbers is: ", totalnumber)
