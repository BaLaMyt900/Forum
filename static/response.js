function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



$(function ($) {
    $('#response_form').submit(function (form) {
        form.preventDefault();
        $.ajax({
            url: '/announce/responce/new/',
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            data: $(this).serialize(),
            method: 'POST',
            success: function (data) {
                $('#response_form').addClass('d-none');
                $('#responce_succsess').removeClass('d-none');
            },
            error: function (data) {
                console.log('ERROR - ' + data);
            }
        });
    });
});