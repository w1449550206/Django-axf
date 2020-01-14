

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
                    }
                }
            }
        )


    })

})