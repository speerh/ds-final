from imdb import Cinemagoer

#Create Cinemagoer Instance and text file to write to in append mode
ia = Cinemagoer()
file = open("IMDB_input.sql", "w")

#Get the top 250 movies, bottom 100 movies, and top 250 shows respectively
print("Fetching top 250 movies")
topMovies = ia.get_top250_movies()
print("Fetching bottom 100 movies")
bottomMovies = ia.get_bottom100_movies()
print("Fetching top 250 shows")
topShows = ia.get_top250_tv()
print("Done!")

def formatSanitary(text, *args, **kwargs):
    return text.replace("'", "&sq;").format(*args, **kwargs).replace("'","''").replace("&sq;","'")

#region SQL templates

mediaInsert = """
INSERT
INTO MEDIA (TitleID, Name, Rating, Budget, Synopsis, Country)
VALUES ({titleID}, '{name}', '{rating}', {budget}, '{synopsis}', '{country}');

"""

genreInsert = """
INSERT
INTO Genre(Genre_MediaID, GenreName)
VALUES({titleID}, '{genre}');

"""

langInsert = """
INSERT
INTO Languages(Language_MediaID, LanguageName)
VALUES({titleID}, '{lang}');

"""

movieInsert = """
INSERT
INTO Movie(MovieID, Runtime)
VALUES({titleID}, {runtime});

"""

personInsert = """
INSERT
INTO Person(PersonName, Contact, DOB, RoleFlags)
VALUES('{name}', '{contact}', DATE '{dob}', {roleFlags});

"""

wroteInsert = """
INSERT
INTO Wrote(Writer_Name, Wrote_MediaID)
VALUES('{name}', {titleID});

"""

directedInsert = """
INSERT
INTO Directed(Director_Name, Directed_MediaID)
VALUES('{name}', {titleID});

"""

actedInsert = """
INSERT
INTO Acted(Actor_Name, Acted_MediaID)
VALUES('{name}', {titleID});

"""

#endregion

# Create the SQL statements for the topMovies/bottomMovies and Crew
# because we don't need two giant loops for this!
for mov in topMovies[:5] + bottomMovies[:5]:
    #Precisely selects the movie, writer, director, and cast
    movie = ia.get_movie(mov.movieID)
    writer = ia.get_person(movie['writer'][0].personID)
    director = ia.get_person(movie['director'][0].personID)
    cast = (movie['cast'])

#create null variables if data isn't found
    budget_nosan = movie.get('box office', {}).get('Budget', 'NULL')
    budget = ''.join(c for c in budget_nosan if c.isnumeric())
    
    #create a plot variable to remove ' from the plot variable
    movPlot = str(movie['plot'][0]).replace("'", "''")

    #Create the SQL statement to insert into media
    out = formatSanitary(
        mediaInsert,
        titleID = movie.movieID,
        name = movie['title'],
        rating = str(movie['rating']),
        budget = budget,
        synopsis = str(movie['plot'][0]),
        country = str(movie["countries"][0])   
    )
    
    file.write(out)

    #create the SQL statement to insert genre
    for genre in movie['genres']:
        out = formatSanitary(
            genreInsert,
            titleID = movie.movieID,
            genre = genre
            )
        file.write(out)

    #create the SQL statement to insert languages
    for language in movie['languages']:
        out = formatSanitary(
            langInsert,
            titleID = movie.movieID,
            lang = language
            )
        file.write(out)

    #create the SQL statement to insert movie
    out = formatSanitary(
        movieInsert,
        titleID = movie.movieID,
        runtime = ''.join(c for c in movie['runtime'] if c.isnumeric())
        )
    file.write(out)

