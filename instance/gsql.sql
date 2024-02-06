BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "gtable" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(250),
	"platform"	VARCHAR(250),
	"release_date"	VARCHAR(250),
	"summary"	VARCHAR(400),
	"review"	NUMERIC,
	PRIMARY KEY("id")
);
INSERT INTO "gtable" VALUES (1,'The Legend of Zelda: Ocarina of Time',' Nintendo 64','November 23, 1998','As a young boy, Link is tricked by Ganondorf, the King of the Gerudo Thieves. The evil human uses Link to gain access to the Sacred Realm, where he places his tainted hands on Triforce and transforms the beautiful Hyrulean landscape into a barren wasteland. Link is determined to fix the problems he helped to create, so with the help of Rauru he travels through time gathering the powers of the Seven Sages.',9.1);
INSERT INTO "gtable" VALUES (2,'Tony Hawk''s Pro Skater 2','PlayStation','September 20, 2000','As most major publishers'' development efforts shift to any number of next-generation platforms, Tony Hawk 2 will likely stand as one of the last truly fantastic games to be released on the PlayStation.',7.4);
INSERT INTO "gtable" VALUES (3,'Grand Theft Auto IV','PlayStation 3','April 29, 2008','[Metacritic''s 2008 PS3 Game of the Year; Also known as "GTA IV"] What does the American Dream mean today? For Niko Belic, fresh off the boat from Europe. It''s the hope he can escape his past. For his cousin, Roman, it is the vision that together they can find fortune in Liberty City, gateway to the land of opportunity. As they slip into debt and are dragged into a criminal underworld by a series of shysters, thieves and sociopaths, they discover that the reality is very different from the dream in a city that worships money and status, and is heaven for those who have them an a living nightmare for those who don''t. [Rockstar Games]',7.7);
COMMIT;
