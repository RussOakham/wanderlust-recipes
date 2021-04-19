// On document load scripts
$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('select').formSelect();
});

// Add list item to ingredients list when '+' button hit
// https://stackoverflow.com/questions/53400879/how-to-add-new-item-to-materialize-css-collection
$('#ingredients .add-ingredient-list-item').click(function (event) {
    let IngredientItem = `<li class="collection-item">
                                <div class="input-field">
                                    <input name="ingredients" type="text" maxlength="100" required>
                                    <label for="ingredients">Ingredient</label>
                                </div>
                                <a class="remove-list-item">
                                    <i class="fas fa-times"></i>
                                </a>
                            </li>`;
    $(this).parent().before(IngredientItem);
});

// Remove ingredient list item on click
$('#ingredients').on("click", ".remove-list-item", function (event) {
    $(this).parent().remove();
});

// Add Method Step item to ingredients list when '+' button hit
$('#method_step .add-method-step-item').click(function (event) {
    let methodStep = `<li class="collection-item">
                            <a class="remove-list-item">
                                <i class="fas fa-times"></i>
                            </a>
                            <div class="input-field">
                            <textarea name="method_step" class="materialize-textarea" required></textarea>
                            <label for="method_step">Step Description</label>
                            </div>
                        </li>`;
    $(this).parent().before(methodStep)
});

// Remove Method step item on click
$('#method_step').on("click", ".remove-list-item", function (event) {
    $(this).parent().remove();
});