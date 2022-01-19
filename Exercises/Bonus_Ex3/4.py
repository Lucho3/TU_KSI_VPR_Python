def Text_From_Indexes(text,*indexes):
    text_for_return=''
    for i in indexes:
        if i<len(text):
            text_for_return+=text[i]

    return text_for_return


print(Text_From_Indexes("Pesho",1,2,15))


