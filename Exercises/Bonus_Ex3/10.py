class Arabic_Roman:
    def __init__(self):
        self.arabic=1
        self.roman=''
        self.map=conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
            [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
            [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
            [   1, 'I']]


    def get_arabic(self,arabic):
        self.arabic=arabic

    def get_roman(self,roman):
        self.roman=roman


    def __get_count(self,text,pattern):
        return text.count(pattern)
        
    def roman_to_arabic(self):
        result = 0
        
        for arabic_digit, roman_digit in self.map:
            while len(self.roman)>0 and self.roman.startswith(roman_digit):
                p=len(self.roman)-len(self.roman.lstrip(roman_digit))
                result+=arabic_digit*self.__get_count(self.roman[:p],roman_digit)
                self.roman=self.roman.lstrip(roman_digit)
        return result


    def arabic_to_roman(self):
        result = ''
        for denom, roman_digit in self.map:
            result += roman_digit*(self.arabic//denom)
            self.arabic %= denom
        return result


st=Arabic_Roman()
st.get_arabic(2631)
#MMDCXXXI
print(st.arabic_to_roman())

