$(function(){
    init_mySwiper();
    init_swiperMenu();
})


function init_mySwiper(){
    var mySwiper = new Swiper('#topSwiper',{
        loop:true,
        autoplay:3000,
        pagination:'.swiper-pagination',
        autoplayDisableOnInteraction:false,
    })
}

function init_swiperMenu(){
    var mySwiper = new Swiper('#swiperMenu',{
        slidesPerView :3
    })
}