$.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (my_json) => {
        $.each(my_json.results, (i, films) => {
            $('ul#list_movies').append('<li>' + films.title + '</li>');
        });
    }
});