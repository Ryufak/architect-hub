function page_load() {
    add_classes();
}

var left = 0;
var right = 0;

function add_classes() {
    let images = document.getElementsByClassName('sub-img');
    var i = 0;
    var m = 100;
    for (const element of images) {
        right += 1;
        element.classList.add('img' + i);
        element.style.marginLeft = m +"%";
        m += 100;
        i += 1;}
}

function click_left(){
    if (left > 0) {
        let images = document.getElementsByClassName('img');
        for (const element of images) {
            let margin = element.style.marginLeft;
            var value = parseInt(margin) + 100;
            element.style.marginLeft = value +"%";}
        left = left - 1;
        right = right + 1;}
}


function click_right(){
    if (right > 0){
        let images = document.getElementsByClassName('img');
        for (const element of images) {
            let margin = element.style.marginLeft;
            var value = parseInt(margin) - 100;
            element.style.marginLeft = value +"%";}
        left = left + 1;
        right = right - 1;}
}


