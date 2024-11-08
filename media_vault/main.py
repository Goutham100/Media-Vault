import requests
from tmdbv3api import TMDb, Movie, Discover

# Initialize TMDb API
tmdb = TMDb()
tmdb.api_key = '09d0650e48d242f97c52f1e4f6780f98'

# BST Node for Review
class ReviewNode:
    def __init__(self, rating, review):
        self.rating = rating
        self.review = review
        self.left = None
        self.right = None

# BST for storing and sorting reviews by rating
class ReviewBST:
    def __init__(self):
        self.root = None

    # Insert review into BST based on rating
    def insert(self, rating, review):
        if not self.root:
            self.root = ReviewNode(rating, review)
        else:
            self._insert_recursive(self.root, rating, review)

    def _insert_recursive(self, node, rating, review):
        if rating < node.rating:
            if node.left is None:
                node.left = ReviewNode(rating, review)
            else:
                self._insert_recursive(node.left, rating, review)
        else:
            if node.right is None:
                node.right = ReviewNode(rating, review)
            else:
                self._insert_recursive(node.right, rating, review)

    # In-order traversal to get sorted reviews from lowest to highest
    def in_order_traversal(self):
        sorted_reviews = []
        self._in_order_recursive(self.root, sorted_reviews)
        return sorted_reviews

    def _in_order_recursive(self, node, sorted_reviews):
        if node:
            self._in_order_recursive(node.left, sorted_reviews)
            sorted_reviews.append(node.review)
            self._in_order_recursive(node.right, sorted_reviews)

    # Filtered traversal to get reviews with rating >= min_rating
    def filter_by_min_rating(self, min_rating):
        filtered_reviews = []
        self._filter_recursive(self.root, min_rating, filtered_reviews)
        return filtered_reviews

    def _filter_recursive(self, node, min_rating, filtered_reviews):
        if node:
            if node.rating >= min_rating:
                filtered_reviews.append(node.review)
            self._filter_recursive(node.left, min_rating, filtered_reviews)
            self._filter_recursive(node.right, min_rating, filtered_reviews)

# Function to get reviews by a specific user and insert them into a BST
def get_user_reviews(username, min_rating=None):
    response = requests.get(f"http://localhost:3000/reviews?user={username}")
    if response.status_code == 200:
        reviews = response.json()
        if reviews:
            review_bst = ReviewBST()
            for review in reviews:
                try:
                    rating = float(review.get('rating', 0))
                    review_bst.insert(rating, review)
                except ValueError:
                    print("Invalid rating format. Skipping review.")
                    continue

            if min_rating is not None:
                print(f"Reviews by {username} with rating >= {min_rating}:")
                filtered_reviews = review_bst.filter_by_min_rating(min_rating)
                if filtered_reviews:
                    for review in filtered_reviews:
                        print_review_details(review)
                else:
                    print(f"No reviews found by {username} with rating >= {min_rating}.")
            else:
                print(f"All reviews by {username} (sorted by rating from lowest to highest):")
                sorted_reviews = review_bst.in_order_traversal()
                for review in sorted_reviews:
                    print_review_details(review)
        else:
            print(f"No reviews found by {username}.")
    else:
        print("Failed to fetch reviews.")

# Helper function to print review details
def print_review_details(review):
    movie_name = review.get('movie_name', 'Unknown')
    review_text = review.get('review', 'No review text available')
    rating = review.get('rating', 'No rating available')
    print(f"Movie: {movie_name}")
    print(f"Review: {review_text}")
    print(f"Rating: {rating}")
    print("-" * 40)

# Placeholder login function
def login(username, password):
    if username and password:
        return username  # Returning username as a stand-in for user ID
    else:
        print("Invalid login credentials.")
        return None

# Placeholder signup function
def signup(username, password):
    if username and password:
        print(f"User {username} registered successfully.")
        return username
    else:
        print("Sign-up failed. Please provide both username and password.")
        return None

# Main program
if __name__ == '__main__':
    logged_in_user_id = None
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
        print("4. View your reviews")
        print("5. Write a review")
        print("6. Quit")
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
                print_reviews(media)
            elif arg == 4:
                print("1. View all your reviews (sorted by rating, lowest to highest)")
                print("2. View reviews with rating more than or equal to a specific rating")
                try:
                    review_option = int(input("Enter your choice (1 or 2): "))
                    if review_option == 1:
                        get_user_reviews(username)
                    elif review_option == 2:
                        min_rating = float(input("Enter the minimum rating to filter by: "))
                        get_user_reviews(username, min_rating)
                    else:
                        print("Invalid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif arg == 5:
                media = input("Enter the movie you want to review: ")
                review_text = input("Enter your review: ")
                rating = input("Enter your rating: ")
                add_review(media, username, review_text, rating)
            elif arg == 6:
                loop = False
                print("Goodbye!")
            else:
                print("Invalid Option")
        except ValueError:
            print("Invalid input. Please enter a number.")
