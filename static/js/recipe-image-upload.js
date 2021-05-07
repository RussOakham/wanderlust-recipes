// Shows the cloudinary image upload widget
$("#image_upload_btn").click(function (event) {
    event.preventDefault();
    cloudinary.openUploadWidget({
            cloud_name: 'dolhmfgvf',
            upload_preset: 'syqgnqe3',
            maxFiles: 1,
            maxFileSize: 100000,
            autoMinimize: true,
            resourceType: "image",
            min_height: 260,
        },
        imageUploaded);
});

// Shows the current selected image in the image box
$("#image_upload_url").on('change', function (event) {
    $('#recipe-upload-image').prop("src", $(this).val());
});

// cloudinary callback. Sets image upload input to new URL
function imageUploaded(error, result) {
    $('#recipe-upload-image').prop("src", result[0].secure_url);
    $('#image_upload_url').val(result[0].secure_url)
};