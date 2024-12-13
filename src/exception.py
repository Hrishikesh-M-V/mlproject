# this is for exception handling

import sys
import logging
from src import logger

def error_message_detail(error, error_detail:sys):
    '''exc _info Returns a tuple (type, value, traceback), where traceback contains the traceback object (exc_tb).
        exc_tb.tb_frame: Refers to the current stack frame where the exception occurred
        tb_frame.f_code.co_filename: Extracts the file name from the code object (f_code) associated with the frame.'''
    
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno 
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, line_number, str(error)

    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail :sys):
        # It’s a good practice to always call the parent constructor when subclassing exceptions (or any other class) to ensure proper initialization of inherited functionality.
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
        

