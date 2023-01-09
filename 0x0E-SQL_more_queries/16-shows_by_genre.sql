-- lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
SELECT title, name FROM tv_shows LEFT JOIN tv_show_genres tsg
    ON tv_shows.id = tsg.show_id
    LEFT JOIN tv_genres tg on tsg.genre_id = tg.id
    ORDER BY title, name;
