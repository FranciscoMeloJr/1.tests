import lttngust
import logging


def example():
    logger = logging.getLogger('my-logger')

    while True:
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
        time.sleep(1)


if __name__ == '__main__':
    example()
