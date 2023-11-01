$.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (my_json) => {
        $('div#hello').text(my_json.hello)
    }
})