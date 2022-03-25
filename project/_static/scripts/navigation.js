//Toggle Hamburger
function hamburger() {
    const hamburger = document.getElementById('hamburger');
    const navigation = document.getElementById('menu');
    hamburger.classList.toggle('active');
    navigation.classList.toggle('active');
}

//Mobile and Tablet open submenu
if($(window).width() < 1050) {
function language() {
    const activate = document.getElementById('lang-dd');

    if (activate.classList.contains('active') == true) {
        activate.classList.remove('active');}
    else {
        activate.classList.add('active');}
}
}



//Log out anchor -> activate logout form
function logout_submit() {
    document.getElementById('logout_submit_form').submit();
}


