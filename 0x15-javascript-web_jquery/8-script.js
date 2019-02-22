$.getJSON('https://swapi.co/api/films/?format=json').done(function (data) {
  $.each(data.results, function(i, item) {
  $('#list_movies').append('<li>' + item.title + '</li>');
  });
});
