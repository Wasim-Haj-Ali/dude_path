from pydantic import BaseModel

class Response(BaseModel):
    status_code: str
    data: list = []
    message: str = ""
    
    
    def __init__(self, status_code: str, data: list, message: str):
        super().__init__(status_code=status_code, data=data, message=message)
        
        codes = {
            "200": "OK " ,
            "201": "Created " ,
            "202": "Accepted " ,
            "203": "Non - authoritative Information " ,
            "204": "No Content " ,
            "205": "Reset Content " ,
            "400": "Bad Request " ,
            "401": "Unauthorized " ,
            "402": "Payment Required " ,
            "403": "Forbidden " ,
            "404": "Not Found " ,
            "405": "Method Not Allowed " ,
            "406": "Not Acceptable " ,
            "407": "Proxy Authentication Required " ,
            "408": "Request Timeout " ,
            "413": "Payload Too Large " ,
            "414": "Request - URI Too Long " ,
            "415": "Unsupported Media Type " ,
            "416": "Requested Range Not Satisfiable " ,
            "417": "Expectation Failed " ,
            "500": "Internal Server Error " ,
            "501": "Not Implemented " ,
            "502": "Bad Gateway " ,
            "503": "Service Unavailable " ,
            "504": "Gateway Timeout " ,
            "505": "HTTP Version Not Supported "
        }
        
        self.message = codes.get(self.status_code, "Status code not implemented") + self.message

