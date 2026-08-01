from utils import utilities
import logging


#setup logger
logging.basicConfig(level=logging.INFO)
logging.getLogger(__name__)


#setup sys path
from utils import utilities
utilities.add_root_to_syspath()

#generate test log data
from data import data_generator
data_generator.generate_data_file(num_lines=10000)


#initialize database and connections


#parse generated data and write to db


#query data for insights

