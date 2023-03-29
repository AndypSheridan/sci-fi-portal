# Testing

* [**Testing Overview**](#testing-overview)
* [**Bugs**](#bugs)
* [**Lighthouse**](#lighthouse)
  * [**Home Page**](#home-page)
    * [*Desktop*](#home-desktop)
    * [*Mobile*](#home-mobile)
  * [**Books Page**](#books-page)
    * [*Desktop*](#books-desktop)
    * [*Mobile*](#books-mobile)
  * [**Authors Page**](#authors-page)
    * [*Desktop*](#authors-desktop)
    * [*Mobile*](#authors-mobile)
  * [**About Page**](#about-page)
    * [*Desktop*](#about-desktop)
    * [*Mobile*](#about-mobile)
  * [**Profile Page**](#profile-page)
    * [*Desktop*](#profile-desktop)
    * [*Mobile*](#profile-mobile)
  * [**Book Detail**](#book-detail-page)
    * [*Desktop*](#book-detail-desktop)
    * [*Mobile*](#book-detail-mobile)
  * [**Author Detail**](#author-detail-page)
    * [*Desktop*](#author-detail-desktop)
    * [*Mobile*](#author-detail-mobile)
  * [**Add Book Page**](#add-book-page)
    * [*Desktop*](#add-book-desktop)
    * [*Mobile*](#add-book-mobile)
  * [**Edit Book Page**](#edit-book-page)
    * [*Desktop*](#edit-book-desktop)
    * [*Mobile*](#edit-book-mobile)
  * [**Delete Book**](#delete-book-page)
    * [*Desktop*](#delete-book-desktop)
    * [*Mobile*](#delete-book-mobile)
  * [**Search Results Page**](#search-results-page)
    * [*Desktop*](#search-results-desktop)
    * [*Mobile*](#search-results-mobile)
  * [**Sign Up Page**](#signup-page)
    * [*Desktop*](#signup-desktop)
    * [*Mobile*](#signup-mobile)
  * [**Log In Page**](#login-page)
    * [*Desktop*](#login-desktop)
    * [*Mobile*](#login-mobile)
  * [**Log Out Page**](#logout-page)
    * [*Desktop*](#logout-desktop)
    * [*Mobile*](#logout-mobile)
* [**Validation**](#validation)
  * [**HTML**](#html)
  * [**CSS**](#css)
  * [**JavaScript**](#javascript)
  * [**Python / Django**](#python--django)
* [**User Story Testing**](user-story-testing)


<hr>

## **Testing Overview**

At the time of writing this is the largest project I had undertaken so I felt the testing process needed to be as thorough as possible. The Sci-Portal was tested on a variety of devices including a MacBook Pro 2021, a MacBook Air 2020, an iPad Air 2020, iPhone 12, iPhone SE, Dell Desktop with 24" Screen, Kindle Fire and a Samsung Galaxy Tablet.

The majority of User testing was conducted by myself, however I enlisted the help of family and several work colleagues, essentially to try to break the site or help me identify bugs and areas for improvement.

All buttons and links were clicked multiple times to test they functioned as expected. Multiple test reviews were created, edited and deleted to check the efficacy of the CRUD (create, read, update and delete) functionality across the site.

Inevitably there were bugs and these are outlined and summarised below.

Full details of manual testing can be found on this page.

<hr>

## **Bugs**
​
The following bugs were identified during user testing:

* Bug 🐞 - When running the search function, it would display results from books which had not yet been published and therefore resulted in an error.
* Cause ⚒️ - Whilst the search function worked as intended, I had not set a specific condition for which results could be displayed.
* Resolution ✅ - Added an if statement that would only display results if the Book status was set to published.

<br>

* Bug 🐞 - Logging in would redirect the User to the Books page.
* Cause ⚒️ - This was what I had set the login redirect to do during the initial stages of the project before the inception of the Search Function.
* Resolution ✅ - Adjust login redirect in settings.py

​<br>

* Bug 🐞 - An error message was displayed when submitting the 'add book' form after setting the 'created_by' field to hidden.
* Cause ⚒️ - The field was removed so that Users could not submit reviews as other Users. This meant the field, which is required, would be empty and thus result in the error and the form failing to submit.
* Resolution ✅ - Used some simple JavaScript code to pre-populate the 'created_by' field with the logged-in User id.

<br>

* Bug 🐞 - The front end method for Users to add Book or Profile images did not work.
* Cause ⚒️ - Lack of familiarity with, and knowledge of the Cloudinary platform.
* Resolution ✅ - Researched the various methods to upload and save images to Cloudinary and add Cloudinary fields to forms.

<br>

* Bug 🐞 - Error messages displayed after creating the UserProfile class.
* Cause ⚒️ - As the UserProfile class was added after several Users had already been created, no profiles were linked to their accounts.
* Resolution ✅ - Used the Admin page to assign profiles to Users by using the drop-down menu.

<br>

* Bug 🐞 - When setting debug=False in settings.py, and removing DISABLE_COLLECTSTATIC from Heroku Config Vars, project would not deploy.
* Cause ⚒️ - Heroku failed to collect static files due to a conflict between Whitenoise and Cloudinary.
* Resolution ✅ - Removed Whitenoise and ran the deployment again.

<br>

* Bug 🐞 - Initial deployment of Django app failed.
* Cause ⚒️ - There was a typo in the settings.py file.
* ✅ - Corrected typo.

<br>

* Bug 🐞 - Users were unable to register without providing a valid email address, something I did not deem necessary for this project.
* Cause ⚒️ - Email was set to required in settings.py.
* ✅ - Adjusted the settings to remove the need for an email address. The User can still choose to provide one if they wish.

<br>

* Bug 🐞 - Lighthouse scores for some pages were poor.
* Cause ⚒️ - There were several reasons for reduced performance but the main one seemed to eminate from an issue with jQuery.
* ✅ - Removed jQuery from the app.


<hr>

## **Unfixed Bugs**

* At this stage, there are no known unfixed bugs.

<hr>

## Lighthouse**

The Lighthouse test results for all major pages can be found below. The Mobile scores are generally lower in terms of performance with the reason being some issues with the Bootstrap CDN and the images used. The majority of these images were already compressed to what I felt was an acceptable limit. Some of the lower scores are as a result of the Cloudinary integration and issues with cookies which I feel were beyond my control here.

### Home Page

*Desktop*

![Home page desktop lighthouse](docs/validation/index-lighthouse.png)

*Mobile*

![Home page mobile lighthouse](docs/validation/index-lighthouse-mobile.png)

### Books Page

*Desktop*

![Books page desktop lighthouse](docs/validation/books-lighthouse-1.png)

*Mobile*

![Books page mobile lighthouse](docs/validation/books-lighthouse-mobile.png)

### Authors Page

*Desktop*

![Authors page desktop lighthouse](docs/validation/authors-lighthouse.png)

The lower 'best practice' score is as a result of the following which is a cookie issue related to Cloudinary:

![Best practice score](docs/validation/authors-lighthouse-bp.png)

*Mobile*

![Authors page mobile lighthouse](docs/validation/authors-lighthouse-mobile.png)

### About Page

*Desktop*

![About page desktop lighthouse](docs/validation/about-lighthouse.png)

*Mobile*

![About page mobile lighthouse](docs/validation/about-lighthouse-mobile.png)

### Profile Page

*Desktop*

![Profile page desktop lighthouse](docs/validation/profile-lighthouse.png)

*Mobile*

![Profile page mobile lighthouse](docs/validation/profile-lighthouse-mobile.png)

### Book Detail Page

*Desktop*

![Book Detail page desktop lighthouse](docs/validation/book-detail-lighthouse1.png)

The reasons for the reduced 'best practices' score can be seen below:

![Book detail best practice lighthouse](docs/validation/book-detail-lighthouse-bp.png)

In the above instance, the image proportions are as intended and I found no lack of clarity during testing.

![Book detail best practice lighthouse 2](docs/validation/book-detail-lighthouse-bp-2.png)

The above instance again flags issue to do with cookies and Cloudinary which I felt were beyond my control given the time constraints. They do not affect the performance or appearance of the page.

*Mobile*

![Book Detail page mobile lighthouse](docs/validation/book-detail-lighthouse-mobile.png)

### Author Detail Page

*Desktop*

![Author Detail page desktop lighthouse](docs/validation/author-detail-lighthouse.png)

*Mobile*

![Author Detail page mobile lighthouse](docs/validation/author-detail-lighthouse-mobile.png)

### Add Book Page

*Desktop*

![Add Book page desktop lighthouse](docs/validation/submit-review-lighthouse.png)

*Mobile*

![Add Book page mobile lighthouse](docs/validation/submit-review-lighthouse-mobile.png)

### Edit Book Page

*Desktop*

![Edit Book page desktop lighthouse](docs/validation/edit-book-lighthouse.png)

*Mobile*

![Edit Book page mobile lighthouse](docs/validation/edit-review-lighthouse-mobile.png)

### Delete Book Page

*Desktop*

![Delete Book page desktop lighthouse](docs/validation/delete-lighthouse.png)

*Mobile*

![Delete Book page mobile lighthouse](docs/validation/delete-lighthouse-mobile.png)

### Search Results Page

*Desktop*

![Search Results page desktop lighthouse](docs/validation/search-lighthouse.png)

*Mobile*

![Search Results page mobile lighthouse](docs/validation/search-lighthouse-mobile.png)

### Signup Page

*Desktop*

![Signup page desktop lighthouse](docs/validation/signup-lighthouse.png)

*Mobile*

![Signup page mobile lighthouse](docs/validation/signup-lighthouse-mobile.png)

### Login Page

*Desktop*

![Log in page desktop lighthouse](docs/validation/login-lighthouse.png)

*Mobile*

![Log in page mobile lighthouse](docs/validation/login-lighthouse-mobile.png)

### Logout Page

*Desktop*

![Log out page desktop lighthouse](docs/validation/logout-lighthouse.png)

*Mobile*

![Log out page mobile lighthouse](docs/validation/logout-lighthouse-mobile.png)

<hr>


## **Validation**

### **HTML**

The code for all pages was run through the [W3C HTML Markup Validation Service](https://validator.w3.org/). Ultimately several pages needed to be entered as text due to the User Authentication features used across the site. This meant having to remove the Jinja templating language as it resulted in errors in any instance where it was still present in the code.

Results from the validation can be seen below:

#### ***Home Page***

![Home page HTML validation](docs/validation/sfportal-home-html-validation.png)

#### ***Books Page***

![Books page HTML validation](docs/validation/sfp-books-html-validation.png)

#### ***Authors Page***

![Authors page HTML validation](docs/validation/sfp-authors-html-validation.png)

#### ***About Page***

![About page HTML validation](docs/validation/sfportal-about-html-validation.png)

#### ***Profile Page***

![Profile page HTML validation](docs/validation/sfp-profile-html-validation.png)

#### ***Book Detail Page***

![Book Detail page HTML validation](docs/validation/sfp-book-detail-html-validation.png)

#### ***Author Detail Page***

![Author Detail page HTML validation](docs/validation/sfp-author-detail-html-validation.png)

#### ***Add Book Page***

![Add book page HTML validation](docs/validation/add-book-html-validation.png)

#### ***Edit Book Page***

![Edit book page HTML validation](docs/validation/edit-book-html-validation.png)

#### ***Delete Book Page***

![Delete book page HTML validation](docs/validation/sfp-delete-book-html-validation.png)

#### ***Signup Page***

![Signup page HTML validation](docs/validation/sfp-signup-html-validation.png)

#### ***Login Page***

![Login page HTML validation](docs/validation/sfp-login-html-validation.png)

#### ***Log Out Page***

![Log Out page HTML validation](docs/validation/sfp-logout-html-validation.png)


<hr>

### ***CSS***

The custom CSS code was passed through the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/). The result can be seen below:

![CSS Validation Result](docs/validation/sfp-css-certificate.png)


<hr>

### ***JavaScript***

Although there is very little JavaScript in this code, I ran it through the [JSHint Validation Service](https://jshint.com/). The result can be seen below:

![JS Validation Result](docs/validation/sfp-js-validation.png)


<hr>

### ***Python / Django ***

The PEP8 Online Validator was down when creating this project, however I added a PEP8 validator to my workspace by running the command: "pip3 install pycodestyle". The validator identified the errors in the following files:

![PycodeStyle Results views.py](docs/validation/views-py-errors.png)


This highlights an error in line length which I was unable to rectify without breaking the code. I decided against changing it.

![PycodeStyle Results settings.py](docs/validation/settings-py-errors.png)


Again there are issues with line length but I was reluctant to change anything in this file. I surmised that as this was the default code, it was better to leave it in place.

![PycodeStyle Results env.py](docs/validation/env-py-errors.png)

The final errors displayed also related line length. I was unsure how to remedy this without compromising the code in the env.py file so overlooked this too.


<hr>

## **Manual Testing**

### User Stories

#### As a Site Admin I can:

* User Story 📖: Create draft Book posts in order to publish them at a later time
* Test 🧪: The admin panel was used to create Test Book Reviews and set the status to either draft or published
* Result 🏆: The Book status was updated as intended
* Verdict ✅: Test passed.

<br>

* User Story 📖: Add to, or remove from, the Authors section in order to keep content fresh and relevant
* Test 🧪: The admin panel was used to add or remove authors along with date of birth, bios, images and famous works.
* Result 🏆: Creating and deleting authors functioned as intended.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Delete a User account in order remove Users who do not respect who do not respect others in the community.
* Test 🧪: The delete User option was selected from the dropdown menu in the admin panel in order to delete Test Users
* Result 🏆: Users were deleted as intended.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Approve or disapprove book reviews in order to check their content is appropriate.
* Test 🧪: Logging in as a Test User, I added a Book Review using the front end method. The Review did not appear in the Books page as the default setting was 'Draft'. By logging in as the Admin, I was able to set the status to 'Published' using the drop down menu.
* Result 🏆: The Book Review was approved and published as intended.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Approve or disapprove comments in order to filter out objectionable content.
* Test 🧪: Logging in as a Test User, I added a comment to a Book Review. The confirmation message informed me the comment must be approved by the Admin. When I logged into the Admin panel, I was able to approve the comment or choose not to.
* Result 🏆: The comment was approved and posted to the relevant Book Review.
* Verdict ✅: Test passed.

<br>

* User Story 📖: View the number of likes on a post or comment in order to see which is the most popular.
* Test 🧪: Logging in as the Admin, I checked the Books list for the 'number of likes' field.
* Result 🏆: The field was not present.
* Verdict ❌: Test failed.
* Solution 🔍: Add 'number_of_likes' to BookAdmin list display in admin.py
* Verdict ✅: Test passed.

<hr>

#### As an Unregistered Site User I can:

* User Story 📖: Easily determine the purpose of the site in order to see if I want to sign up to it.
* Test 🧪: Navigating to the Home Page I was presented with a simple, but attractive Home Page welcoming me to the site and a brief description that it was an online community devoted to Science Fiction literature
* Result 🏆: I found the appearance appealing and wanted to sign up.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Register for an account in order to view and interact with content on the site.
* Test 🧪: Navigating to the Home Page I clicked the 'Register' button and was taken to the Sign Up Page. I tried entering invalid information and the Usernames I already knew existed.
* Result 🏆: Invalid data was not accepted, nor were dupliacted Usernames. I was informed if passwords were too short or obvious. When the valid data was passed, registration was successful and I was logged in and redirected to the Home Page.
* Verdict ✅: Test passed.

<hr>

#### As a Registered Site User I can:


* User Story 📖: Easily Log In to my account.
* Test 🧪: When logged out, I navigated to the Home Page and clicked the Log In button on the page.
* Result 🏆: I entered my details and clicked the Log In button to be redirected to the full Home Page. In subsequent visits, my devices had auto-filled the login fields and this provided an even smoother login experience.
* Verdict ✅: Test passed.

<br>

* User Story 📖: View a list of book posts in order to select one to read.
* Test 🧪: Logging in as a Test User, I navigated to the Books Section of the site to see a list of Book Reviews. 
* Result 🏆: The list of Books displayed in a paginated list of 6 as intended.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Click on a Book Review in order to view all of its content
* Test 🧪: Logging in as a Test User, I navigated to the Books Section of the site to see a list of Book Reviews. I clicked on each review in order to view more details and the review itself.
* Result 🏆: When clicking on each review, I was able to view more about the Book and read the User's Book Review.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Create posts of my own in order to share my review with the community.
* Test 🧪: Logging in as a Test User, I navigated to the Books Section of the site to see a list of Book Reviews. I clicked on the 'Submit Review' button and completed the form on the 'Add Book' page. I completed the form and uploaded an image.
* Result 🏆: Upon submission of the form, a message informed me the Review had been submitted for approval by the Admin. When logging in as Admin and approving the Review, it displayed on the Books page as intended.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Edit or delete my book posts in order to keep my own contributions relevant.
* Test 🧪: When logged in, 'Edit' and 'Delete' buttons were present on reviews I had written on both the Books and Book Detail pages. Clicking 'Edit' directed me to the 'Edit Review' form which I could update accordingly. If I clicked 'Delete' I was asked for confirmation.
* Result 🏆: Submitting the Update Review form displayed a message informing me the review had been updated and the new content displayed. Confirming deletion removed the Book Review from the site and database.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Comment on other users' posts in order to interact with the community.
* Test 🧪: Logging in as a Test User, I navigated to the Books Section of the site to see a list of Book Reviews. On the Book Detail page, I added a comment using the form at the bottom of the page and clicked 'Submit'. A message provided feedback and informed me the comment must be approved by the Admin.
* Result 🏆: Logging in as the Admin, I was able to approve the comment and it displayed on the corresponding Book Detail page as intended.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Like or unlike posts and comments in order to interact with the site content.
* Test 🧪: Logging in as a Test User, I navigated to the Books Section of the site to see a list of Book Reviews. On the Book Detail page, I clicked the 'Like' button.
* Result 🏆: The outline heart icon changed to a solid red heart. If I clicked the button again, it reverted to the previous state.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Add to and / or update my profile in order to keep my account up-to-date.
* Test 🧪: Logging in as a Test User, I navigated to the Profile Page and saw that the User Profile had been created automatically when registering. A card and hidden form were both pre-populated with the information I provided when registering. I completed the form and clicked 'Update' at the bottom of the page. 
* Result 🏆: Feedback was provided by a message informing me that the profile had been updated and the corresponding information was displayed in the card.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Upload a profile image in order to express myself within the community.
* Test 🧪: On the Profile Page, I clicked the 'Edit Profile' button and added an image using the field in the form.
* Result 🏆: Feedback was provided by a message informing me that the profile had been updated and the corresponding photograph was displayed in the card.
* Verdict ✅: Test passed.

<br>

* User Story 📖: Easily Log Out of my account.
* Test 🧪: When logged in, I navigated to 'Log Out' in the Navbar or Hamburger Menu (depending on the device).
* Result 🏆:  Clicking the Log Out link took me to the Log Out page where I was prompted for confirmation I wanted to do so. Upon clicking the button I was logged out and redirected to the logged-out version of the Home Page. A message informed me I had successfully logged out.
* Verdict ✅: Test passed.


<hr>

## Addditional Testing

* Aim 🎯: Test 404 Page.
* Test 🧪: When logged in, I added the URL of a page of a deleted Book Review. 
* Result 🏆:  The custom 404 page was displayed.
* Verdict ✅: Test passed.

* Aim 🎯: Test 500 Page.
* Test 🧪: When logged out, I pasted the URL of the Profile, Edit and Delete pages into the browser.
* Result 🏆: The custom 500 page was displayed.
* Verdict ✅: Test passed.
​
<hr>

Back to [README](/README.md)