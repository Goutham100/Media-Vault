# MediaVault
MediaVault is a Python-based application that allows users to search for movies, TV shows, or anime using TMDb’s API, filter searches by genre, release year, language, and rating, and view user reviews with searching and sorting using BinarySearchTrees(BST). The application also provides user authentication to enable login and signup functionality.  

This is the DSA project of III Sem Cyber Physical Systems Engineering Students of MIT,Manipal.  
## Table of Contents
- [Features](https://github.com/Goutham100/Media-Vault/blob/main/README.md#features)
- [Installation](https://github.com/Goutham100/Media-Vault/blob/main/README.md#installation)
- [Usage](https://github.com/Goutham100/Media-Vault/blob/main/README.md#usage)
- [API Details](https://github.com/Goutham100/Media-Vault/blob/main/README.md#api-details)
- [Contributing](https://github.com/Goutham100/Media-Vault/blob/main/README.md#contributing)
- [License](https://github.com/Goutham100/Media-Vault/blob/main/README.md#license)
## Features
- User Authentication: Users can log in or sign up using locally stored credentials.  
- Search Movies/TV Shows/Anime: Search for movies, TV shows, or anime by title.  
- Filter Movies: Search movies with advanced filters like genre, release year, language, and minimum rating.  
- View Reviews: View user-submitted reviews for specific movies via sorting and searching based on Rating with Binary Search Trees.  

## Installation
Clone the repository:  
```
git clone https://github.com/Goutham100/Media-Vault.git
cd media_vault
```
Make sure you have Python installed. Then, install the required dependencies:  
```
pip install requests tmdbv3api
```
Sign up on The Movie Database (TMDb) to obtain an API key and replace it in the ```tmdb.api_key``` section in the code:  
```
tmdb.api_key = 'tmdb_api_key'
```
Start JSON Server (for user authentication and review management):  

Install JSON Server to simulate the backend server:  
```
npm install -g json-server
json-server --watch db.json --port 3000
```
Database Setup: Ensure db.json is properly formatted with initial data. Here's a sample structure:  
```
{
  "users": [
    { "id": 1, "username": "testuser", "password": "password123" }
  ],
  "reviews": [
    { "movie_name": "Inception", "user": "testuser", "review": "Great movie!", "rating": "9.0" }
  ]
}
```
## Usage
Run the script in your terminal:  
```
python main.py
```
- Log In or Sign Up: Select an option to log in if you already have an account or sign up to create a new one.
- Search Options: After logging in, you’ll be presented with the main menu:  
  Search for a Movie/TV Show/Anime: Enter the title of the media item you want to search for.
- Search with Filters: Use filters like genre ID, release year, language, and minimum rating.
- View User Reviews: Enter the searching and sorting condition and view the user review.
- Quit: Exit the application.
## API Details
The application uses the TMDb API to fetch movie information:  

API Key: Required for TMDb.  
Endpoints:  
`Movie().search()`: Used for basic title searches.  
`Discover().discover_movies()`: Used for advanced search with filters.  
## Contributing
Contributions are welcome! Here’s how you can help:  

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Open a pull request with a description of the changes.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.  


