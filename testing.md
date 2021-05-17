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

<details>
<summary>app.py - inaccurate warnings</summary>

![app.py - inaccurate warnings](assets/validation/python/app.PNG)
</details>

 - unbalanced-tuple-unpacking & unused-variable (per_page, offset): This relates to code used by flask-paginate to automate content pagination. The code was taken directly from their own installation guide, changes to the code causes the site to fail on page load.
 - invalid-name & unused-argument: 'e' is an accepted variable, used to capture errors in error handling functionality.
 - unused-import: 'env' is the local file used to configure the development environment, as it is not pushed to live via .gitignore, pylint is incorrectly believing the function is not used.

To clean up these false positives, I created a .pylintrc file and added the below rules to allow for these warning instances. By doing so, my app.py file now returns 10/10 score.

<details>
<summary>.pylintrc</summary>

![.pylintrc](assets/validation/python/pylintrc.PNG)
</details>



### Google Lighthouse Audit

I used Google's lighthouse audit to test the website conforms positively with Google's performance metrics, intending to achieve scores of 90% in all areas on desktop.

After running the audit, the site recieved the below scores;
![Google Lighthouse Audit](assets/validation/google-lighthouse-audit/GLA.PNG)

This shows 90%+ scores in accessibility and best practices, but sub 90% in performance and SEO. Upon checking the reasoning for the low Performance and SEO scores, I decided to not take further action to improve the scores for the below reasons;

<details>
<Summary>Performance</Summary>

![Performance Score](assets/validation/google-lighthouse-audit/performance.PNG)

The driving factors to the low performance score are the 'Elminate Render Blocking Resources' and 'Remove Unused JavaScript', however the sources driving these are third party, such as Materialize and jQuery. Therefore as the underlying cause is due to third party, no further on-site optimisation is suitable.

</details>
<details>
<Summary>SEO</Summary>

![Performance Score](assets/validation/google-lighthouse-audit/SEO.PNG)

The two driving factors in the low SEO score are 'uncrawlable links' and 'robots.txt is not valid'. The uncrawable links are the pagination links on the recipes page, which are auto-generated by by flask-pagination. These links are not necessarily needed for crawling, as a properly optimised robots.txt file will ensure as each individual recipe page (recipe-details) would be crawled by search engines.

The invalid robots.txt is being flagged, as since this is a personal project, no robots.txt file has been created. If this project were for commercial or public purposes, a robots.txt file should be created, which will direct search engines how to properly index every page of the site and allow it to show in search results.

As this project is not to be crawled by search engines, no robots.txt has been created.

</details>

## Responsive Device & Browser Testing

