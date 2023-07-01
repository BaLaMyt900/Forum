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
            const notifications = Updatespan(pk);
            console.log(notifications);
            // TODO: Доделать сбор уведомлений и прикручивание их к объявлениям
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
                let notifications = GetNorifications(pk);
                $.each(announce, function (i, item) {
                    announce_list.append(`<li class="list-group-item bg-body d-inline-flex rounded"><a href="/announce/${item.pk}">${item.title}<span class="badge bg-primary rounded-pill">${notifications}</span></a></a></li>`);
                });
               announce_content.empty().append(announce_list);
            }
            if (response) {
                var response_list = $('<ul class="list-group list-group-flush bg-body-tertiary overflow-y-auto" style="height: 304px">');
                $.each(response, function (i, item) {
                   response_list.append(`<li class="list-group-item bg-body-tertiary"><a href="/announce/${item.id}">${item.title}<span id="notification_${item.id}" class="badge bg-primary rounded-pill"></span></a></li>`);
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
});

function GetNorifications (pk) {
    $.ajax({
        url: '/accounts/profile/ajax/update_notifications/' + pk,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            console.log(data);
        },
        error: function (data) {
            console.log(data);
        }
    });
}