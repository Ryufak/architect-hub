function page_load() {
    load_blocks();
}


function load_blocks(){
    var blocks = document.getElementsByClassName('block');
    for (const element of blocks){ element.classList.add('active'); }



}
