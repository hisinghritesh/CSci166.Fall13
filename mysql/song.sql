create database music;
use music;
drop table songs;

create table songs (
AYear int, YearlyRank int, ASource char(1),
Prefix varchar(30),
CH int, A40 int, A10 int, PK int, High int, 	
Verified char(1),
	
Artist varchar(30), ArtistInverted varchar(30),	
Featured varchar(30), UnFeatured varchar(30),
Album varchar(30), BSide varchar(30), Track varchar(30),	
ATime varchar(30), TimeSource varchar(30), explicit varchar(30),

ATimeAlbum varchar(30),
ArtistID int,	SYMBL char(1),	ReIssue varchar(30), LabelNumber varchar(30),	
Media varchar(30), Stereo varchar(30), PicSleeve varchar(30),	
Genre varchar(30), Comments varchar(30), 

WrittenBy varchar(30), 
Temp1 int, DateEntered varchar(20), DatePeaked varchar(20));

LOAD DATA 
LOCAL INFILE 'D:/Documents/druby/cs126/sql/Songs.1.csv' 
INTO TABLE songs 
FIELDS TERMINATED BY ',';
 
LOAD DATA 
LOCAL INFILE 'C:/Users/Administrator/Documents/GitHub/CSci226.Fall13/mysql/Songs.1.csv' 
INTO TABLE songs 
FIELDS TERMINATED BY ',';

select count(*) from songs;

select artist, count(*) as countit from 
(select * from songs where PK = 1) song
group by artist having count(*) > 10;

select * from songs where artist like '%beatles%';
select * from songs where AYear = 2013;
select count(*) from songs where PK = 1;