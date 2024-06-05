import os , sys
sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")
from src.logger import logging


# exc_tb = exception from try block
# exc_info = exiuation infomation complete imformation

def error_message_detail(error , error_detail:sys):
    _,_, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    # 0 = exec_tb 
    # 1 = tb_frame
    error_message = "Error occur in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name , exc_tb.tb_lineno , str(error))
    
    return error_message

class CustmerExcepetion(Exception):
    def __init__(self , error_message , error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message , error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Division by zero")
        raise CustmerExcepetion(e , sys)