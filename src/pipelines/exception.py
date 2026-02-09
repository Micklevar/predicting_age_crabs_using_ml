import sys

def error_message_detail(error, error_detail: sys):
    # Obtenemos el traceback (exc_tb)
    _, _, exc_tb = error_detail.exc_info()
    
    # Extraemos el nombre del archivo y la línea
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    # Formateamos el mensaje
    error_message = "Error en el script: [{0}] | Línea: [{1}] | Mensaje: [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Generamos el mensaje de error detallado usando nuestra función
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message