import logging
import datetime

def init_logger(module_name:str, outdir:str='', tag:str='',
                level_console:str='warning', level_file:str='info'):
    '''
    initialize logger
    parameters:
        module_name: str 対象のモジュール名,__name__など
        outdir: str output_dir
        tag: str outdut_file_name
        level_console, level_file: str logging level
    '''

    level_dic = {
        'critical':logging.CRITICAL,
        'error':logging.ERROR,
        'warning':logging.WARNING,
        'info':logging.INFO,
        'debug':logging.DEBUG,
        'notset':logging.NOTSET
        }
    tag = datetime.datetime.now().strftime('%Y%m%d_%H%M_') + tag
    
    # logging.basicConfig(
    #     level=level_dic[level_file],
    #     filename=f'{outdir}/log_{tag}.log',
    #     format='[%(asctime)s] [%(levelname)s] %(message)s',
    #     datefmt='%Y%m%d_%H%M%S',
    # )
    logger = logging.getLogger(module_name)
    logger.setLevel(level_dic['debug'])

    sh = logging.StreamHandler()
    fh = logging.FileHandler(f'{outdir}/log_{tag}.log')
    fh.setLevel(level_dic[level_file])
    sh.setLevel(level_dic[level_console])
    fmt = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(message)s',
        '%Y%m%d_%H%M%S'
        )
    sh.setFormatter(fmt)
    fh.setFormatter(fmt)
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger
