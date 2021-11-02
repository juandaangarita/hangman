# word = "Outlook"
# lista = list(enumerate(word))

# print(lista)



# for count, element in lista:
#     if element == "o":
#         element == "-"
#         lista[count] = "-"
#         print(lista)
#         print(count)
        
def open_hangpics():
    with open("./files/HANGMANPICS.txt", "r", encoding="utf-8") as f:
        variable = []
        pics = f.readlines()
        for line in pics:
            variable.append(line.strip())
            # print(line)

    return variable


print(' '.join(open_hangpics()))