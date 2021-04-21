// On document load scripts
$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('select').formSelect();
    $('.tabs').tabs({
        swipeable: true,
        duration: 300,
    });

    // Add Validate to 'Select' inputs in Materlize - Code from Code Instititue Task Manager Mini-Project
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
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