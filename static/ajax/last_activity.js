$(function() {
    // Start a timer that will call our API at regular intervals
    // The 2nd value is the time in milliseconds, so 5000 = 5 seconds
    setInterval(updateChat, 3000);
    get_chat()
});

function updateChat() {
    $.getJSON('api/get_latest_chat/3', function(data){
        // Enumerate JSON objects
        $.each(data, function (i, item){
                // console.log(item);
                var newChatLine = $('<div class="border rounded bg-body p-1 m-1 text-wrap text-break" style="width: 220px">');
                newChatLine.append('<div class="fw-semibold">' + item.author__username + '</div>');
                newChatLine.append('<div class="fw-lighter">' + item.text + '</div>');
                $('#chatbox').append(newChatLine);
                $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
            })
    });
}

function get_chat() {
    $.getJSON({
        url: 'api/get_chat/',
        success: function (data){
            $.each(data, function (i, item){
                // console.log(item);
                var newChatLine = $('<div class="border rounded bg-body p-1 m-1 text-wrap text-break" style="width: 220px">');
                newChatLine.append('<div class="fw-semibold">' + item.author__username + '</div>');
                newChatLine.append('<div class="fw-lighter">' + item.text + '</div>');
                $('#chatbox').append(newChatLine);
                $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
            })
        }
    })
}

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

$(function ($) {
    $('#new_message').submit(function (e) {
        e.preventDefault()
        var $data = {};
        $data['csrfmiddlewaretoken'] = getCookie('csrftoken');
        $('#new_message').find('input').each(function (){
            $data[this.name] = $(this).val();
        })
        console.log($data)
        $.ajax({
            type: 'POST',
            url: 'api/new_chat_message/',
            data: $data,
            success: function (data) {
                $('#new_message').find('input').val('')
            }
            })
    })
})
