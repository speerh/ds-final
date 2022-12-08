from imdb import Cinemagoer
from datetime import datetime

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
    return text.replace("'", "&sq;").format(*args, **kwargs).replace("'","''").replace("&sq;","'").replace('&', 'and')

people = {}
involvementRecords = []

# Person records must be unique.
# Using this function adds a Wrote/Directed/Acted record
# and a Person if they don't exist;
# otherwise, it updates their role flags accordingly.
# Person, Wrote, Directed, and Acted records are written
# at the end of the file.
def addInvRecord(name, person, role, titleID):
    flags = 0
    if role == 'wrote':
        flags = 0b100
        involvementRecords.append(
            formatSanitary(wroteInsert, name = name, titleID = titleID)
            )
    elif role == 'directed':
        flags = 0b010
        involvementRecords.append(
            formatSanitary(directedInsert, name = name, titleID = titleID)
            )
    elif role == 'acted':
        flags = 0b001
        involvementRecords.append(
            formatSanitary(actedInsert, name = name, titleID = titleID)
            )
        
    if not name in people:
        people[name] = {
            'contact': name.replace(" ", "") + "@gmail.com",
            'DOB': person.get("birth date", "0001-01-01"),
            'roleFlags':flags
            }
    else:
        people[name]['roleFlags'] = people[name]['roleFlags'] | flags

#region SQL templates

mediaInsert = """
INSERT INTO MEDIA (TitleID, Name, Rating, Budget, Synopsis, Country)
VALUES ({titleID}, '{name}', '{rating}', {budget}, '{synopsis}', '{country}');
"""

genreInsert = """
INSERT INTO Genre(Genre_MediaID, GenreName)
VALUES({titleID}, '{genre}');
"""

langInsert = """
INSERT INTO Languages(Language_MediaID, LanguageName)
VALUES({titleID}, '{lang}');
"""

movieInsert = """
INSERT INTO Movie(MovieID, Runtime)
VALUES({titleID}, {runtime});
"""

personInsert = """
INSERT INTO Person(PersonName, Contact, DOB, RoleFlags)
VALUES('{name}', '{contact}', DATE '{dob}', {roleFlags});
"""

wroteInsert = """
INSERT INTO Wrote(Writer_Name, Wrote_MediaID)
VALUES('{name}', {titleID});
"""

directedInsert = """
INSERT INTO Directed(Director_Name, Directed_MediaID)
VALUES('{name}', {titleID});
"""

actedInsert = """
INSERT INTO Acted(Actor_Name, Acted_MediaID)
VALUES('{name}', {titleID});
"""

tvInsert = """
INSERT INTO TV_Show(TVID, Start_Date, End_Date)
VALUES ({titleID}, DATE '{startYear}-01-01', DATE '{endYear}-01-01');
"""

seasonInsert = """
INSERT INTO Season(ShowID, Season_No, Name)
VALUES ({titleID}, {season}, '{name}');
"""

episodeInsert = """
INSERT INTO Episode(Ep_ShowID, Ep_Season_No, Episode_No, Ep_Rating, Ep_Air_Date, Ep_Length, Ep_Synopsis)
VALUES ({titleID}, {season}, {episode}, '{rating}', DATE '{airdate}', {length}, '{synopsis}');
"""

#endregion

# Create the SQL statements for the topMovies/bottomMovies and Crew
# because we don't need two giant loops for this!
for mov in topMovies[:5] + bottomMovies[:5]:
    #Precisely selects the movie, writer, director, and cast
    print(f"Creating queries for {mov['title']}")
    print("Requesting fine data for Movie")
    movie = ia.get_movie(mov.movieID)
    print("Requesting fine data for Writer")
    writer = ia.get_person(movie['writer'][0].personID)
    print("Requesting fine data for Director")
    director = ia.get_person(movie['director'][0].personID)
    cast = (movie['cast'])
    
