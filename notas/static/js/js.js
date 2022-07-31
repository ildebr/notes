$("nav.about-barras").click(function(){
    $("section.extra").toggleClass("initial-pos");
    $("img.barras").toggleClass("hide");
    $("img.barras").css("background-color: red")
    //$("section.more-stuff>h2.title").attr('data-aos', 'fade-right')
    console.log("alo")
})

console.log("alo")


var elem = document.querySelector('.notas-container');
var msnry = new Masonry( elem, {
  // options
  itemSelector: '.nota-li',
  columnWidth: 100
});

$('.notas-container').masonry({
    // options
    itemSelector: '.nota-li',
    columnWidth: 200
  });