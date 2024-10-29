import requests

API_KEY = 'd78386fe'
BASE_URL = 'http://www.omdbapi.com/'

def search_movie(title):
    # parameter for the request
    params = {
        'apikey': API_KEY,
        't': title,
        'plot': 'short'  # Use 'short' for a brief summary; use 'full' for detailed summary
    }

    # Makes a request
    response = requests.get(BASE_URL, params=params)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if movie was found
        if data.get("Response") == "True":
            genre = data.get("Genre", "N/A")
            plot = data.get("Plot", "N/A")
            return {"Genre": genre, "Plot": plot}
        else:
            return "Error 404: Movie not found Nigga!"
    else:
        return "Error: Unable to fetch data from OMDb."

# this acts as the main function
if __name__ == '__main__':
    with open('logo.txt', 'r') as file:
        content = file.read()
        print(content)
    loop = True
    # this while displays the options for users to choose
    while loop:
        print('1. Find a movie/tv show/anime')
        print('2. Quit')
        arg = int(input("Enter your choice: "))
        if arg == 1:
            movie_name = input("Enter the name of movie/tv show/anime : ")
            movie_data = search_movie(movie_name)
            print(movie_data)
        elif arg == 2:
            loop = False
        else:
            print("Invalid Choice Dumbass Nigga")
