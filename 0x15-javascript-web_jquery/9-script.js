document.addEventListener('DOMContentLoaded', () => {
    $.ajax({
        type: "GET",
        url: "https://fourtonfish.com/hellosalut/?lang=fr",
        success: data => {
            $('div#hello').text(data.hello);
        },

        error: () => {
            console.log("Couldn't get data");
        }
    });
    
});
