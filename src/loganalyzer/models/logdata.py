from pydantic import BaseModel
from utils import utilities

utilities.add_root_to_syspath()

from data import data_generator

class LogData(BaseModel):
    ip: str
    http_method: str
    http_endpoint: str
    http_response: str


if __name__ == '__main__':
    log_data = LogData(ip = "127.0.0.1", http_method = "method", 
    http_endpoint = "endpoint", http_response = "response_code")
    print(f"*********************{log_data.http_endpoint}")