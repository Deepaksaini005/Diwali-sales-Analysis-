# %matplotlib inline
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# to open  the graph in same window 
# inline = inside notebook line /output

df = pd.read_csv(r"C:\Users\saini\Downloads\Diwali Sales Data.csv" , encoding = 'unicode_escape')
#utf-8
#latin1
#unicode_escape

# print(df.head())  
# print(df.tail())
# print(df.shape)


drop_columns =df.drop(["Status", "unnamed1"] ,axis =1 , inplace = False )   # inplace = False is used to create a new dataframe after dropping the columns
print(drop_columns)

data = pd.isnull(drop_columns).sum()  #  is null is used to find the null values in the column
print(data)

drop_Amount = drop_columns.dropna( subset = ["Amount"] , inplace = False) # dropna is used to drop the null values from the column
print(drop_Amount)


# chnage the name of the Amount column to Sales Amount
data= drop_Amount.rename( columns = {"Amount" : "Sales Amount"} , inplace = False)   #rename is used to change the name of column
print(data)

# chnage the datatype of Sales Amount column to int
data["Sales Amount"] = data["Sales Amount"].astype("int")  # astype is used to change the datatype of column
print(data.dtypes)

print(data.describe())  # describe is used to get the statistical data of the column



# bar chart for the Gander column and the count of the Gander column
gender_counts = data["Gender"].value_counts()
c=["blue" , "yellow"]  # color for the bar chart
plt.bar(gender_counts.index, gender_counts.values , color=c)  #  index is used to get the index of the column and values is used to get the values of the column
plt.xlabel("Gender" )
plt.ylabel("Count")
plt.title("Count of Each Gender")

for i , v in enumerate(gender_counts.values):
    plt.text(i, v + 10 , str(v) , ha = 'center' , fontsize = 10 )  # ha is used to align the text in the center and fontsize is used to change the size of the text
    
plt.legend(["F","M"] , title = "Gender")  # legend is used to add the legend to the graph and title is used to add the title to the legend
plt.show()


# Using the seaborn create a graph for the age , gender (1 male ke liye  ) and ek  female ke liye graph banao

ax = sns.countplot(data=df, x = "Age Group", hue = "Gender")

for i in ax.containers:
    ax.bar_label(i)
    
plt.show()


# Total Amount vs Age Group.
sns.barplot(data = data , x = "Sales Amount" , y = "Age Group" , estimator=np.sum)  # estimator is used to get the sum of the values in the column
plt.show()


# Total number of orders from top 10 states 
top_states =  data["State"].value_counts().head(10)
print(top_states)

sns.barplot(x = top_states.index , y = top_states.values )
plt.xlabel("State")
plt.ylabel("Number of Orders")
plt.title("Top 10 States by Number of Orders")
plt.xticks(rotation = 30 )  # xticks is used to rotate the x-axis labels
plt.show()



# Weather the customer is Married or Not.
marital_status = data["Marital_Status"].value_counts()
print(marital_status)

sns.barplot(
    x=marital_status.index,
    y=marital_status.values , palette = ["red", "yellow"], legend=True
)

plt.title("Marital Status of Customers")
plt.xlabel("Marital Status")
plt.ylabel("Count")
plt.legend(" Marital status")
plt.show()


# Their proffession .
Occupation_counts= data["Occupation"].value_counts()
print(Occupation_counts)









