
"""
print('Capital Asset Pricing Model (CAPM)')
print('Formula: ER_i = B(ER_m - R_f')
print('ER_i = expected return of investment')
print('B = beta of the investment')
print('R_f = Risk-free rate')
print('ER_m - R_f = market risk premium')
"""

print('Capital Asset Pricing Model (CAPM)')


def CAPM(x,y,z):
    return x + (y*(z-x))
def func_Beta(x, y):
    return x / y
def YIELD(x, y):
    return x / y

def calculator():
    print('Type 1. to calculate CAPM')
    print('Type 2. to calculate Beta')
    print('Type 3. to calculate Dividend Yield')
 
    
    operator = int(input(':'))
    if operator == 1:
        user_input_5 = float(input('Risk-free rate:'))
        user_input_6 = float(input('beta of the investment:'))
        user_input_7 = float(input('Expected return of the investment:'))
        print('CAPM:', CAPM(user_input_5, user_input_6, user_input_7))
    elif operator == 2: 
        user_input_3 = float(input('Covariance:'))
        user_input_4 = float(input('Variance:'))
        print('Beta:', func_Beta(user_input_3, user_input_4))
        
    elif operator == 3:
        user_input_5 = float(input('Annual Dividends per share:'))
        user_input_6 = float(input('Price per share:'))
        print('Divident Yield:', YIELD(user_input_5, user_input_6))
        
        
    else:
        print('Error')
        return calculator()
    
calculator()
