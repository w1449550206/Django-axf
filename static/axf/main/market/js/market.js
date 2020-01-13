$(function(){
    $('#all_type').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        $('#all_type_container').toggle();
    })


    $('#sort_rule').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        $('#sort_rule_container').toggle()
    })
})