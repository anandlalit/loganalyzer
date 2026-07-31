from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

SEED_LOG_LINE: str = '127.0.0.1 - - [30/Jul/2026:14:22:01] "GET /api/users HTTP/1.1" 200 512\n'

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
            log_data.write(SEED_LOG_LINE)
        log.info(f"Data file creation is complete with lines added {counter}")

if __name__ == '__main__':
    generate_data_file(num_lines = 10000, clean_before_writing = True)
