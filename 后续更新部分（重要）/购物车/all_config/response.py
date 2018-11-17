



# def  Self_Respoonse():
#
#     return   {'code':1000,'msg':None}




class  Self_Response():

    def __init__(self):
        self.code=1000
        self.msg=None
        self.error=None
        self.all_data=None

    @property
    def get_response(self):


        return   self.__dict__




# obj=Self_Response()
#
#
# print(obj.get_response)

