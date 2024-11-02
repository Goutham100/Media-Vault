
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = '09d0650e48d242f97c52f1e4f6780f98'

def search_media(movie_):
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

if __name__ == '__main__':
    with open('logo.txt', 'r') as file:
        content = file.read()
        print(content)
    loop = True
    while(loop):
        print("1. Search for a movie/tv show/anime")
        print("2. Quit")

        try:
            arg = int(input("Enter your option: "))
            if arg == 1:
                media = input("Enter the movie: ")
                search_media(media)
            elif arg == 2:
                loop = False
            else:
                print("Invalid Option")
        except ValueError:
            print("must be a number")