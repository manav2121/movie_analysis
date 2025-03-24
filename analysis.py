import pandas as pd

# Load cleaned data
df = pd.read_csv("data/imdb_movies.csv")

# Find Top 10 Movies by Rating
top_movies = df[['Movie_Title', 'Year', 'Genre', 'Rating']].sort_values(by='Rating', ascending=False).head(10)
print("Top 10 Movies by Rating:\n", top_movies)

# Find Top 5 Genres by Average Rating
genre_ratings = df.groupby('Genre')['Rating'].mean().sort_values(ascending=False).head(5)
print("Top 5 Genres by Average Rating:\n", genre_ratings)
