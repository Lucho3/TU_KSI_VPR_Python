class Text_Reverser:
    def __init__(self,text):
        self.text = text

    def Reverse_Text(self):
        return self.text.split()[::-1]

tr=Text_Reverser("I Love Python!")

print(tr.Reverse_Text())