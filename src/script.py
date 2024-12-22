import pandas as pd

# Load MovieLens dataset
#movies = pd.read_csv("data/movies.csv")
#ratings = pd.read_csv("data/ratings.csv")

# Load Goodreads dataset
books = pd.read_csv("data/books.csv", on_bad_lines="warn")

# Explore datasets
print("Movies:")
#print(movies.head())
print("\nBooks:")
print(books.head())
