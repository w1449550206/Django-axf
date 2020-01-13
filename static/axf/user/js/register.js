$(function () {
    $('#name').blur(function () {
        var name = $('#name').val();

        var reg = /^\w{3,6}$/;
        //如果字符串符合该正则 那么就返回true 否则返回false
        if(reg.test(name)){
            // $('#nameinfo').html('用户名字可以注册').css('color','green');
        //    将名字发送到视图函数  然后视图函数去数据库中去访问  看有木有
        //    如果有返回用户名子已经存在  如果没有  返回用户名字可以注册
        //    $.getJson  $.get  $.post  $.ajax
        //    getJSON方法的第一个参数是请求资源路径
        //    第二个参数 是请求参数
        //    第三个参数是 执行完视图函数的返回值  注意function中必须是data
            $.getJSON('/axfuser/checkName/',
                      {'name':name},
                      //data就是执行完视图函数返回的数据
                      function (data) {
                            if(data['status'] == 200){
                                $('#nameinfo').html(data['msg']).css('color','green');
                            }else{
                                $('#nameinfo').html(data['msg']).css('color','red');
                            }
                      }
                )





        }else{
            $('#nameinfo').html('用户名字格式错误').css('color','red');
        }


    })

})