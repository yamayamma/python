from log_init import init_logger

logger = init_logger(__name__, './', 'test', level_file='info')

def hoge():
    return 1, 10, 100

def main():
    tmp = hoge()
    logger.info(f'this is {tmp}')
    logger.info(tmp)
    logger.warning('warning level is shown')
    logger.debug('debug level is not shown')

if __name__ == '__main__':
    main()
