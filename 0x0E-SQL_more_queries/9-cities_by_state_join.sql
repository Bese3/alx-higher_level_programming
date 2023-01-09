-- lists all cities contained in the database hbtn_0d_usa. Lists the cities
-- along with their corresponding state
SELECT table_1.id, table_1.name AS name, table_2.name AS name FROM cities
    table_1, states table_2 WHERE table_1.state_id =table_2.id ORDER BY
                                                                    table_1.id;
