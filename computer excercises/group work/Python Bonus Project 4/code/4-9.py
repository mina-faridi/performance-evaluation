#! python3.9
# Q9.py
# Author : Pooya Jamshidi
# This code represent The result of Problem No. 9 in Section 4 of Bertsekas Book.
import math

lambda_param = float(input("Please Enter The lambda parameter of variable X : "))
mu_param = float(input("Please Enter The mu parameter of variable Y : "))
z = float(input("Please Enter z : "))

cdf = pdf = 0

if z >= 0:
    cdf = 1 - (mu_param * math.exp(-lambda_param * z)) / (mu_param + lambda_param)
    pdf = (lambda_param * mu_param * math.exp(-lambda_param * z)) / (mu_param + lambda_param)
else:
    cdf = (lambda_param * math.exp(mu_param * z)) / (mu_param + lambda_param)
    pdf = (lambda_param * mu_param * math.exp(mu_param * z)) / (mu_param + lambda_param)

print("The CDF of Z=X-Y for z=" + str(z) + " is : " + str(cdf))
print("The PDF of Z=X-Y for z=" + str(z) + " is : " + str(pdf))

input("Thank You for your time, press Enter for exit... ")