from utils import utilities
import logging


#setup logger
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


#setup sys path
from utils import utilities
utilities.add_root_to_syspath()

#generate test log data, in deployed env system will be fed with the live logs data
from data import data_generator
data_generator.generate_data_file(num_lines=10000)


#initialize database and connections
from loganalyzer.repository.databasemgr import DatabaseManager
database_handler = DatabaseManager()
database_handler.connect()
database_handler.init_database()
database_handler.execute_sql("INSERT INTO logs (ip, http_method, http_api_path, http_response_code) VALUES ('127.0.0.1', 'GET', '/api/users', '200')")
rs = database_handler.execute_sql("select * from logs")
log.info(f"the stored ip {rs[0][1]}")

#parse generated data and write to db


#query data for insights

