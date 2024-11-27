import logging
import colorlog

console_handler = logging.StreamHandler()
color_formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    },
)

console_handler.setFormatter(color_formatter)

server_request_log = logging.getLogger(__name__)
server_request_log.addHandler(console_handler)
server_request_log.setLevel(logging.DEBUG)