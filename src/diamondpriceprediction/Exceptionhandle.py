import sys

class CustomException(Exception):

    def __init__(self,error_message,error_details :sys):
        
        self.error_message=error_message
        # error details means which module or file or script i get a error message and which line number i got a error so the type of error message is sys(system)
        _,_,exc_tb=error_details.exc_info()
        # here exe_tb is execuatation trace back , exc_info() function is provided by sys who give the all detailed about the error message
        #_,_, these two paramerter is not important , so we don't need to store these in any parameter.

        self.line_number=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    # __str__ this method is used to print the string representation of the any object 
    def __str__(self):
        return "the error occured in the python script [{0}] and the line number is [{1} and error message[{2}]]".format( self.file_name,self.line_number,str(self.error_message))

if __name__=="__main__":
    try:
        a=3/0

    except Exception as e:
        raise CustomException(e,sys)
