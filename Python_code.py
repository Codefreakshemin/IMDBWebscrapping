import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Define the URL of the IMDb Top 250 page
url = "https://www.imdb.com/chart/top/"

# Add headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the page
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the web page")
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all elements that contain movie information
    movie_titles = soup.select('td.titleColumn a')
    movie_years = soup.select('td.titleColumn span.secondaryInfo')
    movie_ratings = soup.select('td.ratingColumn.imdbRating strong')
    
    # Check if we found the correct number of elements
    if len(movie_titles) == len(movie_years) == len(movie_ratings):
        print("Successfully located movie titles, years, and ratings.")
        
        # Lists to store the extracted data
        titles = [title.text for title in movie_titles]
        years = [year.text.strip('()') for year in movie_years]
        ratings = [rating.text for rating in movie_ratings]

        # Create a DataFrame
        df = pd.DataFrame({
            'Title': titles,
            'Year': years,
            'Rating': ratings
        })

        # Display the DataFrame
        print(df)

        # Define the path where the CSV file will be saved
        save_path = os.path.join('E:/GitHub/IMDBWebscrapping', 'IMDB_Top_250_Movies.csv')

        # Save the DataFrame to a CSV file
        df.to_csv(save_path, index=False)
        print(f"Data saved to {save_path}")

    else:
        print("Mismatch in the number of titles, years, and ratings found. Please inspect the elements.")

else:
    print(f"Failed to fetch the web page. Status code: {response.status_code}")
