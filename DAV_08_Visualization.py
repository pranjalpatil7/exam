import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Q Scatter plot (create or upload any suitable data set)

data1 = pd.DataFrame({
    "Math": [95, 60, 78, 45, 88, 70, 92, 55],
    "Reading": [90, 58, 80, 50, 85, 72, 94, 60]
})

sns.set_style("whitegrid")

# Matplotlib Scatter
plt.scatter(data1["Math"], data1["Reading"], color="blue")
plt.title("Matplotlib: Math vs Reading")
plt.xlabel("Math")
plt.ylabel("Reading")
plt.grid(True)
plt.show()

# Seaborn Scatter
sns.scatterplot(x="Math", y="Reading", data=data1, color="red")
plt.title("Seaborn: Math vs Reading")
plt.xlabel("Math")
plt.ylabel("Reading")
plt.show()

# data2 = pd.read_csv("StudentsPerformance.csv")

# # Matplotlib Scatter
# plt.scatter(data2["math score"], data2["reading score"], color="green")
# plt.title("Matplotlib: Student Data")
# plt.xlabel("Math Score")
# plt.ylabel("Reading Score")
# plt.show()

# # Seaborn Scatter
# sns.scatterplot(x="math score", y="reading score", data=data2, color="purple")
# plt.title("Seaborn: Student Data")
# plt.xlabel("Math Score")
# plt.ylabel("Reading Score")
# plt.show()

#Q Program - pie chart to show cars data using Matplotlib

# Cars data
cars = ["BMW", "Audi", "Tesla", "Ford", "Hyundai"]
sales = [25, 20, 15, 18, 22]

# Pie chart
plt.pie(sales, labels=cars, autopct='%1.1f%%', startangle=90)

plt.title("Car Sales Distribution")
plt.show()

# pip install pandas matplotlib seaborn
# pip install --upgrade pip
