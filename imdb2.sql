DROP TABLE Media CASCADE CONSTRAINTS;
DROP TABLE More_Like CASCADE CONSTRAINTS;
DROP TABLE Genre CASCADE CONSTRAINTS;
DROP TABLE Languages CASCADE CONSTRAINTS;
DROP TABLE ViewOpt CASCADE CONSTRAINTS;
DROP TABLE Movie CASCADE CONSTRAINTS;
DROP TABLE TV_Show CASCADE CONSTRAINTS;
DROP TABLE Season CASCADE CONSTRAINTS;
DROP TABLE Episode CASCADE CONSTRAINTS;
DROP TABLE Award CASCADE CONSTRAINTS;
DROP TABLE Review CASCADE CONSTRAINTS;
DROP TABLE Person CASCADE CONSTRAINTS;
DROP TABLE Wrote CASCADE CONSTRAINTS;
DROP TABLE Directed CASCADE CONSTRAINTS;
DROP TABLE Acted CASCADE CONSTRAINTS;
DROP TABLE MediaVideo CASCADE CONSTRAINTS;
DROP TABLE MediaPhoto CASCADE CONSTRAINTS;
DROP TABLE ActingSample CASCADE CONSTRAINTS;
DROP TABLE PersonPhoto CASCADE CONSTRAINTS;
DROP TABLE WritingSample CASCADE CONSTRAINTS;

CREATE TABLE Media (
TitleID		NUMBER (7) PRIMARY KEY,
Name		VARCHAR2 (50) NOT NULL,
Rating		VARCHAR2 (4) DEFAULT 'N/A',
Budget		NUMBER,
Synopsis	VARCHAR2 (500) DEFAULT 'No description given',
Country		VARCHAR2 (30)
);

CREATE TABLE More_Like (
ReferenceID	NUMBER (7),
SimilarID	NUMBER (7),
CONSTRAINT More_Like_pk PRIMARY KEY (ReferenceID, SimilarID),
CONSTRAINT More_Like_ReferenceID_fk FOREIGN KEY (ReferenceID) REFERENCES Media(TitleID),
CONSTRAINT More_Like_SimilarID_fk FOREIGN KEY (SimilarID) REFERENCES Media(TitleID)
);

