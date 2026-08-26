import pandas as pd
data={
    "name":["kabir","shruti","sanket","vijay","arti"],
    "maths":[78,56,87,67,99],
    "physics":[78,45,87,98,77],
    "chemistry":[78,56,99,87,76]

}
df=pd.DataFrame(data)
print(df)
print(type(df))
print(df["maths"])
print(type(df["maths"]))

