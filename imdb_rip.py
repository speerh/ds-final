from imdb import Cinemagoer

#Create Cinemagoer Instance and text file to write to in append mode
ia = Cinemagoer()
file = open("IMDB_input.sql", "w")

#Get the top 250 movies, bottom 100 movies, and top 250 shows respectively
topMovies = ia.get_top250_movies()
bottomMovies = ia.get_bottom100_movies()
topShows = ia.get_top250_tv()

#Add a set number of topMovies to the input file
#This variable is the hard limit for adding movies (change in the fucntion)
topLimit = 0
for mov in topMovies:
    #Precisely selects the movie from the list
    movie = ia.get_movie(mov.movieID)

    #Create the SQL statement to insert into table
    out = "INSERT\nINTO Media(TitleID, Name, Rating, Budget, Synopsis, Country)\nVALUES(" + movie.movieID + ", " + movie['title'] + ", " + str(movie['rating']) + ", " + ''.join(c for c in movie['box office']['Budget'] if c.isnumeric()) + ", " + str(movie['plot'][0]) + str(movie["countries"][0]) + ")\n\n"
    file.write(out)

    #Sets the topMovie Limit
    topLimit += 1
    if topLimit >= 2:
        print("Top Movies Written\n")
        break

#Add a set number of bottomMovies to the input file
#This variable is the hard limit for adding movies (change in the fucntion)
bottomLimit = 0
for mov in bottomMovies:
    #Precisely selects the movie from the list
    movie = ia.get_movie(mov.movieID)

    #Create the SQL statement to insert into table
    out = "INSERT\nINTO Media(TitleID, Name, Rating, Budget, Synopsis, Country)\nVALUES(" + movie.movieID + ", " + movie['title'] + ", " + str(movie['rating']) + ", " + ''.join(c for c in movie['box office']['Budget'] if c.isnumeric()) + ", " + str(movie['plot'][0]) + str(movie["countries"][0]) + ")\n\n"
    file.write(out)

    #Sets the bottomMovie Limit
    bottomLimit += 1
    if bottomLimit >= 2:
        print("Bottom Movies Written\n")
        break

#Add a set number of topShows to the input file
#This variable is the hard limit for adding shows (change in the fucntion)
showLimit = 0
for sho in topShows:
    #Precisely selects the movie from the list
    show = ia.get_movie(sho.movieID)

    #Create the SQL statement to insert into table
    out = "INSERT\nINTO Media(TitleID, Name, Rating, Budget, Synopsis, Country)\nVALUES(" + show.movieID + ", " + show['title'] + ", " + str(show['rating']) + ", " + ''.join(c for c in movie['box office']['Budget'] if c.isnumeric()) + ", " + str(show['plot'][0]) + str(show["countries"][0]) + ")\n\n"
    file.write(out)

    #Sets the topShow Limit
    showLimit += 1
    if showLimit >= 2:
        print("Top Shows Written\n")
        break

#Close the file when complete with the statements
file.close()