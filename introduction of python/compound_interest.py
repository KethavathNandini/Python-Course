'''
amount = P*(1+R/100) ** T
compound interest = amount - principle(p)

'''

principle = float(input('enter the principle amount : '))
rate = float(input("enter the rate of interst : "))
time = float(input("enter the time : "))

amount = principle * pow((1 + rate / 100),time)
compound_interest = amount - principle
print("Compound Interest :",compound_interest)