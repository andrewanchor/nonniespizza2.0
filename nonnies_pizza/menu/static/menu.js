    $(document).ready(function(){
        $('qty_field').prop('disabled', true);
        $('plus-btn').click(function(){
            $('qty_field').val(parseInt($('qty_field').val())+1);
        });
        
    })