import pandas as pd

dataset = pd.read_excel("data\Material groups.xlsx")
df = pd.DataFrame(dataset)

# =============================================================================
# renaming the columns
# =============================================================================

df.rename(columns = {"Material":"MaterialID","Description":"MaterialDetails","RM/PM":"RM_PM",\
                    "Material group":"MaterialGroup"},inplace = True)

# =============================================================================
# modifying one column 
# =============================================================================

udf = df

def modifyMD(s):
    if "-" in s:
        return ' '.join(s.split("-")[1:])
    else:
        return s

df["MaterialDetails"] = df["MaterialDetails"].apply(modifyMD)

# print(df)

