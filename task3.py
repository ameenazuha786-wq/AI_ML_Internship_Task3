import pandas as pd

# Load Housing dataset
df = pd.read_csv("Housing.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Check for duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Statistical summary
print("\nStatistical Summary:")
print(df.describe())
# Price distribution
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=20)
plt.xlabel("Price")
plt.ylabel("Number of Houses")
plt.title("Distribution of House Prices")
plt.show()
# Area distribution
plt.figure(figsize=(8, 5))
plt.hist(df["area"], bins=20)
plt.xlabel("Area")
plt.ylabel("Number of Houses")
plt.title("Distribution of House Area")
plt.show()
# Price vs Area
plt.figure(figsize=(8, 5))
plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price vs Area")
plt.show()
# Number of bedrooms
plt.figure(figsize=(8, 5))
plt.hist(df["bedrooms"], bins=10)
plt.xlabel("Number of Bedrooms")
plt.ylabel("Number of Houses")
plt.title("Distribution of Bedrooms")
plt.show()
# Average price by furnishing status
avg_price = df.groupby("furnishingstatus")["price"].mean()

plt.figure(figsize=(8, 5))
avg_price.plot(kind="bar")
plt.xlabel("Furnishing Status")
plt.ylabel("Average Price")
plt.title("Average House Price by Furnishing Status")
plt.xticks(rotation=0)
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price vs Area")
plt.show()
plt.figure(figsize=(8, 5))
plt.hist(df["bedrooms"], bins=6)
plt.xlabel("Number of Bedrooms")
plt.ylabel("Number of Houses")
plt.title("Distribution of Bedrooms")
plt.show()