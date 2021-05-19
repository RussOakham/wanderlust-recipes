// General function for submitting forms via AJAX

// RECIPE FAVOURITE SUBMISSION SCRIPTS
// Toggle 'favourite' fontawesome icon class on toggle
$('#recipe_favorite').on('click', function (event) {
    $('.fa-heart').toggleClass('far fas');
});

// Submit 'favourite' form to server via AJAX
$('#recipe_favorite_form').submit(function (event) {
    event.preventDefault();
    submitFormAJAX(event, null);
});

// Binds favorite form submit to favorite checkbox toggle change event
$('#recipe_favorite input[type=checkbox]').change(function (event) {
    $('#recipe_favorite_form').submit();
});

// RECIPE RATING SUBMISSION SCRIPTS
// Submit 'rating' form to server via AJAX
// On rating submission, unhide tick gif for visual submit confirmation.
$('#recipe_rating_form').submit(function (event) {
    event.preventDefault();
    submitFormAJAX(event, null);
    // Disable input once submitted
    $('input', this).prop('disabled', true);
    $('.star-rating-input', this).prop('disabled');
    $('.collapsible').collapsible('open', 0);
});

// Submit 'comment' form to database via AJAX
$('#user_comment_form').submit(function (event) {
    event.preventDefault();
    submitFormAJAX(event, commentSubmit);
});

$('#user-comment-list').on("click", ".remove-comment", function (event) {
    commentIndex = {
        "recipe": $('recipeId').val(),
        "comment": $(this).closest('.comment-div').index()
    }
    console.log(commentIndex)
});

// General AJAX form submission script
// Following links used to help create and understand the below script:
// https://www.digitalocean.com/community/tutorials/submitting-ajax-forms-with-jquery
// https://github.com/seanyoung247/Plum/blob/main/static/js/script.js
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