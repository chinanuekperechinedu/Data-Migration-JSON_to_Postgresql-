# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (
                                songplay_id bigserial not null primary key, 
                                start_time timestamp, 
                                user_id INT, 
                                level varchar, 
                                song_id varchar, 
                                artist_id varchar, 
                                session_id int, 
                                location varchar, 
                                user_agent varchar);
""")

user_table_create = ("""CREATE TABLE users(
                            user_id int not null PRIMARY KEY, 
                            first_name varchar, 
                            last_name varchar, 
                            gender char, 
                            level varchar);
""")

song_table_create = ("""CREATE TABLE songs(
                            song_id varchar not null PRIMARY KEY, 
                            title varchar, 
                            artist_id varchar, 
                            year int, 
                            duration float);
""")

artist_table_create = ("""CREATE TABLE artists(
                            artist_id varchar not null PRIMARY KEY, 
                            artist_name varchar, 
                            artist_location varchar, 
                            artist_latitude float, 
                            artist_longitude float);
""")

time_table_create = ("""CREATE TABLE time (
                            start_time timestamp, 
                            hour int, 
                            day int, 
                            week int, 
                            month int, 
                            year int, 
                            weekday int );
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays 
                            (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                             ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
                        INSERT INTO users 
                            (user_id, first_name, last_name, gender, level)
                            VALUES(%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""
                        INSERT INTO songs 
                            (song_id, title, artist_id, year, duration)
                            VALUES(%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
                       INSERT INTO artists 
                          (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
                          VALUES (%s, %s, %s, %s, %s)
                          ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
                        INSERT INTO time 
                          (start_time, hour, day, week, month, year, weekday)
                          VALUES (%s, %s, %s, %s, %s, %s, %s)
                          ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id
                  FROM songs s, artists a
                  WHERE (s.title = %s AND a.artist_name = %s AND s.duration = %s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]