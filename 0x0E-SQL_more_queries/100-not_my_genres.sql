-- a script that uses the hbtn_0d_tvshows 
SELECT DISTINCT name FROM (SELECT DISTINCT id, title, genre_id FROM tv_shows JOIN tv_show_genres tsg ON
    tv_shows.id = tsg.show_id WHERE title <> 'Dexter') AS dexter_genre INNER
    JOIN tv_genres ON dexter_genre.genre_id = tv_genres.id ORDER BY name;
