import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales.csv")
plt.plot(df["Month"],df["Sales"],marker='o',linestyle='--',color='r',linewidth=2)
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xrotations(45)
plt.grid(True)
plt.savefig("monthly_sales.png")
plt.tight_layout()
plt.show()