import traceback


def raise_exception(ExceptionType):
    raise ExceptionType('My exception')


try:
    raise_exception(TypeError)
except TypeError as err:
    print('Handled with TypeError: ', err)
    traceback.print_tb(err.__traceback__)
except ValueError as err:
    print('Handled with ValueError')
except Exception as err:
    print('Handled with Exception')
except (TypeError, ValueError) as err:
    print('TypeError or ValueError')
except:
    print('Handled in except')
print('It still works!')
#
# try:
#     raise_exception(TypeError)
# except Exception as err:
#     if type(err) == TypeError:
#         print('Handled with TypeError: ', err)
#     elif type(err) == ValueError:
#         print('Handled with ValueError')

try:
    raise_exception(KeyError)
except KeyError as err:
    print('Logged', err)
    raise err
