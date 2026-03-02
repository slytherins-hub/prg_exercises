(function () {
    function setHidden(hidden) {
        document.body.classList.toggle('topnav-hidden', hidden);
        document.documentElement.classList.toggle('topnav-hidden', hidden);
        localStorage.setItem('topnavHidden', hidden ? '1' : '0');

        var button = document.getElementById('topnav-toggle');
        if (button) {
            button.textContent = hidden ? 'Zobrazit lištu' : 'Skrýt lištu';
        }
    }

    function init() {
        var button = document.createElement('button');
        button.id = 'topnav-toggle';
        button.type = 'button';
        button.textContent = 'Skrýt lištu';
        document.body.appendChild(button);

        var hidden = localStorage.getItem('topnavHidden') === '1';
        setHidden(hidden);

        button.addEventListener('click', function () {
            setHidden(!document.body.classList.contains('topnav-hidden'));
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
