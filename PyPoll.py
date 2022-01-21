f = open("election_data.csv","r")
f = f.readlines()
f.remove(f[0]) #this line removes the top header of the csv file
#print(f)
pollDict = {}
candidateList = []
list = []
votesCount = {}
khanCount = 0
correyCount = 0
liCount = 0
otooleyCount = 0


for item in f:
    splitItems = item.split(",")
    #print(splitItems)
    voterId = splitItems[0]
    voterCounty = splitItems[1]
    candidate = splitItems[2].strip()
    list.append(candidate)
    data = [voterCounty, candidate]
    if data[1] == "Khan":
        khanCount += 1
    elif data[1] == "Correy":
        correyCount += 1
    elif data[1] == "Li":
        liCount += 1
    elif data[1] == "O'Tooley":
        otooleyCount += 1
    pollDict[voterId] = data
#print(pollDict)

for candidate in list:
    if candidate not in candidateList:
        candidateList.append(candidate)

totalVotes = len(pollDict)
khanPercentage = "{:.2f}".format((khanCount / totalVotes) * 100)
correyPercentage = "{:.2f}".format((correyCount / totalVotes) * 100)
liPercentage = "{:.2f}".format((liCount / totalVotes) * 100)
otooleyPercentage = "{:.2f}".format((otooleyCount / totalVotes) * 100)

votesCount["Khan"] = khanCount
votesCount["Correy"] = correyCount
votesCount["Li"] = liCount
votesCount["O'Tooley"] = otooleyCount
winner = max(votesCount)
#position = votesCount.index(winner)


#print(votesCount.keys())
#position = (votesCount.keys()).index(winner)
# key_list = list(votesCount.keys())
# val_list = list(votesCount.keys())
# position = val_list.index(winner)
# print(position)



# print(totalVotes)
# print(candidateList)
# print(khanPercentage)
# print(correyPercentage)
# print(liPercentage)
# print(otooleyPercentage)

print('''
Election Results
----------------
''')
print(f"Total Votes: {totalVotes}")
print(f"Khan: {khanPercentage}% ({khanCount})")
print(f"Correy: {correyPercentage}% ({correyCount})")
print(f"Li: {liPercentage}% ({liCount})")
print(f"O'Tooley: {otooleyPercentage}% ({otooleyCount})")
print('''
----------------
Winner: Khan
''')
#print(f"{votesCount[index]}")
