
poro = input("What is the reservoir porosity")
area = input("What is the acreage of the reservoir")
h = input("What is the thickness of the reservoir")
sw = input("What is the water saturation of the reservoir")
boi = input("What is formation volume factor of the reservoir fluid")

poro = float(poro)
area = float(area)
h = float(h)
sw = float(sw)
boi = float(boi)

N = (7758*area*h*poro*(1-sw))/boi

print('The amount of oil initially in place is ', N)


