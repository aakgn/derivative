# @author: ali.akgun
# @brief:
# @to do:
# @bugs:
# @date: 23.12.2020
from math import *
class ForwardDerivative:

    def __init__(self, x, h, function):
        self.x = x
        self.h = h
        self.function = function

    def derivative(self, x, h):
        return (self.function(x + h) - self.function(x)) / h



h = 0.000001
x = 1
user_input = "sin(x)"
function = lambda x: eval(user_input)
derivative1 = ForwardDerivative(x, h, function)
print(derivative1.derivative(x, h))
