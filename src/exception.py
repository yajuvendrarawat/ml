import sys

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script [{0}] Line Number [{1} Error Message [{2}]".format
    (
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message

class CustomExceptions(Exception):
    def __init__(self,error_message,error_details:sys):
        super.__init__(error_message)
    