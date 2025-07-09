import os
import sys

class AppException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = AppException.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_message = f"Error occurred in script: [{file_name}] at line number: [{exc_tb.tb_lineno}] with message: [{str(error_message)}]"
        return error_message

    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return AppException.__name__.str() + f"({self.error_message})"