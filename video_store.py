MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
  title = input('Enter the movie title: ')
  director = input('Enter the movie director: ')
  year = input('Enter the movie release year: ')

  movies.append({
      'title': title,
      'director': director,
      'year': year
  })


def list_movie():
  for movie in movies:
    print_movie(movie)


def find_movie():
  search_title = input('Enter a movie title: ')

  for movie in movies:
    if search_title == movie['title']:
      print_movie(movie)
    else:
      print('Movie not found!')


def print_movie(movie):
  print("-------------------------------------------")
  print(f"Title: {movie['title']}")
  print(f"Director: {movie['director']}")
  print(f"Release year: {movie['year']}")
  print("-------------------------------------------")


options = {
  'a': add_movie,
  'l': list_movie,
  'f': find_movie
}


def menu():
  selection = input(MENU_PROMPT)
  
  while selection != 'q':
    if selection in options:
      execution = options[selection]
      execution()
    else:
      print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


menu()