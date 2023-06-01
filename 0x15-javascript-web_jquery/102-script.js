$('document').ready(() => {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
    $('input#btn_translate').click(() => {
        const $input = $('input#language_code').val() 
        $.get((url + $input), data => {
        $('div#hello').html(data.hello);
      });
    });
});
