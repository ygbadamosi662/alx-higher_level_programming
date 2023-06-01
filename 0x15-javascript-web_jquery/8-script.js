const $titles = $('ul#list_movies');

$.ajax({
    type: "GET",
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    success: data => {
        $.each(data.results, (i, item) => {
            $titles.append(`<li> Title ${i+1}: ${item.title}`);
        });
    },

    error: () => {
        console.log("Couldn't fetch titles")

    }
});
