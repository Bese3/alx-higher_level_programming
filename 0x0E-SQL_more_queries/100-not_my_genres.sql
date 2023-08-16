-- a script that uses the hbtn_0d_tvshows database to list
SELECT tv_genres.name FROM  (SELECT * FROM tv_shows JOIN tv_show_genres tsg ON
    tv_shows.id = tsg.show_id WHERE title = 'Dexter') AS tmp_table
RIGHT JOIN tv_genres ON tmp_table.genre_id = tv_genres.id WHERE tv_genres.id IS NULL
ORDER BY tv_genres.name;
