$('.login-btn').click(function () {
    if($('#id_username').val() == '') {
        $('#required_username').css('display', 'block');
        return false;
    }

    if($('#id_password').val() == '') {
        $('#required_password').css('display', 'block');
        return false;
    }

    if (!$('#id_username').val() == '' && !$('#id_password').val() == '') {
        $('form.login-form').submit();
    }
});

$('#id_username').on('keyup', function () {
    if ($('#required_username').css('display') == 'block') {
        $('#required_username').css('display', 'none');
    }
});

$('#id_password').on('keyup', function () {
    if ($('#required_password').css('display') == 'block') {
        $('#required_password').css('display', 'none');
    }
});