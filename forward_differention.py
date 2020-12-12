class ForwardDerivative:

    def __init__(self, x, h):
        self.x = x
        self.h = h

    def function(self, x):
        return x* x

    def derivative(self, x, h):
        return (self.function(x + h) - self.function(x)) / h



h = 0.000001
x = 1
derivative1 = ForwardDerivative(x, h)
print(derivative1.derivative(x, h))
