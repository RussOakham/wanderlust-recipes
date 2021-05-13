# Wanderlust Recipes Testing

1. [**Validation**](testing.md#validation)
   * [**HTML**](testing.md#w3-html)
   * [**CSS**](testing.md#w3-css)
   * [**JavaScript**](testing.md#javascript)
   * [**Google Lighthouse Audit**](testing.md#google-lighthouse-audit)
2. [**Responsive Device Browser Testing**](testing.md#responsive-device--browser-testing)
   * [**Responsiveness**](testing.md#responsiveness)
   * [**Browser Compatibility**](testing.md#browser-compatibility)
3. [**Testing User Stories**](testing.md#testing-user-stories)
4. [**Issues I had to overcome**](testing.md#issues-i-had-to-overcome)
5. [**Issues still to overcome**](testing.md#issues-still-to-overcome)

## Validation

### W3 HTML

I validated the HTML with [W3 Validation Service](https://validator.w3.org/). The results can be seen below;

<details>
<summary>base.html & recipes.html</summary>

![Base & Recipes](assets/validation/html/recipes.PNG)
</details>
<details>
<summary>add-recipe.html</summary>

![Add Recipe](assets/validation/html/add-recipe.PNG)
</details>
<details>
<summary>edit-categories.html</summary>

![Edit Categories](assets/validation/html/edit-categories.PNG)
</details>
<details>
<summary>edit-recipe.html</summary>

![Edit Recipe](assets/validation/html/edit-recipe.PNG)
</details>
<details>
<summary>login.html</summary>

![Login](assets/validation/html/login.PNG)
</details>
<details>
<summary>manage-categories.html</summary>

![Manage Categories](assets/validation/html/manage-categories.PNG)
</details>
<details>
<summary>profile.html</summary>

![Profile](assets/validation/html/profile.PNG)
</details>
<details>
<summary>recipe-details.html</summary>

![Recipe Details](assets/validation/html/recipe-details.PNG)
</details>
<details>
<summary>register.html</summary>

![Register](assets/validation/html/register.PNG)
</details>
<details>
<summary>search.html</summary>

![Search](assets/validation/html/search.PNG)
</details>

**Warnings**
All pages showed warnings regarding HTML semantics and use H2-6's in sections, however upon review I am happy that all headings are relevant for page layout. So I decided not to enact any changes.

<details>
<summary>H2-6 Warning</summary>

![HTML Warnings](assets/validation/html/html-warning.PNG)
</details>

### W3 CSS

I validated the CSS with the [w3 Validation Service](https://jigsaw.w3.org/css-validator/) and it found no errors.

<details>
<summary>CSS Validation</summary>

![Style.css](assets/validation/css/style.PNG)
</details>

### JavaScript

I validated the JavaScript with [JSHint](https://jshint.com/).

<details>
<summary>Script.js</summary>

![script.js](assets/validation/js/script.PNG)
</details>
<details>
<summary>ajax-form-submission.js</summary>

![ajax-form-submission.js](assets/validation/js/ajax-form-submission.PNG)
</details>
<details>
<summary>created-on-timestamp.js</summary>

![created-on-timestamp.js](assets/validation/js/created-on-timestamp.PNG)
</details>
<details>
<summary>recipe-image-upload.js</summary>

![recipe-image-upload.js](assets/validation/js/recipe-image-upload.PNG)
</details>

  The recipe-image-upload flagged an inaccurate issue with an undefined variable, however this is because the variable is called from a third-party application (cloudinary).

### Python

I validated the Python code with the [Pylint Validation Tool](https://www.pylint.org/), which found a number of simple errors I corrected.
The final validation marks are below, scoring 10/10 for all files.

<details>
<summary>app.py</summary>

![app.py](assets/validation/python/app-2.PNG)
</details>
<details>
<summary>user_management.py</summary>

![user_management.py](assets/validation/python/user_management.PNG)
</details>
<details>
<summary>user_rating.py</summary>

![user_rating.py](assets/validation/python/user_rating.PNG)
</details>

**Warnings and Errors Fixed**
On initial running of pylint, it flagged that I had not included Docstring descriptions for each of my functions, as I had used '#' notes instead. Additionally Pylint flagged a few occasions of poor syntax, such as imbalanced returns and use of unnecessary 'else' statements.
Based off Pylints feedback, I corrected these issues quickly and easily.

**.pylintrc**
After the above corrections, Pylint was still displaying a handful of warnings related to the app.py file, however these were false positive results for the following reasons:

<summary>app.py - inaccurate warnings</summary>

![app.py - inaccurate warnings](assets/validation/python/app.PNG)
</details>

 - unbalanced-tuple-unpacking & unused-variable (per_page, offset): This relates to code used by flask-paginate to automate content pagination. The code was taken directly from their own installation guide, changes to the code causes the site to fail on page load.
 - invalid-name & unused-argument: 'e' is an accepted variable, used to capture errors in error handling functionality.
 - unused-import: 'env' is the local file used to configure the development environment, as it is not pushed to live via .gitignore, pylint is incorrectly believing the function is not used.

To clean up these false positives, I created a .pylintrc file and added the below rules to allow for these warning instances. By doing so, my app.py file now returns 10/10 score.

<summary>.pylintrc</summary>

![.pylintrc](assets/validation/python/pylintrc.PNG)
</details>



### Google Lighthouse Audit

I used Google's lighthouse audit to test the website conforms positively with Google's performance metrics, intending to achieve scores of 90% in all areas on desktop.

## Responsive Device & Browser Testing

To test the responsiveness of the site I used [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools), [Responsive Design Checker](https://www.responsivedesignchecker.com/) and [Lambdatest](https://www.lambdatest.com/).

### Responsiveness

To ensure responsive I used bootstrap, flexbox methods and containers to ensure all site pages resized responsively for all device viewports.

### Browser Compatibility

## Testing User Stories

## Issues I had to overcome

## Issues still to overcome