#create null variables if data isn't found
    budget_nosan = movie.get('box office', {}).get('Budget', 'NULL')
    budget = ''.join(c for c in budget_nosan if c.isnumeric()) if budget_nosan != "NULL" else "NULL"

    #Create the SQL statement to insert into media
    out = formatSanitary(
        mediaInsert,
        titleID = movie.movieID,
        name = movie['title'],
        rating = str(movie['rating']),
        budget = budget,
        synopsis = str(movie['plot'][0])[:500],
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
    addInvRecord(wname, writer, 'wrote', movie.movieID)   

    #Insert Director into Person
    dname = str(movie['director'][0])
    addInvRecord(dname, director, 'directed', movie.movieID)

    #Insert top cast members
    for i in range(2):
        print(f"Requesting fine data for actor #{i}")
        actor = ia.get_person(cast[i].personID)
        aname = str(cast[i])
        addInvRecord(aname, actor, 'acted', movie.movieID)
        
print("Movies written (Top and Bottom)\n")

#Create the SQL statements for the topShows and Crew
for sho in range(5):
    #Precisely selects the movie from the list
    print(f"Creating queries for {topShows[sho]['title']}")
    print("Requesting fine data for Show")
    show = ia.get_movie(topShows[sho].movieID)
    
    ia.update(show, 'episodes')
    episode = ia.get_movie(show['episodes'][1][1].movieID)
    
    #create null variables if data isn't found
    budget_nosan = show.get('box office', {}).get('Budget', 'NULL')
    budget = ''.join(c for c in budget_nosan if c.isnumeric()) if budget_nosan != "NULL" else "NULL"
    
    #Create the SQL statement to insert into table
    out = formatSanitary(
        mediaInsert,
        titleID = show.movieID,
        name = show['title'],
        rating = str(show['rating']),
        budget = budget,
        synopsis = str(show['plot'][0])[:500],
        country = str(show["countries"][0])   
    )
    file.write(out)

    #Create the SQL statement to insert into genre
    for genre in show['genres']:
        out = formatSanitary(
            genreInsert,
            titleID = show.movieID,
            genre = genre
            )
        file.write(out)

    #create the SQL statement to insert languages
    for language in show['languages']:
        out = formatSanitary(
            langInsert,
            titleID = show.movieID,
            lang = language
            )
        file.write(out)
#Insert the crew into people
    #Insert Writer into person
    
    try:
        print("Requesting fine data for Writer")
        writer = ia.get_person(show['writer'][0].personID)
        addInvRecord(str(show['writer'][0]), writer, 'wrote', show.movieID)  
    except KeyError:
        pass

    try:
        print("Requesting fine data for Director")
        director = ia.get_person(show['director'][0].personID)
        #Insert Director into Person
        addInvRecord(str(show['director'][0]), director, 'directed', show.movieID)
        
    except KeyError:
        pass

    #Insert top cast members
    cast = show.get('cast', [])
    for i in range(2):
        try:
            print(f"Requesting fine data for actor #{i}")
            actor = ia.get_person(cast[i].personID)
            addInvRecord(str(cast[i]), actor, 'acted', show.movieID)
        except KeyError:
            pass

    years = show['series years'].split('-')
    
    file.write(formatSanitary(
        tvInsert,
        titleID = show.movieID,
        startYear = years[0],
        endYear = years[1] if years[1].isnumeric() else "9999"
        ))

    print('Requesting fine data for S1E1')

    file.write(formatSanitary(
        seasonInsert,
        titleID = show.movieID,
        season = 1,
        name = 'Season 1'
        ))

    ep = ia.get_movie(show['episodes'][1][1].movieID)

    file.write(formatSanitary(
        episodeInsert,
        titleID = show.movieID,
        season = 1,
        episode = 1,
        rating = ep['rating'],
        airdate = datetime.strptime(ep['original air date'], '%d %b %Y').strftime('%Y-%m-%d'),
        length = ep['runtimes'][0],
        synopsis = ep['plot'][0][:500]
        ))
    
    
print("Top Shows Written\n")

print("Writing crew records.....")
for pname in people:
    p = people[pname]
    out = formatSanitary(
        personInsert,
        name = pname,
        contact = p['contact'],
        dob = p['DOB'],
        roleFlags = p['roleFlags']
        )
    file.write(out)

[file.write(i) for i in involvementRecords]
print("Done!")

#Close the file when complete with the statements
file.close()