#Insert the crew into people
    #Insert Writer into person
    wname = str(movie['writer'][0])
    contact = wname.replace(" ", "") + "@gmail.com"
    writerDOB = writer.get("birth date", "0001-01-01")
    out = formatSanitary(
        personInsert,
        name = wname,
        contact = contact,
        dob = writerDOB,
        roleFlags = 0b100 # TEMPORARY!! TODO: track Person and do bitwise AND on these!
        )
    file.write(out)

    #Insert Writer into Wrote
    out = formatSanitary(
        wroteInsert,
        name = wname,
        titleID = movie.movieID
        )
    file.write(out)    

    #Insert Director into Person
    dname = str(movie['director'][0])
    contact = dname.replace(" ", "") + "@gmail.com"
    directorDOB = director.get("birth date", "0001-01-01")    
    out = formatSanitary(
        personInsert,
        name = dname,
        contact = contact,
        dob = directorDOB,
        roleFlags = 0b010 # TEMPORARY!! TODO: track Person and do bitwise AND on these!
        )
    file.write(out)

    #Insert Director into Directed
    out = formatSanitary(
        directedInsert,
        name = dname,
        titleID = movie.movieID
        )
    file.write(out)

    #Insert top cast members
    for i in range(2):
        actor = ia.get_person(cast[i].personID)
        aname = str(cast[i])

        #Insert Actor into Person
        contact = aname.replace(" ", "") + "@gmail.com"
        actorDOB = actor.get("birth date", "0001-01-01")
        out = formatSanitary(
            personInsert,
            name = aname,
            contact = contact,
            dob = actorDOB,
            roleFlags = 0b001 # TEMPORARY!! TODO: track Person and do bitwise AND on these!
            )
        file.write(out)

        #Insert Actor into Acted
        out = formatSanitary(
            actedInsert,
            name = aname,
            titleID = movie.movieID
            )
        file.write(out)
print("Movies and Crew Written (Top and Bottom)\n")

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

    #create a plot variable to remove ' from the plot variable
    showPlot = str(show['plot'][0]).replace("'", "''")
    
    #Create the SQL statement to insert into table
    out = "INSERT\nINTO Media(TitleID, Name, Rating, Budget, Synopsis, Country)\nVALUES(" + show.movieID + ", \'" + show['title'] + "\', \'" + str(show['rating']) + "\', " + budget + ", \'" + showPlot + "\', \'" + str(show["countries"][0]) + "\')\n\n"
    file.write(out)

    #Create the SQL statement to insert into genre
    for genre in movie['genres']:
        out = "INSERT\nINTO Genre(Genre_MediaID, GenreName)\nVALUES(" + show.movieID + ", \'" + genre + "\');\n\n"
        file.write(out)

    #create the SQL statement to insert languages
    for language in movie['languages']:
        out = "INSERT\nINTO Languages(Language_MediaID, LanguageName)\nVALUES(" + show.movieID + ", \'" + language + "\');\n\n"
        file.write(out)
#Insert the crew into people
    #Insert Writer into person
    
    try:
        writer = ia.get_person(show['writer'][0].personID)

        #insert writer into person
        contact = str(movie['writer'][0]).replace(" ", "") + "@gmail.com"
        try:
            writerDOB = writer["birth date"]
        except KeyError:
            writerDOB = "0001-01-01"
        out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(\'" + str(show['writer'][0]) + "\', \'" + contact + "\', DATE \'" + writerDOB + "\', " + str(0b100) + ");\n\n"
        file.write(out)

        #Insert Writer into Wrote
        out = "INSERT\nINTO Wrote(Writer_Name, Wrote_MediaID)\nVALUES(\'" + str(show['writer'][0]) + "\', " + show.movieID + ");\n\n"
        file.write(out)    
    except KeyError:
        pass

    try:
        director = ia.get_person(show['director'][0].personID)

        #Insert Director into Person
        contact = str(movie['director'][0]).replace(" ", "") + "@gmail.com"        
        out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(\'" + str(show['director'][0]) + "\', \'" + contact + "\', DATE \'" + director['birth date'] + "\', " + str(0b010) + ");\n\n"
        file.write(out)

        #Insert Director into Directed
        out = "INSERT\nINTO Directed(Director_Name, Directed_MediaID)\nVALUES(\'" + str(show['director'][0]) + "\', " + show.movieID + ");\n\n"
        file.write(out)
    except KeyError:
        pass

    #Insert top cast members
    for i in range(2):
        try:
            cast = (show['cast'])
            actor = ia.get_person(cast[i].personID)

            #Insert Actor into Person
            contact = str(cast[i]).replace(" ", "") + "@gmail.com"
            out = "INSERT\nINTO Person(PersonName, Contact, DOB, RoleFlags)\nVALUES(\'" + str(cast[i]) + "\', \'" + contact + "\', DATE \'" + actor['birth date'] + "\', " + str(0b001) + ");\n\n"
            file.write(out)

            #Insert Actor into Acted
            out = "INSERT\nINTO Acted(Actor_Name, Acted_MediaID)\nVALUES(\'" + str(cast[i]) + "\', " + show.movieID + ");\n\n"
            file.write(out)
        except KeyError:
            pass
print("Top Shows Written\n")

#Close the file when complete with the statements
file.close()
