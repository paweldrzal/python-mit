"""program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month."""

month = 1
totalPaid = 0
while month <= 12:
    annualInterestRate = annualInterestRate / 12.0
    minMonthlyPaymnemt = monthlyPaymentRate*balance
    balance -= minMonthlyPaymnemy
    balance += annualInterestRate * balance 
    monthlyUnpaidBalance = balance - minMonthlyPaymnemt
    updatedBalanceEachMonth = monthlyUnpaidBalance + air*monthlyUnpaidBalance 
    print "Month: %d" % month
    month += 1
    print "Minimum monthly payment: %.2f" % minMonthlyPaymnemt
    print "Remaining balance: %.2f" % balance
    totalPaid += minMonthlyPaymnemt
    
print round(totalPaid, 2)
print "Remaining balance: %.2f" % balance


