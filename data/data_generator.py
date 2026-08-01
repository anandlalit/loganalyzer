from pathlib import Path
import logging
import random
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

SEED_IP = '127.0.0.1'
SEED_HTTP_METHOD = 'GET'
SEED_HTTP_ENDPOINT_PATH = '/api/users'
SEED_HTTP_RESPONSE_CODE = '200'

CHOICE_SELECTOR = ['ip', 'http_method', 'http_endpoint', 'http_response_code']

SEED_LOG_LINE: str = f"{{SEED_IP}} [30/Jul/2026:14:22:01] {{SEED_HTTP_METHOD}} {{SEED_HTTP_ENDPOINT_PATH}} HTTP/1.1 {{SEED_HTTP_RESPONSE_CODE}}\n"

def generate_data_file(file_name: str = "log_data_for_analysis.log", num_lines: int = 1, clean_before_writing: bool = True) -> None:
    """
    Generate a sample log file with log entries.

    Args:
        file_path: Path to the output log file
        num_lines: Number of log lines to generate
    """
    current_directory = Path(__file__).parent
    log.info(f"Current file directory path {current_directory.resolve()}")
    
    data_file = Path(current_directory / file_name)

    if clean_before_writing and data_file.exists():
        log.info(f"Deleting file {data_file.resolve()}")
        data_file.unlink()

    with open(data_file, 'a') as log_data:
        log.info(f"Starting to write data to the data file {data_file.resolve()}")
        for counter in range(num_lines):
            log_data.write(introduce_noise(random.choice(CHOICE_SELECTOR)))
        log.info(f"Data file creation is complete with lines added {counter}")


def introduce_noise(choice: str) -> str:
    """
    This function will introduce noise to the data generation file.
    Args:
        choice: The name of variability to introduce
    """
    choices: dict = {
    CHOICE_SELECTOR[0]: random.choice([SEED_IP,'0.0.0.1', '197.24.24.234','145.23.27.99']), # ip choices
    CHOICE_SELECTOR[1]: random.choice([SEED_HTTP_METHOD,'POST','PUT', 'DELETE']), # http method choice
    CHOICE_SELECTOR[2]: random.choice([SEED_HTTP_ENDPOINT_PATH, '/api/orders', '/api/products', '/api/cartinfo']), # http endpoint choices
    CHOICE_SELECTOR[3]: random.choice([SEED_HTTP_RESPONSE_CODE, '401', '403', '500']), # http response code choices        
    }

    return SEED_LOG_LINE.format(SEED_IP = choices[CHOICE_SELECTOR[0]],
    SEED_HTTP_METHOD = choices[CHOICE_SELECTOR[1]],
    SEED_HTTP_ENDPOINT_PATH = choices[CHOICE_SELECTOR[2]],
    SEED_HTTP_RESPONSE_CODE = choices[CHOICE_SELECTOR[3]])

if __name__ == '__main__':
    generate_data_file(num_lines = 10000, clean_before_writing = True)
