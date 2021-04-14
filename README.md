# Wanderlust Recipes - by Russell Oakham

## Project overview

'Wanderlust Recipes' is a community-focused website, where user accounts can create, share and review recipe ideas.

The site is created to engage users of all ages and backgrounds, so is branded in a light, clean and neutral style. Additionally, the term 'Wanderlust' is defined as a ['lust for wandering'](https://www.merriam-webster.com/dictionary/wanderlust), so styling elements have been chosen to promote curiosity and exploration.

## Deployed site

## Table of Contents

1. [**UX**](./#1-ux)
   * [**User-Stories**](./#user-stories)
   * [**Structure**](./#structure)
   * [**Skeleton**](./#skeleton)
   * [**Surface**](./#surface)
2. [**Features**](./#2-features)
   * [**Existing Features**](./#existing-features)
   * [**Features to consider in future**](./#features-to-consider-implementing-in-future)
3. [**Technologies Used**](./#3-technologies-used)
4. [**Testing**](./#4-testing)
5. [**Deployment**](./#5-deployment)
   * [**GitHub Pages**](./#github-pages)
6. [**Credits**](./#6-credits)
   * [**Design and Research**](./#design-and-research)
   * [**Technical**](./#technical)
   * [**Content**](./#content)
   * [**Media**](./#media)
   * [**Acknowledgements**](./#acknowledgements)

## 1. UX

Overview of UX decisions, structure etc. Examples of websites I have viewed as part of research & resulting UX design decisions.

### User Stories

#### Browsing

* \(US001\) - As a user I want the website to clearly display recipe suggestions to me so I can be introduced to new content.
* \(US002\) - As a user I want to see recipe reviews and comments from other users, so I am informed of the best recipes.

#### Searching

* \(US003\) - As a user I want to be able to view recipes by category, so I can find recipes of specific type I would like to make.
* \(US004\) - As a user I want to be able to search recipes by keyword, so I can find recipes easily, for example by name or by included ingredient.
* \(US005\) - As a user I want to be able to search and filter recipes by rating, so I can find only the highest rated recipes to choose from.
* \(US006\) - As a user I want to be able to search and filter recipes by serving size, so I can find recipes suited to he number of people I am catering to.
* \(US007\) - As a user I want to be able to search and filter recipes by preparation and cooking time, so I find recipes which are suitable to my available time.
* \(US008\) - As a user, I want to be about to save my favourite recipes, so I can quickly find them again in future.

#### Uploading Recipes

* \(US009\) - As a user, I want to be able to upload my own recipes, so other users can benefit from them.
* \(US010\) - As a user, I want to gain feedback on the recipes I upload, so I can determine improvements.
* \(US011\) - As a user, I want to be able to edit and improve recipes I have already uploaded.

#### Users

* \(US012\) - As a user, I want to be able to register with the site, so I can upload and edit recipes, plus save my favourite recipes.
* \(US013\) - As a registered user, I want to be able to login to my account, so I can access and edit my recipes, and find my favourite recipes.
* \(US014\) - As a registered user, I want to be able to submit ratings and reviews for recipes submitted by other users.

#### Administration

* \(US015\) - As an admin I want to be able to edit content, to ensure it adheres to site rules.
* \(US-16\) - As an admin I want to be able to add and edit food categories, to continuously improve user experience.

#### General

* \(US013\) - As a user I want to recieve clear feedback for my actions on the site, so I know they are complete or if further steps are needed.

### Structure

* **Home Page**:
  * _Header/Footer_: For easy navigation across the site and to external resources such as social media pages.
  * _Website Logo_: To easily identify the 'Avengers Snap' game branding.
  * _Recipe Cards_: To easily provide users key information on featured recipes, including visual image, short description, user rating, serving size and prep/cook times.
  * _Pagination_: Page is paginated after 7 recipes are displayed, to ensure quick page load and easy user navigation.
* **Recipe Page**:
  * _Recipe Image_: Provides users a visual of the final recipe, to entice user to want to create it themselves.
  * _Recipe Title_: Provides users the name of the dish, indicating the style and main ingredients of the dish.
  * _Star Rating_: Provides users visual feedback regarding how highly other users have rated the recipe.
  * _Preparation & Cooking Time_: Provides users information on time requirement to prepare the recipe.
  * _Serving Size_: Provides users information on serving size the recipe creates, allowing users to adjust ingrediant amounts on their own judgement.
  * _Ingredient List_: Provides users list of all ingrediants and measures needed to complete the recipe.
  * _Method_: Provides users step-by-step method for creating the dish.
* **Category & Search Page**:
  * _Search Bar_: Text input bar, allowing users to search recipes by keyword.
  * _Category Cards_: On page load, visual cards will display showing all recipe categories, allowing users easy navigation to recipes of that type.
  * _Search Results_: Once user search input, category cards are replayed by recipe cards for all recipes returned by search query.
  * _Pagination_: Page is paginated after 7 recipes are displayed, to ensure quick page load and easy user navigation.
* **User Login / Registration Page**:
  * _Username Input_: Text input box, allowing users to enter their username.
  * _Password Input_: Text input box, allowing users to enter their username.
  * _Submit / Cancel_: Buttons allowing users to submit entered information, or cancel and restart.
* **User Profile Page**:
  * _Username Banner_: Banner displaying username of logged in account, allowing users to quickly identify if they are logged into their correct desired account.
  * _Recipes Submitted_: All historical recipes uploaded by the user displayed in list format, allowing users to easily access their owned recipes for review or edit.
  * _Favourite Recipes_: All favourited recipes are displayed in list format, allowing users quick access.
  * _Pagination_: Page is paginated after 7 recipes are displayed, to ensure quick page load and easy user navigation.
* **New Recipe Page**:
  * _Input areas for below recipe data points_:
    * Recipe Name - Text
    * Recipe Image - file upload and preview
    * Serving Size - Numeric
    * Preparation Time - hh:mm
    * Cooking Time - hh:mm
    * Recipe Category Selection - Radial Menu
    * Recipe Description: Textbox of 50 to 200 characters
    * Ingredients - List
    * Recipe Steps - List

### Skeleton

At this point I began creating wireframes, using the above structure considerations. I used [Balsamiq](https://balsamiq.com/) these below;

* [Home page on desktop and mobile](./)

### Surface

This is the sensory design section of a website, or how it looks, feels and sounds.

#### Colour & Comic Styling

With this in mind I chose to use variations of the below colours for the core design of the website;

#### Language/Tone

I wanted the language to reflect a casual and fun atmosphere, to reflect a backpackers liftstyle, so content was written in line with this. Avoiding technical or formal language where possible.

Similarly, I wanted to use fonts that reinforce casual identity of the site. To achieve this I used two [Google Fonts](https://fonts.google.com/);

* [Font 1](./)
* [Font 2](./)
* Font 3 - Web safe font, used if primary two fonts fail to load.

#### Styling Considerations

Before beginning development, I listed some styling ideas that I felt benefit the website. The majority of these can be seen in the wireframes.

* Favicon: Desktop and Mobile.
* Navigation
  * Sticky top
  * Mobile: 'Burger' menu icon, expanding on click.
  * Logo: Navigates to the home page on click.

## 2. Features

### Existing Features

#### **The Header** includes:

* **Website Logo**: Builds brand awareness amongst users.
* **Navigation Bar**: Allows users to navigate the site easy and intuitively.

#### **The Footer** includes:

* **Website Developer**: Copyright information for website developer brand awareness.
* **Developer Social Links**: Links to GitHub and LinkedIn of website developer for brand awareness.
* **Business Social Links**: Links to company social media sites, to raise for brand awareness.

Both the Header and Footer are present and consistent on all website pages.

#### **Home** page includes:

* **Image Banner**: Visually pleasing design, allowing users to immediately identify the site brand.

### Features to consider implementing in future

## 3. Technologies Used

1. [HTML](https://en.wikipedia.org/wiki/HTML) - Programming language providing content and structure of the website.
2. [CSS](https://en.wikipedia.org/wiki/CSS) - Programming language providing styling of the website.
3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - The programming language used various interactive elements of the website, including game logic, audio options etc.
4. [Bootstrap CSS Framework](https://getbootstrap.com/) - Library of pre-built HTML and CSS components, used for various aspects of the site, such as navigation bar.
5. [Font Awesome](https://fontawesome.com/) - Library used for icons, such as social links and other images.
6. [Google Fonts](https://fonts.google.com/) - Used to choose a font style for the website.
7. [TinyPNG](https://tinypng.com/) & [TinyJPG](https://tinyjpg.com/): To minimise image file sizes and maximise page load speed.
8. [remove.bg](https://www.remove.bg/) - Used to remove backgrounds from png images.
9. [Real Favicon Generator](https://realfavicongenerator.net/) to generate favicons and icons for desktop and mobile usage.
10. [Am I Responsive?](http://ami.responsivedesign.is/) used for responsive design demo in ReadMe summary.
11. [GitHub](https://github.com/) - Remote hosting platform and code repository.
12. [GitPod](https://gitpod.io/) - IDE \(Integrated Development Environment\), for writing, editing and saving code.
13. [Balsamiq](https://balsamiq.com/) - Used for the creation of wireframes for visual design testing.
14. [Autoprefixer](https://autoprefixer.github.io/) - Used to add vendor prefixes to CSS rules.
15. [Responsive Design Checker](https://www.responsivedesignchecker.com/) - Used to check website response across device types.
16. [Lambdatest](https://www.lambdatest.com/) - Used to check website response across device types.
17. [Photopea](https://www.photopea.com/) - Used to create avengers snap page banner image, via layering two pngs together.

## 4. Testing

The testing process can be seen in the [TESTING.md](https://github.com/RussOakham/wanderlust-recipes/tree/20dd255966ec540dc5cf918a15783c3440fe2b9a/TESTING.md) document.

## 5. Deployment

### Hiroku

The site is hosted using Hiroku, deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.

#### Hot to clone 'Avengers-Snap' in GitHub and GitPod.

To run a version of the site locally, you can clone this repository using the following steps;

In a code editor of your choice;

1. Go to [GitHub.com](https://github.com/)
2. Click on 'Responsitories'
3. Click on 'Avengers Snap'
4. Click on the 'Code' button.
5. Under 'HTTPS' click the clipboard icon to the right of the URL.
6. In your IDE of choice, open a repository or create a new repository.
7. Open Terminal \('Terminal' then 'New Terminal' from the top ribbon menu in GitPod.\)
8. Type 'git clone', paste URL link and press enter.

Additional information around these cloning steps can be found on [GitHub Pages Help Page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

## 6. Credits

### Design and research

The following are websites and articles that I used for reference and inspiration:

### Technical

* [Real Favicon Generator](https://realfavicongenerator.net/): For the generation of Favicon icons and code.
* [Bootstrap Docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/): For guidance on Bootstrap use and adaptations.
* [CSS-Tricks](https://css-tricks.com/): For implementing CSS effects such as box-shadow.
* [w3Schools](https://www.w3schools.com/): For checking proper syntax of HTML and CSS elements. 
* [Autoprefixer](https://autoprefixer.github.io/) - For generating CSS browser prefixes.
* [Stackoverflow](https://stackoverflow.com/) - For researching and troubleshooting JavaScript and Python code issues.

### Content

All text content on the site was written originally by myself, with the below notes;

### Media

The colour palette for the site was inspired and adapted from;

The photos and images used for this site were obtained from;

* [**Shutterstock**](https://www.shutterstock.com/): From the following contributors;

### Acknowledgements

* Thanks to my mentor, [Precious Ijege](https://github.com/precious-ijege) for his suggestions, time and support.
* Thanks to those on Slack for reviewing my project and making suggestions.
* Thanks to my housemates, friends and family for reviewing the project and offering constructive feedback.

