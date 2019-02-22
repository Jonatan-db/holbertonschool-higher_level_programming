$(document).ready(function () {
  const valid = ['ar', 'az', 'be', 'bg', 'bn', 'bs', 'cs', 'da', 'de', 'dz',
    'el', 'en', 'en-gb', 'en-us', 'es', 'et', 'fa', 'fi', 'fil', 'fr', 'he',
    'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'ka', 'kk', 'km', 'ko', 'lb',
    'lo', 'lt', 'lv', 'mk', 'mn', 'ms', 'my', 'ne', 'no', 'pl', 'pt', 'ro', 'ru',
    'sk', 'sl', 'sq', 'sr', 'sv', 'sw', 'th', 'tk', 'uk', 'vi', 'zh'];

  $('#btn_translate').on('click', function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
    let input = url + $('#language_code').val();
    $.get(input, function (data) {
      if (data.code === 'none') {
        $('#hello').text('Bad input. Please input any of the following ' + valid);
      } else {
        $('#hello').text(data.hello);
      }
    });
  });

  $(document).keypress(function (e) {
    if (e.which === 13) {
      const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
      let input = url + $('#language_code').val();
      $.get(input, function (data) {
        if (data.code === 'none') {
          $('#hello').text('Bad input, Please input any of the following ' + valid);
        } else {
          $('#hello').text(data.hello);
        }
      });
    }
  });
});
