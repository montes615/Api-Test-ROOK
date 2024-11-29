import logging
import colorlog

console_handler = logging.StreamHandler()
color_formatter = colorlog.ColoredFormatter(
    '[%(levelname)s] - %(log_color)s%(asctime)s - %(message)s',
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

file_handler = logging.FileHandler('server_logs.log', mode='a', encoding='utf-8')
file_formatter = logging.Formatter(
    '[%(levelname)s] - %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(file_formatter)


server_request_log = logging.getLogger(__name__)
server_request_log.addHandler(console_handler)
server_request_log.addHandler(file_handler)
server_request_log.setLevel(logging.DEBUG)