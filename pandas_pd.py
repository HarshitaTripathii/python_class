import pandas as pd
import numpy as np
df=pd.DataFrame([[2,4],[5,25],[3,9]],columns=["A","B"],index=['x','y','z'])
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Ella"],
    "Age": [25, 30, 35, 40, 45],
    "Score": [85, 90, 95, 80, 75]
}
# df1=pd.DataFrame(data)

'''print(type(df1["Name"].tolist()))  #list
arr=np.array(df1["Name"].tolist())
print(type(arr))   # ndarray
ind=(np.arange(arr.size)).astype(dtype=int, copy=True)
print(ind)
'''
'''#we can change the index name also  , now you canot access row by int, but by Label
df1.index=df1["Name"]
print(df1)'''

'''#dataframe can be modified also.
print(df1)
#change ageof bob to 25
array1=[i for i in df1["Name"].tolist() if i=="Bob"]  # array1=["Bob"]
# array2=df1.loc(df1["Name"]=="Bob", "Name")   #Bob
array2=df1.loc[df1["Name"]=="Bob"]
print(array2)   # full details of Bob

# answer is 
df1.loc[df1["Name"]=="Bob", "Age"]=25
print(df1.loc[df1["Name"]=="Bob"])
# print(df1)'''

# head() returns 1st 5 rows by default
#head(no.of rows from beginning)
# tail() returns last 5 rows by default
#tail(no.of rows from end)

# print(df.head(2))
# print(df.tail(2))

# print(df)  #for full table
# print(df1)

'''# accessing data from pandas below
#sample()
print(df1.sample())   #if no parameter then it return only one row
print(df1.sample(3))   #  parameter as 3, so 3 random rows
print(df1.sample(2,random_state=98))
print(df1.sample(2,random_state=98))
# If you use the same random_state, the selected indices will always remain the 
# same for both sample3 and sample4, no matter how many times you run the script. 
# This is because random_state ensures reproducibility of the random selection process.'''


'''
#loc : df.loc[list of indices]
print(df1.loc[[1,4]]) #we want row of index 1 and 4, see the [] carefully : INDIVIDAUL INDEX
print(df1.loc[2])  #only 1 row of index 2 (not in form of [])   : SINGLE INDEX
print(df1.loc[2:4, "Name"])    # SINGLE COLUMN : SLICED INDEX
print(df1.loc[2:4, ["Name","Score"]])    #SLICED INDEX : LIST OF REQUIRED COLUMNS
print(df1.loc[[1,4],"Name"])    # DATA AT INDEX 1, 4 WITH COLUMN "Name"

print(df1.loc[2,3,"Name"])  #eror : always enclose many indexes in list
print(df1.loc[2,"Name"])    #Charlie
'''

# iloc : integer location 
# loc : label location
#difference is iloc : upper index is excluded and loc : upper index is included

'''
print(df1.iloc[:,2])   #all data from column 2 i.e. Score : No need to give label name
print(df1.iloc[[2,4],[2,0]]) '''

'''# iat / at : for specific or single data : if try to give slicing , it will show error
# iat : only integers
# at :  only label 
print(df1.at[2,"Name"])
print(df1.at[2,0])  #error
print(df1.iat[0,0])  ''' 

# print(df.index.tolist())
# print(df.index)
print(df.columns.tolist())

# print(df.describe())
# infor=df.describe()
# print(type(infor))
# print(df1.describe())
# print(df1.info())

# print(df.info())

# print(df.size) # 6

# coffee=pd.read_csv("use_pack\coffee.csv")
# print(coffee.head())

# coffee=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
# go to given repository , click on raw in right top corner, copy the url, and paste as above.
# print(coffee.head())
# print(coffee.columns.tolist())
# print(coffee.index.tolist())

# df2=pd.read_parquet("use_pack\coffee.parquet",engine="pyarrow", columns=["Day","Units Sold"])  #this is wrong

'''
# Save DataFrame to a Parquet file
# run pip install pyarrow
# csv_file.to_parquet("parquet_file_name",engine="pyarrow")
coffee=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
coffee.to_parquet("coffee1.parquet",engine="pyarrow")
# coffee1.parquet will get created automatically
df2=pd.read_parquet("coffee1.parquet")
print(df2)'''

'''coffee2=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
print(coffee2)
coffee2.to_excel("coffee2.xlsx",index=False)
df3=pd.read_excel("coffee2.xlsx")
print(df3)
'''
# SORTING
'''Sorting is hierarchical: The first column is the primary sort, the second column resolves ties, and so on.
No conflicts : If no ties exist, only the first column’s sorting matters.
Tiebreakers : Secondary columns act as tiebreakers.

If both columns (Age and Score) have all unique values, and the ascending order of Age
conflicts with the descending order of Score, Pandas prioritizes the first column in the sort hierarchy.
'''
# by parameter (optional)
# print(df1)
import functools

record=[["Alice",	24,	85],["Bob",	22,	90],["Charlie",	23,	95]]
df2=pd.DataFrame(record,columns=["name","age","marks"])
print(df2)
m=df2["marks"].tolist()
sum=functools.reduce(lambda x,y:x+y,m)
avg=sum/(len(m))
print(f"the average marks is {avg}")
des=df2.describe()
maxm=des.at[max, "name"]
print(f'the max marks is with {maxm}')






