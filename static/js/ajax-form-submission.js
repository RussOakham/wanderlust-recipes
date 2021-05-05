// General function for submitting forms via AJAX

// Toggle 'favourite' fontawesome icon class on toggle
$('#recipe_favorite').on('click', function (event) {
    $('.fa-heart').toggleClass('far fas')
});

// Submit 'favourite' form to server via AJAX
$('#recipe_favorite_form').submit(function (event) {
    event.preventDefault();
    submitFormAJAX(event, null);
    console.log('AJAX submit')
});

// Binds favorite form submit to favorite checkbox toggle change event
$('#recipe_favorite input[type=checkbox]').change(function (event) {
    $('#recipe_favorite_form').submit();
    console.log('form submit')
})

function submitFormAJAX(event, callbackSuccess) {
    // Get form data
    let data = new FormData(event.target);
    let serialised = {};
    // serialise it into key/value pairs that can be converted to JSON
    for (let key of data.keys()) {
        serialised[key] = data.get(key);
    }
    // Make AJAX request
    $.ajax({
        type: "POST",
        url: $(event.target).prop("action"), // Get route from form action attribute
        contentType: "application/json;charset=UTF-8",
        data: JSON.stringify(serialised),
        success: callbackSuccess
    });
}