$.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: (my_json) => {
        $('div#character').append('<b>' + my_json.name + '</b>');
    }
});