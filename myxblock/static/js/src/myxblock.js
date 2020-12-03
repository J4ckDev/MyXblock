/* Javascript for MyXBlock. */
function MyXBlock(runtime, element) {
    
    var handlerUrl = runtime.handlerUrl(element, 'get_formdata');

        $('#Send', element).click(function (eventObject) {
        var name = document.getElementById("name").value;
        var lastname = document.getElementById("lastname").value;
        var email = document.getElementById("email").value;
        $.ajax({
            type: "POST",
            url: handlerUrl,                     
            data: JSON.stringify({ "name": name, "lastname": lastname, "email": email }),
            success: location.reload
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}