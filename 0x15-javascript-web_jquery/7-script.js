$.getJSON('https://swapi.co/api/people/5/?format=json').done(function (data) {
  $('#character').text('The name of the character with id = 5 is ' + data.name);
});
/*
$('#update_header').click(function () {
  fetch('https://swapi.co/api/people/5/?format=json)').then(function () {
    $('#character').text(');
  }
});
*/
