import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

#this codelines will expand the output (show us all the columns)
pd.options.display.max_columns = None
pd.options.display.width = None
df = pd.ExcelWriter_csv(w"Minning-1.csv")
print(df.head(120))
sns.scatterplot(x="local_employment_percentage", y="profit", data=df)
plt.show()
