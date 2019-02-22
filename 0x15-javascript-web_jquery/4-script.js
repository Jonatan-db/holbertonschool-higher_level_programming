$('header').on('click', function () {
  if ($(this).hasClass('red')) {
    // $(this).toggleClass('red');
    $(this).removeClass('red');
    $(this).addClass('green');
  } else if ($(this).hasClass('green')) {
    $(this).removeClass('green');
    $(this).addClass('red');
  }
});
