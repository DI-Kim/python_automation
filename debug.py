
import traceback
import logging

"""
boxPrint function
******************************
*                            *
*                            *
*                            *
******************************
"""


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width < 2 or height < 2:
        raise Exception('Width and height must be at least 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)
    return None


boxPrint('*', 10, 5)
boxPrint('0', 2, 2)

try:
    raise Exception('This is an exception.')
except Exception as e:
    errorFile = open('errorLog.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.write('\n')
    errorFile.close()
    print('Error logged to errorLog.txt')

print()

# assertion : programmer's error
# assert False, 'This is an assertion error.'

# logging은 print 문과 비슷하지만, logging 모듈을 사용하면 로그 레벨을 설정할 수 있고, 로그를 파일에 저장하거나 콘솔에 출력하는 등의 다양한 기능을 제공한다.
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)  # Disable all logging above CRITICAL level
'''
logging.debug() # lowest level of logging
logging.info()
logging.warning()
logging.error()
logging.critical() # highest level of logging

logging.disable(logging.DEBUG) # Disable all logging below DEBUG level
logging.disable(logging.INFO) # Disable all logging below INFO level

'''
logging.debug('start of program')


def factorial(n):
    logging.debug(f'start of factorial({n})')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i: {i}, total: {total}')
    logging.debug(f'total: {total}')
    return total


print(factorial(5))

logging.debug('end of program')
