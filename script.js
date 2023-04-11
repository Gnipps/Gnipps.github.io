$(window).on("scroll", function () {
  var windowHeight = $(window).height();
  var scrollTop = $(window).scrollTop();
  $(".fade-in").each(function () {
    var elementTop = $(this).offset().top;
    if (elementTop < scrollTop + windowHeight - 100) {
      $(this).addClass("fade-in-active");
    }
  });
});
