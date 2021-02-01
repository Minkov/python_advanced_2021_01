from numbersystem import decimalToBinary, decimalToHexa
from termcolor import colored
from pyfiglet import figlet_format

from utils import app_sum

x = 1555
print(x)
print(decimalToBinary(x))
print(decimalToHexa(x))

print(colored(str(x), 'red', attrs=['bold', 'underline']))
print(figlet_format('Python', font='isometric1'))
print(app_sum(1, 3))