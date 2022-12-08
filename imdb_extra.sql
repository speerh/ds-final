--MORELIKE
INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(68646, 71562);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(71562, 68646);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(167260, 120737);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(120737, 167260);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(120737, 167261);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(167261, 167260);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(167260, 167261);

--VIEWOPT: ONLY INSERT MEDIA IDS

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(68646, 'Netflix');

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(71562, 'Netflix');

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(167260, 'Netflix');

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(120737, 'Netflix');

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(167261, 'Netflix');

--SEASON: INSERT SHOW IDS ONLY-- ONE SEASON PER SHOW ATM

INSERT INTO Season(ShowID, Season_No, Name)
VALUES (ID, 1, 'Season 1');

INSERT INTO Season(ShowID, Season_No, Name)
VALUES (ID, 1, 'Season 1');

INSERT INTO Season(ShowID, Season_No, Name)
VALUES (ID, 1, 'Season 1');

INSERT INTO Season(ShowID, Season_No, Name)
VALUES (ID, 1, 'Season 1');

INSERT INTO Season(ShowID, Season_No, Name)
VALUES (ID, 1, 'Season 1');

--EPISODE: ONLY INPUT SHOW ID

INSERT INTO Episode(Ep_ShowID, Ep_Season_No, Episode_No, Ep_Rating, Ep_Air_Date, Ep_Length, Ep_Synopsis)
VALUES(ID, 1, 1, 'N/A', DATE '0001-01-01', 30, 'No description given.');

INSERT INTO Episode(Ep_ShowID, Ep_Season_No, Episode_No, Ep_Rating, Ep_Air_Date, Ep_Length, Ep_Synopsis)
VALUES(ID, 1, 1, 'N/A', DATE '0001-01-01', 30, 'No description given.');

INSERT INTO Episode(Ep_ShowID, Ep_Season_No, Episode_No, Ep_Rating, Ep_Air_Date, Ep_Length, Ep_Synopsis)
VALUES(ID, 1, 1, 'N/A', DATE '0001-01-01', 30, 'No description given.');

INSERT INTO Episode(Ep_ShowID, Ep_Season_No, Episode_No, Ep_Rating, Ep_Air_Date, Ep_Length, Ep_Synopsis)
VALUES(ID, 1, 1, 'N/A', DATE '0001-01-01', 30, 'No description given.');

INSERT INTO Episode(Ep_ShowID, Ep_Season_No, Episode_No, Ep_Rating, Ep_Air_Date, Ep_Length, Ep_Synopsis)
VALUES(ID, 1, 1, 'N/A', DATE '0001-01-01', 30, 'No description given.');

--AWARD: custom-make these please, jsut pull from the movies we have

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES('Best Picture', 'Academy Awards', 'Best Picture', 1973, 68646, 'Winner');

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES('Best Picture', 'Academy Awards', 'Best Picture', 1975, 71562, 'Winner');

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES('Best Picture', 'Academy Awards', 'Best Picture', 2004, 167260, 'Winner');

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES('Best Sound Editing', 'Academy Awards', 'Best Sound Editing', 2003, 167261, 'Winner');

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES('Best Cinematography', 'Academy Awards', 'Best Cinematography', 2002, 120737, 'Winner');

--REVIEW: again just copy paste this from the media we have

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES(167261, 'dcastor', DATE '2002-12-18', "I considered The Fellowship of the Ring to be one of the greatest movies ever. This one is better!", 0, 111, 9, "Great One");

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES(120737, 'MR-ODIN', DATE '2020-02-15', "It is my firm belief that the standard versions of The Lord of the Rings should be jettisoned in favour of the extended editions universally. Sure, the near 4 hour runtime is a tad steep, but for an absolute masterpiece like this, it's work every second and the first act of undoubtedly the best trilogy in cinematic history!", 0, 77, 5, "Great");

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES(68646, 'alexkolokotronis', DATE '2008-6-21', 'Tell me a movie that is more famous than this. Tell me a movie that has had more parodies spinned off its storyline than this. Tell me one movie that has been as quoted as a much as this.', 1, 247, 10, 'An Iconic Film');

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES(71562, 'umunir-36959', DATE '2019-8-9', 'One of the all time greats. Or probably the alone greatest thing ever made in the history of cinematography. This movie is both "prequel" and "sequel" of the first godfather movie.', 0, 107, 10, 'A masterpiece that can never be beaten...');

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES(167260, 'auuwws', DATE '2020-9-28', 'Best movie in the trilogy and sealed in the best possible way', 0, 185, 10, 'The best trilogy in the history of cinema');

