class Strings:
    def __init__(self):
        self.text=''

    def get_String(self,text):
        self.text=text

    def print_String(self):
        print(self.text)

st=Strings()
st.get_String("Pesho")
st.print_String()