import pandas as pd
df=pd.read_csv("student.csv")
print(df.loc[:,"gender"]) # : is used to obtain all  rows
print(df.loc[0:4,["age","city"]]) # 0:4 all the rows from 0 to 4 #df.loc used forslicing through name of the column
print(df.iloc[:,2]) # df.iloc is used to obtain through column position not name 
print(df.iloc[0:4,1])# here 0:4 mean 0 to 3 it does not go through last rown mentioned 
print(df.iloc[0,[1,2]]) # to  get data through two columns 
print(df[df["city"].isin(["delhi","lucknow"])]) # method to slice .isin
print(df.query("age>30 and gender== 'male'"))# df.query to slice 
print(df[df["age"]>30]) 
print(df[~df["age"]>30]) # not 
print(df[(df["age"]>30) & (df["gender"]=="male")])#and both have to be true
print(df[(df["age"]>30) | (df["gender"]=="male")]) # or  only one have to be true










