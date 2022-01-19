import json

class Student:
    def __init__(self,name,f_num,success_rate):
        self.name=name
        self.f_num=f_num
        self.success_rate=success_rate

    def __str__(self):
        return "{} {} {}".format(self.name,self.f_num,self.success_rate)

    def convert_to_json(self):
        return json.dumps(self.__dict__)