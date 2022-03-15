//Toggle Hamburger
$('#hamburger').click(
    function() {
        const hamburger = document.getElementById('hamburger');
        const navigation = document.getElementById('menu');
        hamburger.classList.toggle('active');
        navigation.classList.toggle('active');
    })

//Mobile and Tablet open submenu
if($(window).width() < 1050) {
    $('#lang-drop').click(
        function() {
            const activate = document.getElementById('lang-dd');

            if (activate.classList.contains('active') == true) {
                activate.classList.remove('active');}
            else {
                activate.classList.add('active');}
        })
}
//Desktop open submenu
if($(window).width() >= 1050) {
    $('#lang-drop').hover(
        function(){$('#lang-dd').addClass('active')},       
        function(){$('#lang-dd').removeClass('active')});   
    $('#lang-drop').hover(
        function(){$('#lang-dd').addClass('active')},       
        function(){$('#lang-dd').removeClass('active')});   
}
if($(window).width() >= 1050) {
    $('#lang-dd').hover(
        function(){$('#lang-dd').addClass('active')},       
        function(){$('#lang-dd').removeClass('active')});   
    $('#lang-dd').hover(
        function(){$('#lang-dd').addClass('active')},       
        function(){$('#lang-dd').removeClass('active')});   
}

//Log out anchor -> activate logout form
function logout_submit() {
    document.getElementById('logout_submit_form').submit();
}


