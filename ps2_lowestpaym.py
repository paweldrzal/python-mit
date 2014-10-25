"""program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month."""

fp1 = 10
s = True
fixedPayment = 0 

def adequatePayment(balance,annualInterestRate,fixedPayment):
    month = 1
    while month <= 12:
        balance -= fp1
        balance += (annualInterestRate/12.0)*balance
        month += 1
    if balance <= 0:
        return fp1
    else:
        return False

while s == True:
    if adequatePayment(balance,annualInterestRate,fp1):
        s = False
        print 'Lowest Payment:',adequatePayment(balance,annualInterestRate,fp1)
    else:
        fp1 += 10
        adequatePayment(balance,annualInterestRate,fp1)

