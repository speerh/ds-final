--1 select errored birth dates

SELECT PersonName 
FROM Person
WHERE DOB = DATE '0001-01-01';

--2 select * from media joining media + tv shows?

SELECT Media.TitleID, Media.Name, TV_Show.Start_Date, TV_Show.End_Date
FROM Media
INNER JOIN TV_Show ON Media.TitleID=TV_Show.TVID;

--3 select * from media joining media + movies????

SELECT Media.TitleID, Media.Name, Movie.Runtime
FROM Media
INNER JOIN Movie ON Media.TitleID=Movie.MovieID;

--4 show more like

SELECT Media.Name
FROM Media
INNER JOIN More_Like ON Media.TitleID=More_Like.ReferenceID
INNER JOIN Media ON More_Like.SimilarID=Media.TitleID;

--5 showing movies that people have directed

SELECT Person.PersonName, Media.Name
FROM Person
INNER JOIN Directed ON Person.PersonName=Directed.Director_Name
INNER JOIN Media ON Directed.Directed_MediaID=Media.TitleID;

--retrieve basic info about an entry

SELECT Media.Name, Genre.GenreName, Languages.LanguageName, ViewOpt.ViewOpt_MediaID
FROM Media
INNER JOIN Genre ON Media.TitleID=Genre.Genre_MediaID
INNER JOIN Languages ON Media.TitleID=Languages.Language_MediaID
INNER JOIN ViewOpt ON Media.TitleID=ViewOpt.ViewOpt_MediaID;

--7 show media rated 9.0 or 1.0

SELECT Media.Name, Media.Rating FROM Media
WHERE Media.Rating = '9.0'
UNION
SELECT Media.Name, Media.Rating FROM Media
WHERE Media.Rating = '9.1';

--8 join media and movie and show info from both

SELECT Media.Name, 
FROM Media
INNER JOIN MediaPhoto ON Media.ID=MediaPhoto.MP_MediaID
WHERE MediaPhoto <> NULL

UNION

SELECT Media.Name, 
FROM Media
INNER JOIN MediaVideo ON Media.ID=MediaVideo.MV_MediaID
WHERE MediaVideo <> NULL;

--9 select count of ratings

SELECT Media.Rating, COUNT(Media.Rating)
FROM Media
GROUP BY Media.Rating
ORDER BY COUNT(Media.Rating) DESC;



--10 select count of directed per person

SELECT Directed.Director_Name, COUNT(Directed.Director_Name)
FROM Directed
GROUP BY Directed.Director_Name
ORDER BY COUNT(Directed.Director_Name) DESC;