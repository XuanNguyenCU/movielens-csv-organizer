# Xuan Nguyen 101228417

#-------------------------------------------------------------------
def display_list(list2D):
    '''displays elements of a 2-D list on separate lines
        input: a 2-D list
        return: None
    '''
    if len(list2D) == 0:
        print("No data in the list")
    for row in list2D:
        print(row)

#-------------------------------------------------------------------
def display_dict(adict):
    '''displays elements of a dictionary in sorted order of keys on separate lines
        input: a dictionary
        return: None
    '''
    if len(adict) == 0:
        print("Dictionary is empty")
    for key in sorted(adict):
        print(str(key) + ": " +str(adict[key]))

#-------------------------------------------------------------------
# functions are added here

def load_data(file1, file2, file3):
    """
    Parameters: three filenames (strings)
    Reads each of these files
    Stores data in separate 2-D lists (except the data in their header rows)
    Returns those lists   
    """

    listMovie = []
    listRate = []
    listTag = []

    try:

        with open(file1, "r") as infile1:
            for line in infile1:
                line = line.strip().split(",")
                listMovie += [line]

            # removes header line
            listMovie.pop(0)

            for movie in listMovie:
                movie[0] = int(movie[0])

    except Exception:
        print("ERROR: one or more files cannot be opened")
        listMovie = []
            
    try:
        with open(file2, "r") as infile2:
            for line in infile2:
                line = line.strip().split(",")
                listRate += [line]

            # removes header line
            listRate.pop(0)

            for rating in listRate:
                rating[0] = int(rating[0])
                rating[1] = int(rating[1])
                rating[2] = float(rating[2])
                rating[3] = int(rating[3])

    except Exception:
        print("ERROR: one or more files cannot be opened")
        listRate = []

    try:

        with open(file3, "r") as infile3:
            for line in infile3:
                line = line.strip().split(",")
                listTag += [line]

            # removes header line
            listTag.pop(0)

            for tag in listTag:
                tag[0] = int(tag[0])
                tag[1] = int(tag[1])
                tag[3] = int(tag[3])

    except Exception:
        print("ERROR: one or more files cannot be opened")
        listTag = []

    return listMovie, listRate, listTag




def get_genre_dict(list2D):
    """
    Parameter: 2D list
    Returns a dictionary:
        each {key: value} of this dictionary is {a valid genre from the list: a list of all movie ids that belong to this genre}  
    """

    genreMovie = {}

    for lists in list2D:

        listGenre = lists[2].split("|")

        for genre in listGenre:

            # every genre added as a key will be in lower case
            if genre.lower() not in genreMovie:
                genreMovie[genre.lower()] = [lists[0]]

            else:
                genreMovie[genre.lower()] += [lists[0]]

    return genreMovie


# gets correct values for each dictionary key. however, keys are not in the same order as the example output from instruction, but one of the TA says that is fine on Discord.
def get_tag_dict(list2D):
    """
    Parameter: 2D list
    Returns a dictionary:
        each {key: value} of this dictionary is {a valid tag from the list: a list of all movie ids that have been tagged with this tag}
    
    """

    dicTag = {}

    for lists in list2D:

        if lists[2] not in dicTag:
            dicTag[lists[2].lower()] = [lists[1]]

        else:
            dicTag[lists[2].lower()] += [lists[1]]

    return dicTag


def get_avg_ratings(list2D):

    """  
    Parameter: 2D list
    Returns a dictionary:
        each {key: value} of this dictionary is {a valid movie id: the average rating received by the reviewers}
    
    """

    dicRating = {}
    for lists in list2D:

        if lists[1] not in dicRating:
            count = 0
            total = 0

        total += lists[2]
        count += 1
        dicRating[lists[1]] = round(total/count, 2) # rounded to 2 decimal places, same as output examples

    return dicRating


def get_movie_dict(list2D, dicRating):
    """
    Parameter: 2D list and dictionary


    Returns a dictionary:
        each {key: value} of this dictionary is {a valid movie id: a list containing the name of movie, year it got released, and the average rating}.
    
    """

    dicMovie = {}

    for lists in list2D:

        year = int(lists[1][len(lists[1])-5 : len(lists[1]) -1 ]) # gets the year as a str and converts it into an int

        dicMovie[lists[0]] = [lists[1][ :len(lists[1])-7], year, dicRating[lists[0]]]


    return dicMovie


def find_movies(movies: dict, genres: dict, tags: dict):
    """
    Three dictionaries as parameters: movies, genres, and tags.
    Repeatedly asks the user to enter a category to view the names of the recommended movies until the user decides to quit.
    Return no value.
    
    """

    while True:

        category = input("Enter a category ['(G)enre', '(T)ag', '(R)ating', '(Y)ear'], any other input will quit the program: ")

        if category == "G" or category == "g":

            listGenre = []

            for key in genres:
                listGenre += [key]
            print("Available genres:", listGenre) # displays all categories availble to choose from

            genreChoice = input("Enter a genre: ")
        
            if genreChoice.lower() not in genres:
                print("Invalid genre, No data in the list.")

            else:
                for id in genres[genreChoice.lower()]:
                    print(movies[id][0])

        elif category == "T" or category == "t":
            tagChoice = input("Enter a tag: ")

            setTag = set()

            if tagChoice.lower() not in tags:
                print("Invalid tag, No data in the list.")

            else:
                # uses a set to remove any duplicates
                for id in tags[tagChoice.lower()]:
                    setTag.add(movies[id][0])

                for title in setTag:
                    print(title)

        elif category == "R" or category == "r":

            number = float(input("Enter a number (minimum rating) in [0-5]: "))

            # validates user input
            while not (0 <= number <= 5):
                number = float(input("Please enter a number from 0 to 5: "))

            counter = 0
            for dic in movies:
                if movies[dic][2] >= number:
                    print(movies[dic][0])
                    counter = 1

            if counter == 0: # prints this message only if there's no data
                print("No data in the list")

        elif category == "Y" or category == "y":

            year = float(input("Enter a year: "))
            counter = 0

            # validates user input
            while year < 0:
                year = float(input("Year must be a positive number, please try again. "))

            for dic in movies:
                if movies[dic][1] == year:
                    print(movies[dic][0])
                    counter = 1

            if counter == 0:
                print("No data in the list")

        else:
            print("Thank you for using the movie recommendation system.")
            break

# test your functions in main()
#-------------------------------------------------------------------
def main():
    # testing display_list()
    alist = [[1,2],[3,4],[5],[6,7]]
    display_list(alist)

    # testing display_dict()
    adict = {2:6, 7:1, 4:3, 5:"zero"}
    display_dict(adict)


    # test your functions here
    filename1 = "movies_20.csv"
    filename2 = "ratings_20.csv"
    filename3 = "tags_20.csv"

    movies_db, ratings_db, tags_db = load_data(filename1, filename2, filename3)

    display_list(movies_db[2:5])
    display_list(ratings_db[2:5])
    display_list(tags_db[2:5])
    
    genres = get_genre_dict(movies_db)
    display_dict(genres)

    tags = get_tag_dict(tags_db)
    display_dict(tags)
    
    print()
    ratings = get_avg_ratings(ratings_db)
    display_dict(ratings)
    
    movies = get_movie_dict(movies_db, ratings)
    display_dict(movies)
     
    find_movies(movies, genres, tags)    
    
    
# call main()
if __name__ == "__main__":
    main()