
from tmdbv3api import TMDb, Movie, Discover

tmdb = TMDb()                                                  # this is the api key
tmdb.api_key = '09d0650e48d242f97c52f1e4f6780f98'

def search_media(movie_):  # this function searches for the movies
    movie = Movie()

    try:
        search_results = movie.search(movie_)

        if not search_results:
            print("No Results")

        print(f"Title: {search_results[0].title}")
        print(f"Overview: {search_results[0].overview}")
        print(f"Release Date: {search_results[0].release_date}")
        print(f"Rating: {search_results[0].vote_average}")
        print()
    except Exception as e:
        print("No Results")
def search_top_movies(genre_id=None, year=None, language=None, min_rating=None):

    try:
        discover = Discover()
    # Set filters for discover function
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

        # Fetch results
        search_results = discover.discover_movies(filters)

        high = 10
        if len(search_results)<10:
            high = len(search_results)
        for i in range(0,high): # Display the top 10 results

            print(f"Title: {search_results[i].title}")
            print(f"Overview: {search_results[i].overview}")
            print(f"Release Date: {search_results[i].release_date}")
            print(f"Rating: {search_results[i].vote_average}")
            print("\n")
    except Exception as e:
        print("No Results")


if __name__ == '__main__':
    with open('logo.txt', 'r') as file:
        content = file.read()
        print(content)
    loop = True
    while(loop): # main loop
        print("1. Search for a movie/tv show/anime")
        print("2. Search with filters")
        print("3. Quit")

        try:
            arg = int(input("Enter your option: "))
            if arg == 1:
                media = input("Enter the movie: ")
                search_media(media)
            elif arg == 2:
                genre_id = input("Enter genre ID (or leave blank): ").strip()
                year = input("Enter release year (or leave blank): ").strip()
                language = input("Enter language code (e.g., 'en' for English, or leave blank): ").strip()
                min_rating = input("Enter minimum rating (0-10, or leave blank): ").strip()

            # Convert inputs as needed
                genre_id = int(genre_id) if genre_id else None
                year = int(year) if year else None
                language = language if language else None
                min_rating = float(min_rating) if min_rating else None

                search_top_movies(genre_id=genre_id, year=year, language=language, min_rating=min_rating)
            elif arg == 3:
                loop = False
            else:
                print("Invalid Option")
        except ValueError:
            print("must be a number")