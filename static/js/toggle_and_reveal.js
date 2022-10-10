// Toggler function for mobile navigation -->
    $(function () {
    'use strict';

    $('[data-toggle="offcanvas"]').on('click', function () {
        $('.offcanvas-collapse').toggleClass('open');
        });
    });

// Toast reveal
    $('.toast').toast('show');
