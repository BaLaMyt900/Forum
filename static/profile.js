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
                console.log(data);
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

$(function ($) {
    $('#logout_form').click(function (e) {
        e.preventDefault();
        $.ajax({
            url: '/accounts/logout/',
            type: 'POST',
            headers: {'X-CSRFToken': csrftokenn},
            success: function (data) {
                window.location.reload();
            },
            error: function (data) {
                console.log('ERROR -' + data);
            }
        });
    });
});

$(function () {
                      getProfile(pk);
                      setInterval(getProfile(pk), 3000);
                      $('#profile_content').removeClass('d-none');
                      $('#profile_btn').addClass('active');
                  });

function getProfile (pk) {
    $.ajax({
        url: '/accounts/profile/' + pk,
        dataType: 'json',
        type: 'GET',
        success: function (data) {
            let profile = data.object;
            let announce = data.announce;
            let response = data.response;
            const profile_content = $('#profile_content');
            const announce_content = $('#announce_content');
            const response_content = $('#response_content');
            if (profile) {
                var profile_form = $('<form>');
                profile_form.append(`<label class="col-form-label" for="profile_${profile.username}">Логин</label>`);
                profile_form.append(`<input id="profile_${profile.username}" class="form-control" value="${profile.username}" readonly placeholder="Не указано" type="text">`);
                profile_form.append(`<label class="col-form-label" for="profile_${profile.email}">Почта</label>`);
                profile_form.append(`<input id="profile_${profile.email}" class="form-control" value="${profile.email}" readonly placeholder="Не указано" type="email">`);
                profile_form.append(`<label class="col-form-label" for="profile_${profile.first_name}">Имя</label>`);
                profile_form.append(`<input id="profile_${profile.first_name}" class="form-control" value="${profile.first_name}" readonly placeholder="Не указано" type="text">`);
                profile_form.append(`<label class="col-form-label" for="profile_${profile.last_name}">Фамилиля</label>`);
                profile_form.append(`<input id="profile_${profile.last_name}" class="form-control" value="${profile.last_name}" readonly placeholder="Не указано" type="text">`);
                profile_content.empty().append(profile_form);
            }
            if (announce) {
                var announce_list = $('<ul class="list-group list-group-flush bg-body-tertiary overflow-y-auto" style="height: 304px">');
                $.each(announce, function (i, item) {
                    announce_list.append(`<li class="list-group-item bg-body d-inline-flex rounded"><a href="/announce/${item.id}">${item.title}</a></li>`);
                });
               announce_content.empty().append(announce_list);
            }
            if (response) {
                var response_list = $('<ul class="list-group list-group-flush bg-body-tertiary overflow-y-auto" style="height: 304px">');
                $.each(response, function (i, item) {
                   response_list.append(`<li class="list-group-item bg-body-tertiary"><a href="/announce/${item.id}">${item.title}</a></li>`);
                });
                response_content.empty().append(response_list);
            }
        },
        error: function (data) {
            console.log('ERROR - ' + data);
        }
    });
    return null;
}



$(function ($) {
    $('#announce_btn').click(function () {
    if (!$('#profile_content').hasClass('d-none')) { $('#profile_content').addClass('d-none'); }
    if (!$('#response_content').hasClass('d-none')) { $('#response_content').addClass('d-none'); }
    $('#announce_content').removeClass('d-none');
    $('#profile_btn').removeClass('active');
    $('#reply_btn').removeClass('active');
    $('#announce_btn').addClass('active');
});
})

$(function ($) {
    $('#profile_btn').click(function () {
    if (!$('#announce_content').hasClass('d-none')) { $('#announce_content').addClass('d-none'); }
    if (!$('#response_content').hasClass('d-none')) { $('#response_content').addClass('d-none'); }
    $('#profile_content').removeClass('d-none');
    $('#announce_btn').removeClass('active');
    $('#reply_btn').removeClass('active');
    $('#profile_btn').addClass('active');
});
})

$(function ($) {
    $('#reply_btn').click(function () {
    if (!$('#announce_content').hasClass('d-none')) { $('#announce_content').addClass('d-none'); }
    if (!$('#profile_content').hasClass('d-none')) { $('#profile_content').addClass('d-none'); }
    $('#response_content').removeClass('d-none');
    $('#announce_btn').removeClass('active');
    $('#profile_btn').removeClass('active');
    $('#reply_btn').addClass('active');
});
})