-- lists all genres of the show Dexter in hbtn_0d_tvshows database.
SELECT name FROM tv_shows INNER JOIN tv_show_genres tsg ON tv_shows.id =
    tsg.show_id INNER JOIN tv_genres ON tv_genres.id = tsg.genre_id WHERE
    title='Dexter' ORDER BY name;
