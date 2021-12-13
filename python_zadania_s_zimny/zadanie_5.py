class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        return Complex((self.real + other.real), (self.imag + other.imag))

    def __sub__(self,other):
        return Complex((self.real - other.real), (self.imag - other.imag))

    def __mul__(self,other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.real)
    
    def __str__(self):
        return '(%s, %si)' % (self.real, self.imag)




class Calculator:

    def __init__(self, num1=0, num2=0, operation=None):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def __call__(self):
        if self.operation == '+':
            return self.num1 + self.num2
        elif self.operation == '-':
            return self.num1 - self.num2
        elif self.operation == '*':
            return self.num1 * self.num2


    def partition(self, operation):
        factors = operation.split(' ')
        factor_1 = self.parser(factors[0])
        factor_2 = self.parser(factors[2])
        factors = factors[1]

        return Calculator(factor_1, factor_2, factors)


    @staticmethod
    def parser(number):
        if '+' in number:
            sign_form = number.split('+')
            complex_numb = Complex(float(sign_form[0]), float(sign_form[1][:-1]))

        elif '-' in number:
            flag = False

            if number[0] == '-':
                flag = True

            sign_form = number.split('-')
            if flag==False:
                num = float(sign_form[0])
            else:
                num = (-float(sign_form[0]))
            complex_numb = Complex(num, -float(sign_form[1][:-1]))
        
        elif '*' in number:
            sign_form = number.split('*')
            complex_numb = Complex(float(sign_form[0]), float(sign_form[1][:-1]))

        return complex_numb


def test_complex():
    a = Complex(1,1)
    b = Complex(1,1)
    result = Complex.__add__(a,b)

    print("Your results: %s "%result)
    

def calculator():
    print("Enter your equation in complex number form: (acceptable form equation is 'A+Bi + C+Di' ) ")
    input_data = input()
    calc = Calculator().partition(input_data)
    print("Your results: %s" %calc())


if __name__ == "__main__":
    #test_complex()
    calculator()

