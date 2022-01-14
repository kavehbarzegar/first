import signal
import yaml
import logging
from time import sleep

logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s',level=logging.INFO)

def sig_handler(sig, frame):
    level = logging.DEBUG
    logger = logging.getLogger()
    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)
    print("level has been changed to DEBUG")

signal.signal(signal.SIGINT, sig_handler)

def sig_handler2(sig, frame):
    level = logging.INFO
    logger = logging.getLogger()
    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)
    print("level has been changed to INFO")

signal.signal(signal.SIGQUIT, sig_handler2)

while True:
    def read_config(filename, mandatory_key_list, cfg):
        file_content = open(filename).read()
        try:
            file_cfg = yaml.safe_load(file_content)
        except Exception as parser_error:
            return False, 'could not decode config content' + str(parser_error)
        for mandatory_key in mandatory_key_list:
            logging.debug('mandatory_key:' + mandatory_key)
            logging.info('mandatory_key:' + mandatory_key)
            if mandatory_key not in file_cfg.keys():
                return False, 'could not found "' + mandatory_key + '"'
        merged_cfg = {**cfg, **file_cfg}
        return True, merged_cfg

    status, result = read_config('my-config.kv', ['first-name', 'last-name'], {'middle-name': ''})
    if not status:
        print(result)
        exit(1)
    cfg = result
    logging.debug(cfg)
    logging.info(cfg)
    print('Your name is', cfg['first-name'], cfg['middle-name'], cfg['last-name'])
    sleep(10)
