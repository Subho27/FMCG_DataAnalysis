import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataset = pd.ExcelFile("data\\2018.xlsx")
months =  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
list2018 = []
for m in months:
    list2018.append(pd.read_excel(dataset, m, skiprows=3, usecols="D:F"))
for df in list2018:
    df["Unit Price"] = df["Unit Price"].apply(float)*df["Qty of Usage"].apply(float)
    df.rename(columns = {"RM/PM":"RM_PM","Material":"MaterialID","Description":"MaterialDetails",\
                    "Qty of Usage":"Qty of Usage","Unit Price":"Total Spend"},inplace = True)
addedDF = list2018[0].set_index('MaterialDetails').add(list2018[1].set_index('MaterialDetails'), fill_value=0).reset_index()
for i in range(2,len(list2018)):
    addedDF = addedDF.set_index('MaterialDetails').add(list2018[i].set_index('MaterialDetails'), fill_value=0).reset_index()
# print(addedDF)


dataset = pd.ExcelFile("data\\2019.xlsx")
months =  ['January', 'February', 'March', 'April', 'mAY', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
list2019 = []
for m in months:
    list2019.append(pd.read_excel(dataset, m, skiprows=4, usecols="D:F"))
for df in list2019:
    df.rename(columns = {"RM/PM":"RM_PM","Material":"MaterialID","Description":"MaterialDetails",\
                    "Actual Usage Quantity":"Qty of Usage","Unit Price":"Total Spend"},inplace = True)
addedDF1 = list2019[0].set_index('MaterialDetails').add(list2019[1].set_index('MaterialDetails'), fill_value=0).reset_index()
for i in range(2,len(list2019)):
    addedDF1 = addedDF1.set_index('MaterialDetails').add(list2019[i].set_index('MaterialDetails'), fill_value=0).reset_index()
# print(addedDF1)

dataset = pd.ExcelFile("data\\2020.xlsx")
months =  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
list2020 = []
for m in months:
    list2020.append(pd.read_excel(dataset, m, skiprows=4, usecols="D:F"))
for df in list2020:
    df["Unit Price"] = df["Unit Price"].apply(float)*df["Qty of Usage"].apply(float)
    df.rename(columns = {"RM/PM":"RM_PM","Material":"MaterialID","Description":"MaterialDetails",\
                    "Qty of Usage":"Qty of Usage","Unit Price":"Total Spend"},inplace = True)
addedDF2 = list2020[0].set_index('MaterialDetails').add(list2020[1].set_index('MaterialDetails'), fill_value=0).reset_index()
for i in range(2,len(list2020)):
    addedDF2 = addedDF2.set_index('MaterialDetails').add(list2020[i].set_index('MaterialDetails'), fill_value=0).reset_index()
# print(addedDF2.replace(np.nan,0))


finalDF = pd.merge(addedDF, addedDF1, on='MaterialDetails')
finalDF = pd.merge(finalDF, addedDF2, on='MaterialDetails')
finalDF.replace(np.nan,0)
# ax = finalDF.head(10).plot.barh(x="MaterialDetails", y="Total Spend")
# finalDF.head(10).plot.barh(x="MaterialDetails", y="Total Spend_y", ax=ax, color="orange")
# finalDF.head(10).plot.barh(x="MaterialDetails", y="Total Spend_x", ax=ax, color="green")
# Year = ["For 2020", "For 2019", "For 2018"]
# plt.xticks(rotation='horizontal')
# plt.legend(Year)
# fig = plt.gcf()
# fig.set_size_inches(30, 10.5)
# fig.savefig('static\\Yearwise_spend.png', dpi=100)
#plt.show()

ax = finalDF.head(10).plot.barh(x="MaterialDetails", y="Qty of Usage")
finalDF.head(10).plot.barh(x="MaterialDetails", y="Qty of Usage_y", ax=ax, color="orange")
finalDF.head(10).plot.barh(x="MaterialDetails", y="Qty of Usage_x", ax=ax, color="green")
Year = ["For 2020", "For 2019", "For 2018"]
plt.xticks(rotation='horizontal')
plt.legend(Year)
fig = plt.gcf()
fig.set_size_inches(30, 10.5)
fig.savefig('static\\Yearwise_usage.png', dpi=100)