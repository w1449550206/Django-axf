$(function () {
    $('#login').click(function () {
        window.open('/axfuser/login/',target='_self');
    })


    $('#regis').click(function () {
        window.location.href='/axfuser/register/';
    })
})