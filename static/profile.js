function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftokenn = getCookie('csrftoken');


$(function ($){
    $('#login_form').submit(function (e){
        e.preventDefault();
        var $data = {};
        $('#login_form').find('input').each(function (){
            $data[this.name] = $(this).val();
        });
        $.ajax({
            url: "/accounts/login/",
            type: 'POST',
            data: $data,
            headers: {'X-CSRFToken': csrftokenn},
            dataType: 'json',
            success: function (data) {
                window.location.reload();
            },
            error: function (data) {
                console.log('ERROR' + '-' + data.responseJSON.form.errors);
                let login_errors = data.responseJSON.form.fields.login.errors;
                if (login_errors.length){
                    $('#login_email').addClass('is-invalid');
                    $('#login_errors').text(login_errors);
                }
                else {
                    $('#login_email').removeClass('is-invalid');
                }
                let errors = data.responseJSON.form.errors;
                if (errors.length){
                    $('#errors').removeClass('d-none').text(errors);
                } else {
                    $('#errors').addClass('d-none');
                }
            }
        });
    });
});
