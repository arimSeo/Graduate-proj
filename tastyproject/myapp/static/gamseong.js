$(document).ready(function () {
    $(".logo").hide();
    $(".h1").hide();
    $(".box1").hide();
    $(".box2").hide();
    setTimeout(function () {
        $(".loading").fadeOut(400);
        $(".logo").fadeIn(2000);
        $(".h1").fadeIn(2000);
        $(".box1").fadeIn(5000);
        $(".box2").fadeIn(5000);
    }, 2500);
});