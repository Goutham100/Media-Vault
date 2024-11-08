import requests
from tmdbv3api import TMDb, Movie, Discover

# Initialize TMDb API
tmdb = TMDb()
tmdb.api_key = '09d0650e48d242f97c52f1e4f6780f98'

# Function to authenticate user
def login(username, password):
    response = requests.get("http://localhost:3000/users")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['username'] == username and user['password'] == password:
                print(f"Welcome, {username}!")
                return user['id']
        print("Invalid username or password.")
    else:
        print("Failed to connect to the user database.")
    return None

# Function to sign up a new user
def signup(username, password):
    response = requests.get("http://localhost:3000/users")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['username'] == username:
                print("Username already exists. Please choose a different username.")
                return None

        # Add new user to database
        new_user = {
            "username": username,
            "password": password
        }
        response = requests.post("http://localhost:3000/users", json=new_user)
        if response.status_code == 201:
            print(f"Account created successfully! Welcome, {username}!")
            return response.json()['id']  # Return new user's ID
        else:
            print("Failed to create a new account.")
    else:
        print("Failed to connect to the user database.")
    return None

# Function to search for a movie or TV show
def search_media(movie_):
    movie = Movie()
    try:
        search_results = movie.search(movie_)
        if not search_results:
            print("No Results")
            return
        high = 10
        if len(search_results)<10:
            high = len(search_results)
        for i in range(0, high):
            print(f"Title: {search_results[i].title}")
            print(f"Overview: {search_results[i].overview}")
            print(f"Release Date: {search_results[i].release_date}")
            print(f"Rating: {search_results[i].vote_average}")
            print()
    except Exception:
        print("No Results")

# Function to search with filters
def search_top_movies(genre_id=None, year=None, language=None, min_rating=None):
    try:
        discover = Discover()
        filters = {
            'sort_by': 'popularity.desc',
            'vote_count.gte': 100,
            'page': 1
        }
        if genre_id:
            filters['with_genres'] = genre_id
        if year:
            filters['primary_release_year'] = year
        if language:
            filters['with_original_language'] = language
        if min_rating:
            filters['vote_average.gte'] = min_rating

        search_results = discover.discover_movies(filters)
        if not search_results:
            print("No Results")
            return

        for i in range(min(10, len(search_results))):
            print(f"Title: {search_results[i].title}")
            print(f"Overview: {search_results[i].overview}")
            print(f"Release Date: {search_results[i].release_date}")
            print(f"Rating: {search_results[i].vote_average}")
            print("\n")
    except Exception:
        print("No Results")

# Function to print reviews for a specific media item
def print_reviews(media):
    # Send a GET request to retrieve reviews for the specified movie name
    response = requests.get(f"http://localhost:3000/reviews?movie_name={media}")

    if response.status_code == 200:
        reviews = response.json()
        if reviews:
            print(f"Reviews for {media}:")
            for review in reviews:
                # Use .get() to safely access dictionary keys
                user = review.get('user', 'Unknown')
                review_text = review.get('review', 'No review text available')
                rating = review.get('rating', 'No rating available')
                
                print(f"User: {user}")
                print(f"Review: {review_text}")
                print(f"Rating: {rating}")
                print("-" * 40)
        else:
            print(f"No reviews found for {media}.")
    else:
        print("Failed to fetch reviews.")
def add_review(movie_name, user, review_text, rating):
    url = "http://localhost:3000/reviews"

    # Define the new review data as a dictionary
    new_review = {
        "movie_name": movie_name,
        "user": user,
        "review": review_text,
        "rating": rating
    }

    # Send a POST request to add the new review
    response = requests.post(url, json=new_review)

    # Check if the request was successful
    if response.status_code == 201:
        print("Review added successfully!")
    else:
        print("Failed to add review.")


# Main program
if __name__ == '__main__':
    logged_in_user_id = None
    # Login or Signup Prompt
    while not logged_in_user_id:
        print("\n1. Login")
        print("2. Sign Up")
        choice = input("Select an option (1 or 2): ")

        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if choice == "1":
            logged_in_user_id = login(username, password)
        elif choice == "2":
            logged_in_user_id = signup(username, password)
        else:
            print("Invalid option. Please choose 1 for Login or 2 for Sign Up.")

    # Main Menu
    loop = True
    while loop:
        print("\nMenu Options:")
        print("1. Search for a movie/TV show/anime")
        print("2. Search with filters")
        print("3. View reviews for a movie")
        print("4. Write Reviews")
        print("5. Quit")

        try:
            arg = int(input("Enter your option: "))
            
            if arg == 1:
                media = input("Enter the movie name: ")
                search_media(media)

            elif arg == 2:
                genre_id = input("Enter genre ID (or leave blank): ").strip()
                year = input("Enter release year (or leave blank): ").strip()
                language = input("Enter language code (e.g., 'en' for English, or leave blank): ").strip()
                min_rating = input("Enter minimum rating (0-10, or leave blank): ").strip()

                genre_id = int(genre_id) if genre_id else None
                year = int(year) if year else None
                language = language if language else None
                min_rating = float(min_rating) if min_rating else None

                search_top_movies(genre_id=genre_id, year=year, language=language, min_rating=min_rating)

            elif arg == 3:
                media = input("Enter the movie name to view reviews: ")
                print(f"The reviews for {media}: ")
                print_reviews(media)
            elif arg == 4:
                media = input("Enter the movie you want to review: ")
                user = username
                review_text = input("Enter your review: ")
                rating = input("Enter your rating: ")
                add_review(media, user, review_text, rating)
            elif arg == 5:
                loop = False
                print("Goodbye!")
            else:
                print("Invalid Option")

        except ValueError:
            print("Please enter a valid number.")
