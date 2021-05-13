// Save timestamp for recipe creation, allows sorting by date
$(document).ready(function () {
    $('#created_on').val(new Date().getTime());
});