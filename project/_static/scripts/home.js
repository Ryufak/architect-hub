function page_load() {
    hero_activate();
}

function hero_activate() {
    left_panel = document.getElementById('hero-split-left');
    right_panel = document.getElementById('hero-split-right');

    left_panel.classList.add('active');
    right_panel.classList.add('active');
}