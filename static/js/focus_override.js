// Over ride default focus state on signup form
let newfocus = document.querySelector('#id_email');
let autofocus = document.querySelector('#id_username');
    if (autofocus) {
        autofocus.removeAttribute('autofocus');
        newfocus.focus();
    }