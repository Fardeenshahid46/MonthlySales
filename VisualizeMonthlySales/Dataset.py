import pandas as pd

sales={
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Sales":[2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000]
}
df=pd.DataFrame(sales)
df.to_csv("sales.csv",index=False)
print("CSV file created")