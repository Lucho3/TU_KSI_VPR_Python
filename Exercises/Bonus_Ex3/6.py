def Recursion_Text(text):
    if len(text) == 0:
        return ''
    else:
        print(text[0])
        return Recursion_Text(text[2:])


Recursion_Text("azxcvbnm1")