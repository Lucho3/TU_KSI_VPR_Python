#Vuzmojno e nqkude da ima greshka, koqto ne sum widql

class Bracket_Check:
    def __init__(self):
        self.open_list = ["[", "{", "("]
        self.close_list = ["]", "}", ")"]


    def Match(self,text):    
        if len(text)%2==1:
            return False 

        counter=0    
        while len(text)!=0:  
            
            if counter+1>len(text)-1:               
                return False
                   
            first_bracket=text[counter]
            second_bracket=text[counter+1]

            if first_bracket in self.open_list and second_bracket in self.close_list:
                if self.open_list.index(first_bracket)==self.close_list.index(second_bracket):
                    text=text[0:counter:]+text[counter+2::]
                    counter-=2
            if counter<0:
                counter=0
            else:
                counter+=1

        return True


            

bc=Bracket_Check()
ls=bc.Match("()[]([[[()]]])([{)])")
print(ls)