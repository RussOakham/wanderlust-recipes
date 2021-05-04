// General function for submitting forms via AJAX

// Toggle 'favourite' fontawesome icon class on toggle
$('#recipe_favourite').on('click', function (event) {
    $(this).find('i').toggleClass('far fas')
});

// Submit 'favourite' form when icon is toggled
$('#recipe_favourite').on('click', function (event) {
    $('#recipe_favourite_checkbox').submit()
});

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