import pandas as pd

# Load the dataset
df = pd.read_csv("data/imdb_movies.csv")

# Drop missing values
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("data/imdb_movies.csv", index=False)

print("Data cleaning completed. Cleaned file saved as 'imdb_movies.csv'")