To test the responsiveness of the site I used [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools), [Responsive Design Checker](https://www.responsivedesignchecker.com/) and [Lambdatest](https://www.lambdatest.com/).

### Responsiveness
![Desktop Responsive Testing](assets/validation/responsiveness/desktop.PNG)

![Tablet Responsive Testing](assets/validation/responsiveness/tablet.PNG)

![Mobile Responsive Testing](assets/validation/responsiveness/mobile.PNG)

To ensure responsive I used materialize grid, flexbox methods, containers and custom media queries add_to ensure all site pages resized responsively for all device viewports.

### Browser Compatibility
![Browser Campatibility Testing](assets/validation/browser-compatibility/browser-testing.PNG)

Through testing, I found some bug on the Safari desktop browser versions, where the 'WebP' image format would not load, this is because [Safari only support WebP image format in version 14 onwards](https://www.keycdn.com/support/webp-browser-support#:~:text=Safari%20will%20support%20WebP%20in,almost%20be%20completely%20globally%20supported.). As version 14 was only released in September 2020, I opted to convert the images to png and re-upload, ensuring wider user compatability.

Additionally, the site does not load properly while using Internet Explorer, due to issues with Materialize CSS compatibility.

According to caniuse the current usage of Internet Explorer is just 1.1% of total browser users, therefore I am comfortable not supporting IE in the site design.

Note: Microsoft released Internet Explorer in 2013 and ceased active development in 2015 when Microsoft Edge was released as the replacement, as evidenced by this article from Microsoft's design team. Since 2015 Microsoft has been actively encouraging users to adopt Edge over Explorer, with the only remaining updates for IE, being security patches and bug fixes.

## Testing User Stories
<details>
<summary>Browsing</summary>

* \(US001\) - As a user I want the website to clearly display recipe suggestions to me so I can be introduced to new content.
   - When a user visits the website, the first page they visit displays latest recipes added to the site and a search function, to browse for specific recipes the user may wish to find.
   - When a user logs in to their account, their profile page displays their favourited recipes and uploaded recipes.
* \(US002\) - As a user I want to see recipe reviews and comments from other users, so I am informed of the best recipes.
   - *** add if time ***
</details>
<details>
<summary>Searching</summary>

* \(US003\) - As a user, I want to be able to view recipes by category, so I can find recipes of specific type I would like to make.
   - The search function on the home page allows users to filter recipes by category.
* \(US004\) - As a user, I want to be able to search recipes by keyword, so I can find recipes easily, for example by name or by included ingredient.
   - The search function on the home page allows users to search recipes by keyword. This function will search through the indexed recipe_title, category_name and ingredients, elements of the recipes database category.
* \(US005\) - As a user, I want to be able to search and filter recipes by rating, so I can find only the highest-rated recipes to choose from.
   - The search function on the home page allows users to filter recipes by minimum rating.
* \(US006\) - As a user, I want to be able to search and filter recipes by serving size, so I can find recipes suited to the number of people I am catering to.
   - The search function on the home page allows users to filter recipes by serving size.
* \(US007\) - As a user, I want to be able to search and filter recipes by preparation and cooking time, so I find recipes that are suitable to my available time.
   - *** REMOVE ***
* \(US008\) - As a user, I want to be about to save my favourite recipes, so I can quickly find them again in future.
   - On each recipe page, there is a heart logo in the top right of the recipe image - toggling the hear to appear filled adds this recipe to user favourites.
</details>

<details>
<summary>Uploading Recipes</summary>

* \(US009\) - As a user, I want to be able to upload my own recipes, so other users can benefit from them.
   - Logged in users can add new recipe's to the site via the link in the navigation bar. The form input fields inform the user of required information.
* \(US010\) - As a user, I want to gain feedback on the recipes I upload, so I can determine improvements.
   - Recipes uploaded to the site can be rated by other users, so users will be able to see the current star rating of their uploaded recipes.
* \(US011\) - As a user, I want to be able to edit and improve recipes I have already uploaded.
   - Logged in users can edit their uploaded recipes via the 'uploaded' list on their user profile page.
</details>

<details>
<summary>Users</summary>

* \(US012\) - As a user, I want to be able to register with the site, so I can upload and edit recipes, plus save my favourite recipes.
   - Users can register as user profile via the 'registration' page, which informs users of required username and password formatting.
* \(US013\) - As a registered user, I want to be able to login to my account, so I can access and edit my recipes, and find my favourite recipes.
   - Users with registered accounts, can login to their account via the 'Login' page, using their registered username and password.
* \(US014\) - As a registered user, I want to be able to submit ratings and reviews for recipes submitted by other users.
   - Logged in users can submit star ratings for recipes via viewing the recipe detail pages. If you have previously rated a recipe, your previous rating score will display.
</details>

<details>
<summary>Administration</summary>

* \(US015\) - As an admin I want to be able to edit content, to ensure it adheres to site rules.
   - If the logged in user has the role of 'admin' the 'uploaded' list is replaced with a list of all recipes, this allows the admin to edit all recipes added to the site.
* \(US-16\) - As an admin I want to be able to add and edit food categories, to continuously improve user experience.
   - If the logged in user has the role of 'admin', the 'Manage Categories' link will be visible in the navigation bar. The 'Manage Categories' page shows all categories added to the site, plus options and edit and delete them.
</details>

<details>
<summary>General</summary>

* \(US013\) - As a user I want to recieve clear feedback for my actions on the site, so I know they are complete or if further steps are needed.
   - Where appropriate, visual responses have been added to confirm success or failure of user interaction events, including;
      - When a user registers with the site, a flash message is shown advising on successful/failed registration.
      - When a user logs in to the site, a flash message is shown welcoming the user to their login page, showing their username. If login is unsuccessful, a flask message shows advising so.
      - When a user adds a new recipe to the site or edits an existing recipe, a flash message is displayed advising of successful/failed update.
      - When a user rates a recipe, a gif is displayed showing successful submission of their rating.
      - When a user favourites a recipe, the heart logo displays in a 'filled' state, indicating the recipe is on the users favourite list.
</details>
&nbsp;

## Issues I had to overcome
- Cloudinary Widget and Image upload
- Materialize List Resizing
- Favourite Form Submission - AJAX
- Pagination
- Edit recipe, page posting.
- WebP format and Safari

## Issues still to overcome
- Forgotten Password
- User/Admin search Function.
- Optimised image delivery
- Restrict file upload type to .png and .jpg

