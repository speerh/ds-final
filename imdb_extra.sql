--MORELIKE
INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(ID1, ID2);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(ID1, ID2);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(ID1, ID2);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(ID1, ID2);

INSERT INTO more_like(ReferenceID, SimilarID)
VALUES(ID1, ID2);

--VIEWOPT: ONLY INSERT MEDIA IDS

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(ID, 'Netflix');

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(ID, 'Netflix');

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(ID, 'Netflix');

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(ID, 'Netflix');

INSERT INTO ViewOpt(ViewOpt_MediaID, ViewOptName)
VALUES(ID, 'Netflix');

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
VALUES();

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES();

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES();

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES();

INSERT INTO Award(Award_Title, Organization, Category, Year, Award_TitleID, Status)
VALUES();

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

