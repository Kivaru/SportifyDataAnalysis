import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import numpy as np

# df_tracks = pd.read_csv('SpotifyFeatures.csv')

# Find Null Values Present in the Dataset.
# print(df_tracks.isnull().sum())
# print(pd.isnull(df_tracks).sum())

# We Will Now Identify the Total Number of Rows and Columns in the Dataset and Check
# the Data Type and Memory Usage.
# df_tracks.info()


# Find Ten Least Popular Songs in the Spotify Dataset.
# sorted_df = df_tracks.sort_values('popularity', ascending=False).head(10)
# print(sorted_df)

# Descriptive Statistics
# print(df_tracks.describe().transpose())

# Top Ten Popular Songs With Popularity More Than 90.
# most_popular = df_tracks.query('popularity>90', inplace=False).sort_values('popularity', ascending=False)
# print(most_popular[:10])

# # Make the Genre Column as the Index Column.
# df_tracks.set_index("genre", inplace=True)
# print(df_tracks.head())


# Plot Duration of the Songs w.r.t. different Genres using a horizontal barplot.
# plt.title("Duration of the songs in different genres")
# sb.color_palette("bright", as_cmap=True)
# sb.barplot(data=df_tracks, y='genre', x='duration_ms')
# plt.xlabel("Duration in milliseconds")
# plt.ylabel("Genres")
# plt.show()

# Find top five genres by Popularity and pot a barplot for the same.
# sb.set_style(style="darkgrid")
# plt.figure(figsize=(10, 5))
# famous = df_tracks.sort_values("popularity", ascending=False).head(10)
# sb.barplot(y="genre", x="popularity", data=famous).set(title="Top 5 Genres by Popularity")
# plt.show()
