import pandas as pd


with open("iris.data") as f:
    data = f.read()
    data = data.split("\n")

#print(data)
newData = []
for line in data:
    #print(line)
    newData.append(line.split(","))

#print(newData)
df = pd.DataFrame(newData, columns=["c1","c2","c3","c4","type"])
df.to_csv("py.csv",index=True)
print(df)
