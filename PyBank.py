f = open("budget_data.csv", "r")
f = f.readlines()
#print(f)


f.remove(f[0])

#print(f)

bankDict = {} #how we make dictionary


for item in f:
  
  splitItems = item.split(",")
  #print(splitItems)
  date = splitItems[0]
  profit = splitItems[1]
  bankDict[date] = profit

#print(bankDict)
totalMonths = len(bankDict)
totalProfit = 0
#print(totalMonths)
for date in bankDict:
  amount = int(bankDict[date])
  #print(amount)
  totalProfit += amount #totalProfit = totalProfit + amount

#print(totalProfit)
averageChange = totalProfit / totalMonths
averageChange = "{:.2f}".format(averageChange)
#print(averageChange)
highestProfit = max(bankDict.values())

#highestProfitDate = 
lowestProfit = min(bankDict.values())
#print(highestProfit)
#print(lowestProfit)
#print(bankDict)
display = '''
Financial Analysis:
------------------------ 
'''

print(display)
print(f"Total Months: {totalMonths} months")
print(f"Total Profit/Loss: ${totalProfit}")
print(f"Average Change: ${averageChange}")
print(f"Highest Profit: ${highestProfit}".strip())
print(f"Lowest Profit: ${lowestProfit}")