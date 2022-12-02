from imdb import Cinemagoer

#Create Cinemagoer Instance and text file to write to in append mode
ia = Cinemagoer()
file = open("IMDB_input.sql", "w")

#Get the top 250 movies, bottom 100 movies, and top 250 shows respectively
topMovies = ia.get_top250_movies()
bottomMovies = ia.get_bottom100_movies()
topShows = ia.get_top250_tv()

#Create the SQL statements for the topMovies and Crew
for mov in range(5):
    #Precisely selects the movie, writer, director, and cast
    movie = ia.get_movie(topMovies[mov].movieID)
    writer = ia.get_person(movie['writer'][0].personID)
    director = ia.get_person(movie['director'][0].personID)
    cast = (movie['cast'])

#create null variables if data isn't found
    try:
        budget = ''.join(c for c in movie['box office']['Budget'] if c.isnumeric())
    except KeyError:
        budget = 'NULL'
    
    #Create the SQL statement to insert into media
    out = "INSERT\nINTO Media(TitleID, Name, Rating, Budget, Synopsis, Country)\nVALUES(" + movie.movieID + ", \'" + movie['title'] + "\', \'" + str(movie['rating']) + "\', " + budget + ", \'" + str(movie['plot'][0]) + "\', \'"+ str(movie["countries"][0]) + "\');\n\n"
    file.write(out)

    #create the SQL statement to insert genre
    for genre in movie['genres']:
        out = "INSERT\nINTO Genre(Genre_MediaID, GenreName)\nVALUES(" + movie.movieID + "," + genre + ");\n\n"
        file.write(out)

    #create the SQL statement to insert languages
    for language in movie['languages']:
        out = "INSERT\nINTO Languages(Language_MediaID, LanguageName)\nVALUES(" + movie.movieID + ", \'" + language + "\');\n\n"
        file.write(out)

    #create the SQL statement to insert movie
    out = "INSERT\nINTO Movie(MovieID, Runtime)\nVALUES(" + movie.movieID + "," + ''.join(c for c in movie['runtime'] if c.isnumeric()) + ");\n\n"
    file.write(out)

