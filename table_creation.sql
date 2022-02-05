
--songplays - records in log data associated with song plays i.e. records with page NextSong
CREATE TABLE songplays (
songplay_id bigserial not null primary key, 
start_time datetime, 
user_id varchar REFERENCES users(user_id), 
level varchar, 
song_id varchar REFERENCES songs(song_id), 
artist_id varchar REFERENCES artists(artist_id), 
session_id int, 
location varchar, 
user_agent varchar)

---users - users in the app
CREATE TABLE users(
user_id varchar not null PRIMARY KEY, 
first_name varchar, 
last_name varchar, 
gender char, 
level varchar)


--songs - songs in music database
CREATE TABLE songs(
song_id varchar not null PRIMARY KEY, 
title varchar, 
artist_id varchar, 
year int, 
duration numeric(18,5))

--artists - artists in music database
CREATE TABLE artists(
artist_id varchar not null PRIMARY KEY, 
name varchar, 
location varchar, 
latitude numeric(18,5), 
longitude numeric(18,5))

--time - timestamps of records in songplays broken down into specific units
CREATE TABLE time (
start_time datetime, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday varchar )
