'use strict';

(function (window, document, $) {
    function sendForm(form, result_field) {

        clearFormResult(result_field);

        var request = $.ajax({
            url: 'http://127.0.0.1:5000/comment',
            method: 'post',
            crossDomain: true,
            dataType: 'json',
            data: form.serialize()
        });

        request.done(function (response) {
            printFormResult(result_field, response);
        });

        request.fail(function (jqXHR, textStatus, errorThrown) {
            alert('Произошла ошибка при отправке формы');
            console.log(jqXHR, textStatus, errorThrown);
        });
    }

    function printFormResult(result_field, response) {
        if(response.status)
            result_field.html("<p>" + response.statusText + "</p>");
        else
            $.each(response.errors, function( field, error ) {
              result_field.prepend("<p>" + field + ": " + error + "</p>");
            });
    }

    function clearFormResult(result_field) {
        result_field.html('');
    }

    $(document).ready(function() {
        var form = $( "form[name='comment']" );
        var result = $( ".result" );
        form.submit(function(event) {
            sendForm(form, result);
            event.preventDefault();
        });
    });
})(window, document, jQuery);
