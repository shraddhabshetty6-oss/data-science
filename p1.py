import os
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "Dataset for Data Analytics.xlsx")

df = pd.read_excel(file_path)

print("First 5 Rows")
print(df.head())
print("\nDataset shape")
print(df.shape)
print("\ncolumn names")
print(df.columns.tolist())
print("\nMissing values")
print(df.isnull().sum())
print("\nstatistical summary")
print(df.describe())
# Handled missing values in coupon code
df["CouponCode"] = df["CouponCode"].fillna(" No coupon ")
print("\nMissing values after handling")
print(df.isnull().sum())
# Outlier detection using IQR
Q1 =df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
outliers = df[(df["TotalPrice"] < lower_limit) | (df["TotalPrice"] > upper_limit)]
print("\nOutliers in Total Price")
print(len(outliers))
df=df[(df["TotalPrice"] >= lower_limit) & (df["TotalPrice"] <= upper_limit)]
print("\nDataset shape after  outlier handling")
print(df.shape)
#3.FEATURE ENGINEERING
#Feature 1: price per item
df["PricePerItem"] = df["TotalPrice"] / df["Quantity"]
df["Average cart value"] = df["TotalPrice"] / df["ItemsInCart"]
df["OrderMonth"] = pd.to_datetime(df["Date"]).dt.month
print("\nNEW FEATURES:")
print(df[["PricePerItem", "Average cart value", "OrderMonth"]].head())
#4 final check
print("\nFINAL COLUMNS")
print(df.columns.tolist())
print("\nFINAL DATASET SHAPE")
print(df.shape)
#5 Save the cleaned and feature-engineered dataset to a new Excel file
Output_file_path = os.path.join(os.path.dirname(__file__), "Cleaned_Dataset.xlsx")
df.to_excel(Output_file_path, index=False)
print("\nPROJECT 1 COMPLETED SUCCESSFULLY!")
print("Cleaned dataset saved as:") 
print(Output_file_path)