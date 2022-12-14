$(document).ready(function () {
    $('.nav li a').each(function(){
        if( $(this).attr('href') == window.location.pathname ) $(this).addClass('active');
    })
    $( ".dateinput" ).datepicker({ dateFormat: 'dd/mm/yy',     minDate: 0,});
})