#Insert the crew into people
    #Insert Writer into person
    try:
        writerDOB = writer["birth date"]
    except KeyError:
        writerDOB = "NULL"
    out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(\'" + str(movie['writer'][0]) + "\', " + "\'CONTACT\'" + ", " + writerDOB + ", " + str(0b100) + ");\n\n"
    file.write(out)

    #Insert Writer into Wrote
    out = "INSERT\nINTO Wrote(Writer_Name, Wrote_MediaID)\nVALUES(\'" + str(movie['writer'][0]) + "\', " + movie.movieID + ");\n\n"
    file.write(out)    

    #Insert Director into Person 
    try:
        directorDOB = director["birth date"]
    except KeyError:
        directorDOB = "NULL"       
    out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(\'" + str(movie['director'][0]) + "\', " + "CONTACT" + ", " + directorDOB + ", " + str(0b010) + ");\n\n"
    file.write(out)

    #Insert Director into Directed
    out = "INSERT\nINTO Directed(Director_Name, Directed_MediaID)\nVALUES(\'" + str(movie['director'][0]) + "\', " + movie.movieID + ");\n\n"
    file.write(out)

    #Insert top cast members
    for i in range(2):
        actor = ia.get_person(cast[i].personID)

        #Insert Actor into Person
        try:
            actorDOB = actor["birth date"]
        except KeyError:
            actorDOB = "NULL"  
        out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(\'" + str(cast[i]) + "\', " + "\'CONTACT\'" + ", " + actorDOB + ", " + str(0b001) + ");\n\n"
        file.write(out)

        #Insert Actor into Acted
        out = "INSERT\nINTO Acted(Actor_Name, Acted_MediaID)\nVALUES(\'" + str(cast[i]) + "\', " + movie.movieID + ");\n\n"
        file.write(out)
print("Top Movies and Crew Written\n")

#Create the SQL statements for the bottomMovies and Crew
for mov in range(5):
    #Precisely selects the movie from the list
    movie = ia.get_movie(bottomMovies[mov].movieID)
    writer = ia.get_person(movie['writer'][0].personID)
    director = ia.get_person(movie['director'][0].personID)
    cast = (movie['cast'])

    #Create the SQL statement to insert into media
    try:
        budget = ''.join(c for c in movie['box office']['Budget'] if c.isnumeric())
    except KeyError:
        budget = 'NULL'
    out = "INSERT\nINTO Media(TitleID, Name, Rating, Budget, Synopsis, Country)\nVALUES(" + movie.movieID + ", \'" + movie['title'] + "\', \'" + str(movie['rating']) + "\', " + budget + ", \'" + str(movie['plot'][0]) + "\', \'"+ str(movie["countries"][0]) + "\');\n\n"
    file.write(out)

    #create the SQL statement to insert genre
    for genre in movie['genres']:
        out = "INSERT\nINTO Genre(Genre_MediaID, GenreName)\nVALUES(" + movie.movieID + ",\'" + genre + "\');\n\n"
        file.write(out)

    #create the SQL statement to insert languages
    for language in movie['languages']:
        out = "INSERT\nINTO Languages(Language_MediaID, LanguageName)\nVALUES(" + movie.movieID + ",\'" + language + "\');\n\n"
        file.write(out)

    #create the SQL statement to insert movie
    out = "INSERT\nINTO Movie(MovieID, Runtime)\nVALUES(" + movie.movieID + "," + ''.join(c for c in movie['runtime'] if c.isnumeric()) + ");\n\n"
    file.write(out)

#Insert the crew into people
    #Insert WRiter into person
    try:
        writerDOB = writer["birth date"]
    except KeyError:
        writerDOB = "NULL"
    out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(\'" + str(movie['writer'][0]) + "\', " + "\'CONTACT\'" + ", " + writerDOB + ", " + str(0b100) + ");\n\n"
    file.write(out)

    #Insert Writer into Wrote
    out = "INSERT\nINTO Wrote(Writer_Name, Wrote_MediaID)\nVALUES(\'" + str(movie['writer'][0]) + "\', " + movie.movieID + ");\n\n"
    file.write(out)    

    #Insert Director into Person 
    try:
        directorDOB = director["birth date"]
    except KeyError:
        directorDOB = "NULL"        
    out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(\'" + str(movie['director'][0]) + "\', " + "\'CONTACT\'" + ", " + directorDOB + ", " + str(0b010) + ");\n\n"
    file.write(out)

    #Insert Director into Directed
    out = "INSERT\nINTO Directed(Director_Name, Directed_MediaID)\nVALUES(\'" + str(movie['director'][0]) + "\', " + movie.movieID + ");\n\n"
    file.write(out)

    #Insert top cast members
    for i in range(2):
        actor = ia.get_person(cast[i].personID)

        #Insert Actor into Person
        try:
            actorDOB = actor["birth date"]
        except KeyError:
            actorDOB = "NULL"
        out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES\'(" + str(cast[i]) + "\', " + "\'CONTACT\'" + ", " + actorDOB + ", " + str(0b001) + ");\n\n"
        file.write(out)

        #Insert Actor into Acted
        out = "INSERT\nINTO Acted(Actor_Name, Acted_MediaID)\nVALUES(\'" + str(cast[i]) + "\', " + movie.movieID + ");\n\n"
        file.write(out)
print("Bottom Movies and Crew Written\n")

#Create the SQL statements for the topShows and Crew
for sho in range(5):
    #Precisely selects the movie from the list
    show = ia.get_movie(topShows[sho].movieID)

    ia.update(show, 'episodes')
    episode = ia.get_movie(show['episodes'][1][1].movieID)
    
    #create null variables if data isn't found
    try:
        budget = ''.join(c for c in show['box office']['Budget'] if c.isnumeric())
    except KeyError:
        budget = 'NULL'
    
    #Create the SQL statement to insert into table
    out = "INSERT\nINTO Media(TitleID, Name, Rating, Budget, Synopsis, Country)\nVALUES(" + show.movieID + ", \'" + show['title'] + "\', \'" + str(show['rating']) + "\', " + budget + ", \'" + str(show['plot'][0]) + "\', " + str(show["countries"][0]) + "\')\n\n"
    file.write(out)

    #Create the SQL statement to insert into genre
    for genre in movie['genres']:
        out = "INSERT\nINTO Genre(Genre_MediaID, GenreName)\nVALUES(" + show.movieID + "," + genre + ");\n\n"
        file.write(out)

    #create the SQL statement to insert languages
    for language in movie['languages']:
        out = "INSERT\nINTO Languages(Language_MediaID, LanguageName)\nVALUES(" + show.movieID + ", \'" + language + "\');\n\n"
        file.write(out)
#Insert the crew into people
    #Insert Writer into person
    
    try:
        writer = ia.get_person(show['writer'][0].personID)

        try:
            writerDOB = writer["birth date"]
        except KeyError:
            writerDOB = "NULL"
        out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(" + str(show['writer'][0]) + ", " + "CONTACT" + ", " + writerDOB + ", " + str(0b100) + ");\n\n"
        file.write(out)

        #Insert Writer into Wrote
        out = "INSERT\nINTO Wrote(Writer_Name, Wrote_MediaID)\nVALUES(" + str(show['writer'][0]) + ", " + show.movieID + ");\n\n"
        file.write(out)    
    except KeyError:
        pass

    try:
        director = ia.get_person(show['director'][0].personID)

        #Insert Director into Person        
        out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(" + str(show['director'][0]) + ", " + "CONTACT" + ", " + director['birth date'] + ", " + str(0b010) + ");\n\n"
        file.write(out)

        #Insert Director into Directed
        out = "INSERT\nINTO Directed(Director_Name, Directed_MediaID)\nVALUES(" + str(show['director'][0]) + ", " + show.movieID + ");\n\n"
        file.write(out)
    except KeyError:
        pass

    #Insert top cast members
    for i in range(2):
        try:
            cast = (show['cast'])
            actor = ia.get_person(cast[i].personID)

            #Insert Actor into Person
            out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(" + str(cast[i]) + ", " + "CONTACT" + ", " + actor['birth date'] + ", " + str(0b001) + ");\n\n"
            file.write(out)

            #Insert Actor into Acted
            out = "INSERT\nINTO Acted(Actor_Name, Acted_MediaID)\nVALUES(" + str(cast[i]) + ", " + show.movieID + ");\n\n"
            file.write(out)
        except KeyError:
            pass
print("Top Shows Written\n")

#Close the file when complete with the statements
file.close()