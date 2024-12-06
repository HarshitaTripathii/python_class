import pandas as pd
df=pd.DataFrame([[2,4],[5,25],[3,9]],columns=["A","B"],index=['x','y','z'])
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Ella"],
    "Age": [25, 30, 35, 40, 45],
    "Score": [85, 90, 95, 80, 75]
}
df1=pd.DataFrame(data)

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

#loc : df.loc[indices]
print(df1.loc[[1,4]]) #we want row at index 1 and 4, see the [] carefully

# print(df.index.tolist())
# print(df.columns.tolist())

# print(df.describe())
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