CREATE TABLE Genre (
Genre_MediaID	NUMBER(16),
GenreName	VARCHAR (20),
CONSTRAINT Genre_pk PRIMARY KEY (Genre_MediaID, GenreName),
CONSTRAINT Genre_MediaID_fk FOREIGN KEY (Genre_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE Languages (
Language_MediaID	NUMBER(16),
LanguageName	VARCHAR (20),
CONSTRAINT Language_pk PRIMARY KEY (Language_MediaID, LanguageName),
CONSTRAINT Language_MediaID_fk FOREIGN KEY (Language_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE ViewOpt (
ViewOpt_MediaID	NUMBER (7),
ViewOptName	VARCHAR (20),
CONSTRAINT ViewOpt_pk PRIMARY KEY (ViewOpt_MediaID, ViewOptName),
CONSTRAINT ViewOpt_MediaID_fk FOREIGN KEY (ViewOpt_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE Movie (
MovieID		NUMBER (7) PRIMARY KEY,
Runtime		NUMBER NOT NULL,
CONSTRAINT Movie_MovieID_fk FOREIGN KEY (MovieID) REFERENCES Media(TitleID)
);

CREATE TABLE TV_Show (
TVID		NUMBER (7) PRIMARY KEY,
Start_Date	DATE NOT NULL,
End_Date	DATE,
CONSTRAINT TV_Show_TVID_fk FOREIGN KEY (TVID) REFERENCES Media(TitleID)
);

CREATE TABLE Season (
ShowID		NUMBER (7),
Season_No	NUMBER (3),
Name		VARCHAR2 (30),
CONSTRAINT Season_pk PRIMARY KEY (ShowID, Season_No),
CONSTRAINT Season_ShowID_fk FOREIGN KEY (ShowID) REFERENCES TV_Show(TVID)
);

CREATE TABLE Episode (
Ep_ShowID	NUMBER (7),
Ep_Season_No	NUMBER (3),
Episode_No	NUMBER (3),
Ep_Rating	VARCHAR2 (4) DEFAULT 'N/A',
Ep_Air_Date	DATE,
Ep_Length	NUMBER NOT NULL,
Ep_Synopsis	VARCHAR2 (200) DEFAULT 'No description given',
CONSTRAINT Episode_pk PRIMARY KEY (Ep_ShowID, Ep_Season_No, Episode_No),
CONSTRAINT Episode_SeasonID_fk FOREIGN KEY (Ep_ShowID, Ep_Season_No) REFERENCES Season(ShowID, Season_No)
);

CREATE TABLE Award (
Award_Title	VARCHAR2 (20),
Organization	VARCHAR2 (40),
Category	VARCHAR2 (25),
Year		NUMBER (4),
Award_TitleID	NUMBER (7) NOT NULL,
Status		VARCHAR2 (10),
CONSTRAINT Award_pk PRIMARY KEY (Award_Title, Organization, Category, Year),
CONSTRAINT Award_TitleID_fk FOREIGN KEY (Award_TitleID) REFERENCES Media(TitleID)
);

CREATE TABLE Review (
Review_MediaID	NUMBER (7),
Reviewer	VARCHAR2 (30),
ReviewDate	DATE NOT NULL,
ReviewBody	VARCHAR2 (4000) NOT NULL,
Spoilers	NUMBER (1),
Helpful		NUMBER DEFAULT 0,
Stars		NUMBER (1),
ReviewTitle	VARCHAR2 (50) NOT NULL,
CONSTRAINT Review_pk PRIMARY KEY (Review_MediaID, Reviewer),
CONSTRAINT Review_MediaID_fk FOREIGN KEY (Review_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE Person (
PersonName	VARCHAR2 (30) PRIMARY KEY,
Contact		VARCHAR2 (50),
DOB		DATE,
RoleFlags	NUMBER (1)
);
-- RoleFlags: bit flags 0-7, 100 (4): Writer, 010 (2): Director, 001 (1): Actor

CREATE TABLE Wrote (
Writer_Name	VARCHAR2 (30),
Wrote_MediaID	NUMBER (7),
CONSTRAINT Wrote_pk PRIMARY KEY (Writer_Name, Wrote_MediaID),
CONSTRAINT Wrote_Name_fk FOREIGN KEY (Writer_Name) REFERENCES Person(PersonName),
CONSTRAINT Wrote_MediaID_fk FOREIGN KEY (Wrote_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE Directed (
Director_Name	VARCHAR2 (30),
Directed_MediaID NUMBER (7),
CONSTRAINT Directed_pk PRIMARY KEY (Director_Name, Directed_MediaID),
CONSTRAINT Directed_Name_fk FOREIGN KEY (Director_Name) REFERENCES Person(PersonName),
CONSTRAINT Directed_MediaID_fk FOREIGN KEY (Directed_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE Acted (
Actor_Name	VARCHAR2 (30),
Acted_MediaID	NUMBER (7),
CONSTRAINT Acted_pk PRIMARY KEY (Actor_Name, Acted_MediaID),
CONSTRAINT Acted_Name_fk FOREIGN KEY (Actor_Name) REFERENCES Person(PersonName),
CONSTRAINT Acted_MediaID_fk FOREIGN KEY (Acted_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE MediaVideo (
MV_MediaID	NUMBER (7),
MV_VideoLink	VARCHAR2 (200),
CONSTRAINT MediaVideo_pk PRIMARY KEY (MV_MediaID, MV_VideoLink),
CONSTRAINT MediaVideo_MediaID_fk FOREIGN KEY (MV_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE MediaPhoto (
MP_MediaID	NUMBER (7),
MP_PhotoLink	VARCHAR2 (200),
CONSTRAINT MediaPhoto_pk PRIMARY KEY (MP_MediaID, MP_PhotoLink),
CONSTRAINT MediaPhoto_MediaID_fk FOREIGN KEY (MP_MediaID) REFERENCES Media(TitleID)
);

CREATE TABLE ActingSample (
AV_PersonName	VARCHAR2 (30),
AV_VideoLink	VARCHAR2 (200),
CONSTRAINT ActingSample_pk PRIMARY KEY (AV_PersonName, AV_VideoLink),
CONSTRAINT ActingSample_PersonName_fk FOREIGN KEY (AV_PersonName) REFERENCES Person(PersonName)
);

CREATE TABLE PersonPhoto (
PP_PersonName	VARCHAR2 (30),
PP_PhotoLink	VARCHAR2 (200),
CONSTRAINT PersonPhoto_pk PRIMARY KEY (PP_PersonName, PP_PhotoLink),
CONSTRAINT PersonPhoto_PersonName_fk FOREIGN KEY (PP_PersonName) REFERENCES Person(PersonName)
);

CREATE TABLE WritingSample (
Sample_Writer_Name	VARCHAR2 (30), 
Sample_Index		NUMBER (3),
Sample_Writing		VARCHAR2 (4000),
CONSTRAINT WritingSample_pk PRIMARY KEY (Sample_Writer_Name, Sample_Index),
CONSTRAINT WritingSample_Writer_Name_fk FOREIGN KEY (Sample_Writer_Name) REFERENCES Person(PersonName)
);