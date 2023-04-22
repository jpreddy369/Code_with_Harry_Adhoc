with open("currencyData.txt") as f:
    lines = f.readlines()

currr_Dict = {}

for line in lines:
    parsed = line.split("\t")
    currr_Dict[parsed[0]] = parsed[1]

print(currr_Dict)
Amount = int(input('Please enter the Amount \n'))
print('please select the currency from the list below')
[print(item) for item in currr_Dict.keys()]
currency = input('select the currency from list')
print(f"{Amount} is equal to {Amount * float(currr_Dict[currency])}    {currency}")