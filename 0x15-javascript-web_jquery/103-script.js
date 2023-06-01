$('document').ready(function () {
    $('input#btn_translate').click(translate);
    $('input#language_code').focus(function () {
      $(this).keydown(function (e) {
        if (e.keyCode === 13) {
          translate();
        }
      });
    });
  });
  
  function translate () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
    $.get(url + $('input#language_code').val()), function (data) {
      $('div#hello').html(data.hello);
    };
};
