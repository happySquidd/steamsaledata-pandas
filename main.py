import kagglehub
import pandas as pd
import os

# dpwnload the dataset
path = kagglehub.dataset_download("benjaminlundkvist/steam-sales-historical-dataset")

# create a correct path by using os
csv_path = os.path.join(path, 'steam_sales.csv')

df = pd.read_csv(csv_path)

#
# print(df.info()) # see info about the table

high_discount_df = df[df["Discount%"] <= -70.0]
result_df = high_discount_df.sort_values(by=["Rating", "Discount%"], ascending=[False, True])
# show games with highest ratings and biggest discounts
print(result_df.loc[:, ["Game Name", "Rating", "#Reviews", "Discount%", "Price (€)", "Original Price (€)", "Release Date"]].head(20))
