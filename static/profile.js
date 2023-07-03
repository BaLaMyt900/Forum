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
            let notifications = data.notifications;
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
                if (notifications) {$('#announce_span').text(notifications.sum);}
                $.each(announce, function (i, item) {
                    if (notifications[item.pk]) {
                        announce_list.append(`<li class="list-group-item bg-body d-inline-flex rounded my-2"><a href="/announce/${item.pk}">${item.title}<span class="badge bg-primary rounded-pill">${notifications[item.pk]}</span></a></a></li>`);
                    }
                    else {
                        announce_list.append(`<li class="list-group-item bg-body d-inline-flex rounded my-2"><a href="/announce/${item.pk}">${item.title}</a></a></li>`);
                    }
                });
               announce_content.empty().append(announce_list);
            }
            if (response) {
                var response_list = $('<ul class="list-group list-group-flush bg-body-tertiary overflow-y-auto" style="height: 304px">');
                $.each(response, function (i, item) {
                   if (item.is_accept) {
                       response_list.append(`<li class="list-group-item bg-body d-flex"><a href="/announce/${item.announce_id}"><div class="d-flex-grow-1">${item.announce__title}</div><span class="badge bg-primary rounded-pill"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
  <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
</svg></span></a></li>`);
                   }
                   else {
                       response_list.append(`<li class="list-group-item bg-body"><a href="/announce/${item.announce_id}">${item.announce__title}</a></li>`);
                   }
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
