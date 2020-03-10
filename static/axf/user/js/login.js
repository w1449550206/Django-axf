$(function () {
    $('#changeimg').click(function () {
        $(this).attr('src','/axfuser/get_code/?'+Math.random())
    })
    
    
    $('form').submit(function () {
        var password = $('#password').val();

        var secret_password = md5(password);

        $('#password').val(secret_password);



        return true;
    })
})