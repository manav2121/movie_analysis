import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/imdb_movies.csv")

# Plot IMDb Rating Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Rating'], bins=20, kde=True, color='blue')
plt.title('Distribution of IMDb Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Plot Top 5 Genres by Average Rating
genre_ratings = df.groupby('Genre')['Rating'].mean().sort_values(ascending=False).head(5)
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_ratings.index, y=genre_ratings.values, palette='viridis')
plt.title('Top 5 Genres by Average IMDb Rating')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.show()
