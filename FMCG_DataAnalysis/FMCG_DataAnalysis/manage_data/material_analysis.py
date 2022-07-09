from materials import df
import numpy as np
from matplotlib import pyplot as plt

material = ['PM', 'RM']
count = list(df['RM_PM'].value_counts())
exp = [0, 0.1]
fig = plt.figure(figsize = (5,4))
# plt.pie(count, labels=material, explode=exp, autopct='%1.1f%%')
# plt.savefig('static\\PM_RM.png')
#plt.show()

temp_RM = df
temp_RM = temp_RM.loc[temp_RM['RM_PM'] == "RM"]
temp_RM = temp_RM.groupby(["MaterialGroup"])
temp_RM = temp_RM["MaterialID"].agg(np.count_nonzero)
# p = temp_RM.plot.barh(figsize=(10,8))
# plt.xlabel("Number of items")
# plt.ylabel("Raw Material Groups")
# plt.savefig('static\\temp_RM.png')
#plt.show()

temp_PM = df
temp_PM = temp_PM.loc[temp_PM['RM_PM'] == "PM"]
temp_PM = temp_PM.groupby(["MaterialGroup"])
temp_PM = temp_PM["MaterialID"].agg(np.count_nonzero)
# p = temp_PM.plot(kind = "bar", figsize=(10,8))
# plt.xticks(rotation='horizontal')
# plt.xlabel("Pakaged Material Groups")
# plt.ylabel("Number of items")
# plt.savefig('static\\temp_PM.png')
# plt.show()

