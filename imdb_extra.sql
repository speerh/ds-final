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
VALUES();

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES();

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES();

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES();

INSERT INTO Review(Review_MediaID, Reviewer, ReviewDate, ReviewBody, Spoilers, Helpful, Stars, ReviewTitle)
VALUES();

