-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title FROM tv_shows INNER JOIN tv_show_genres tsg
    ON tv_shows.id = tsg.show_id
    INNER JOIN tv_genres tg on tsg.genre_id = tg.id WHERE name='Comedy'
    ORDER BY title;