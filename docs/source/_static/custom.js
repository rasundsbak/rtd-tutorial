// Eksempel: Tilpasset JavaScript for kollapsbare menyer
document.addEventListener("DOMContentLoaded", function() {
    var items = document.querySelectorAll('.wy-menu-vertical .toctree-l1 > a');
    for (var i = 0; i < items.length; i++) {
        items[i].addEventListener('click', function(event) {
            var next = this.nextElementSibling;
            if (next && next.classList.contains('wy-menu-vertical')) {
                event.preventDefault();
                next.classList.toggle('shown');
            }
        });
    }
});
