


print("The CDF of Z=|X-Y| is equal to : F(z) = 1-((1-z)*(1-z))")
print("The PDF of Z=|X-Y| is equal to : f(z) = 2*(1-z)")

z = float(input("Please Enter z : "))

CDF = PDF = 0

if (z >= 0 and z <= 1) :
    CDF = 1 - ((1-z)*(1-z))
    PDF = 2*(1-z)
elif z<0 :
    CDF = 0
    PDF = 0
else :
    CDF = 1
    PDF = 0

print("The CDF of Z=|X-Y| for z=" + str(z) + " is : " + str(CDF))
print("The PDF of Z=|X-Y| for z=" + str(z) + " is : " + str(PDF))
