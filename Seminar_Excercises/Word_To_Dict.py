word=input("Enter new word: ")
dic_of_simbols=dict()

for i in range(len(word)):
    if dic_of_simbols.keys().__contains__(word[i]):
        dic_of_simbols.update({word[i]:dic_of_simbols[word[i]]+1})
    else:
        dic_of_simbols[word[i]]=1

print(dic_of_simbols)
