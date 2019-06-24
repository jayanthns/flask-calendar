
// $(document).ready(function () {
//     $.ajax({
//         url: USER_DETAILS_URL,
//         dataType: 'json',
//         type: 'get',
//         contentType: 'application/json',
//         success: function (data, textStatus, jQxhr) {
//             console.log(data);
//             window.location.replace("/");
//         },
//         error: function (jqXhr, textStatus, errorThrown) {
//             // window.location.replace("/users/login");
//         }
//     });
// });

// $("form.user-login-form").submit(
//     function submit_login(e) {
//         e.preventDefault()
//         var $form = $("form.user-login-form")
//         var data = getFormData($form);
//         // $(".submit-button").text("Logging In").attr('disabled', true)
//         console.log(data)
//         call_login(data);

//     }
// );

function call_login(request_data) {
    $.ajax({
        url: LOGIN_URL,
        dataType: 'json',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(request_data),
        success: function (data, textStatus, jQxhr) {
            console.log(data);
            console.log(textStatus);
            console.log(jQxhr);
        },
        error: function (jqXhr, textStatus, errorThrown) {
            console.log(jqXhr);
            console.log(textStatus);
            console.log(errorThrown);
        }
    });
};


// $('.forgot-password').on('click', function (event) {
//     event.preventDefault();
//     console.log("CLICKED");
//     $('.modal').css('display', 'block');
// })