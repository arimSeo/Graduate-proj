$(document).ready(function () {
    $(".logo").hide();
    $(".h1").hide();
    $(".p").hide();
    $(".box1").hide();
    $(".box2").hide();
    $(".more").hide();
    setTimeout(function () {
        $(".loading").fadeOut(400);
        $(".logo").fadeIn(2000);
        $(".h1").fadeIn(2000);
        $(".p").fadeIn(4000);
        $(".box1").fadeIn(4500);
        $(".box2").fadeIn(6000);
        $(".more").fadeIn(6000);
    }, 2500);
});