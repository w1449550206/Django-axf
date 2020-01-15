

$(function () {
    $('.subToCart').click(function () {
        var $button = $(this);
        var $div = $button.parent().parent();

        var cartid = $div.attr('cartid');

        $.post('/axfcart/subToCart/',
               {'cartid':cartid},
                function (data) {
                    if(data['status'] == 200){
                        if(data['c_goods_num'] >= 1){
                            $button.next().html(data['c_goods_num']);
                        }else{
                            $div.remove();
                        }
                    }
                })



    })


    $('.confirm').click(function () {
        var $confirm = $(this);
        var $div = $confirm.parent();

        var cartid = $div.attr('cartid');

        $.ajax(
            {
                url:'/axfcart/changeStatus/',
                data:{'cartid':cartid},
                type:'GET',
                dataType:'json',
                success:function (data) {
                    if(data['status'] == 200){
                        if(data['c_is_select']){
                            $confirm.find('span').find('span').html('✔')
                        }else{
                            $confirm.find('span').find('span').html('')
                        }
                        if(data['is_all_select']){
                            $('#all_select').find('span').find('span').html('✔');
                        }else{
                            $('#all_select').find('span').find('span').html('');
                        }
                    }
                }
            }
        )


    })


    $('#all_select').click(function () {
    //    （1）要将当前用户的购物车的选中的cartid放到一个列表  未选中的cartid放到一个列表
    //    （2）如果未选中的列表的长度大于0了   证明有未被选中的  所以将此列表的对应的对象修改为选中
    //    （3）否则证明了此时全都被选中了 那么就要将列表对应的对象的修改为未被选中
        var select_list = [];
        var unselect_list = [];

        var $confirm = $('.confirm');

        $confirm.each(function () {
            //$(this)一个有一个的div对象
            var $div = $(this);

            var cartid = $div.parent().attr('cartid');
            //html()会判断标签中有没有内容 如果有内容 那么返回true  如果没有返回false
            if($div.find('span').find('span').html()){
                select_list.push(cartid);
            }else{
                unselect_list.push(cartid);
            }
        })


        if(unselect_list.length > 0){
            $.getJSON('/axfcart/allSelect/',
                      //ajax的参数 不可以传递列表
                      //join方法会将列表中所有的元素进行拼接
                      {'cartlist':unselect_list.join('#')},
                       function (data) {
                           if(data['status'] == 200){
                               $confirm.find('span').find('span').html('✔');
                               $('#all_select').find('span').find('span').html('✔');
                           }
                       })
        }else{

            $.get('/axfcart/allSelect/',
                  {'cartlist':select_list.join('#')},
                  function (data) {
                      if(data['status'] == 200){
                               $confirm.find('span').find('span').html('');
                               $('#all_select').find('span').find('span').html('');
                           }
                  })


        }


    })



})