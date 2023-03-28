# **Sci-Fi Portal**
## **Site Overview**

As a keen fan of the Science Fiction genre, I have often found it difficult to keep track of the growing number of books I have read. I have also struggled to find the passion and love for sci-fi from others within my own social or professional circles.

The Sci-Fi Portal is designed with the aim of creating a platform for an online community of like-minded fans who wish to share their own experiences of sci-fi novels, short stories or animé. Users can create, read, update and delete book reviews which can be viewed by themselves as well as other registered users. The community experience is enhanced by the ability to comment on reviews, thus generating discussion and fulfilling one of the aims of providing a forum to interact and engage with other fans of the genre.

<hr>

![Am I Responsive Screenshot](docs/images/am-i-responsive.png)

Click [here](https://sci-fi-portal.herokuapp.com/) to see the final deployment of the site.

<hr>

## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [**Strategy**](#strategy)
      * [***Site Aims***](#site-aims)
      * [***Target Audiences***](#target-audiences)
      * [***User Stories***](#user-stories)
    * [***Wireframes***](#wireframes)
    * [***Database Schema***](#database-schema)
    * [***Color Scheme***](#color-scheme)
    * [***Typography***](#typography)
1. [**Agile Development**](#agile-development)
1. [**Features**](#features)
    * [***Admin Page***](#admin-page)
    * [***Navbar***](#navbar)
    * [***Social Media and Email Links***](#social-media-and-email-links)
    * [***Home Page***](#home-page)
    * [***Books Page***](#books-page)
    * [***Book Detail Page***](#book-detail-page)
    * [***Add Book Page***](#book-detail-page)
    * [***Edit Book Page***](#edit-book-page)
    * [***Delete Book Page***](#delete-book-page)
    * [***Authors Page***](#authors-page)
    * [***Author Detail Page***](#author-detail-page)
    * [***About Page***](#about-page)
    * [***Profile Page***](#profile-page)
    * [***Account Pages***](#account-pages)
      * [***Sign Up***](#sign-up)
      * [***Log In***](#log-in)
      * [***Log Out***](#log-out)
    * [***Messages***](#messages)
    * [***Defensive Programming***](#defensive-programming)
    * [***User Authentication***](#user-authentication)
    * [***404 Page***](#404-page)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Software and Tech**](#software-and-tech)
1. [**Media**](#media)
1. [**Credits**](#credits)
1. [**Honourable mentions**](#honorable-mentions)

<hr>

## **Planning Stage**

### **Site Aims:**

* Develop a colourful, interactive online platform for fans of Science Fiction literature to come together as a community.
* To provide users with a platform to keep track of their own reading within the genre.
* Deliver an accessible and easy to navigate site for users on desktop and mobile devices.
* Provide registered users with the opportunity share their own sci-fi experiences and to Create, Read, Update or Delete book reviews on the site.
* Provide users with an opportunity to gain future reading inspiration by browing the book reviews and featured authors.
* Offer users the opportunity to interact and engage with others by liking and commenting on reviews by other users.
* Ensure provision of safe content as reviews and comments must be approved by the admin.
* Enhance the user experience by using an integrated search function for those trying to find a specific book or author.
* Offer users the opportunity to provide more information about themselves by adding to their user profile.
* Deliver to the user a comprehensive explanation and rationale behind the site through a clear and concise About page. 

<hr>

### **Target Audiences:**

* People who are fans of Science Fiction books.
* People who are fans of the genre in general.
* People looking to share their own reading experiences from within the genre.
* People looking for an online book-club which is easy to sign up to and easy to navigate.
* People who would like to comment on other reviews in order to discuss these books.
* People seeking future reading inspiration.
* People who are new to the genre and would like to engage with the community.

<hr>

### **User Stories:**

#### **Site User**
As a **Registered** user I can: 
* *create draft book posts* in order for *admin to approve and post them after reviewing*.
* *view a list of book posts* in order to *select one to read*.
* *click on a book post* in order to *view its content*.
* *create a book post* in order to *share my review with the community*.
* *comment on other users' book posts* in order to *share my opinions and interact with the community*.
* *upload a profile picture or bio* in order to *tell a little more about myself*.
* *edit or update my profile* in order to *keep my account up to date*.
* *like or unlike a book review* in order to *interact with the site content*.
* *easily login* in order to *access my account*.
* *easily logout* in order to *end my session on the site*.
* *edit or delete my own book post* in order to *keep my own contributions relevant*.

As an **Unregistered** User I can:
* *easily determine the purpose of the site* in order to *see if I want to register and join*.
* *easily register* in order to *start interacting with the content and community*.


#### **Site Admin**
As a **Site Admin** I can: 
* *approve user book reviews* in order to *publish them to the site*.
* *approve user book reviews* in order to *check that their content is appropriate*.
* *approve user comments* in order to *filter out objectionable content*.
* *view the number of likes on a book review* in order to *see which is the most popular*.
* *delete user accounts* in order to *remove users who do not respect others in the community*.
* *add to the featured authors section* in order to *keep site content fresh and relevant*.

<hr>

### **Wireframes**

I used [Figma](https://www.figma.com) to help guide my design process for this project. I wanted to use a programme which would help me visualise the pages a little clearer than Balsamiq Wireframes, which I have used in the past. As images and colours are a key part of this site's look and feel, I wanted to feel happy they worked in planning before committing.

* [Homepage](docs/wireframes/sfp-index-wireframe.png)
* [About Page](docs/wireframes/sfp-about-wireframe.png)
* [Books Page](docs/wireframes/sfp-books-wireframe.png)
* [Authors Page](docs/wireframes/sfp-authors-wireframe.png)
* [Book / Author Detail Page](docs/wireframes/sfp-detail-wireframe.png)
* [User Account Page](docs/wireframes/sfp-account-wireframe.png)
* [Submit Review Page](docs/wireframes/sfp-submit-review-wireframe.png)
* [Edit Review Page](docs/wireframes/sfp-edit-book-wireframe.png)
* [Delete Review Page](docs/wireframes/sfp-delete-book-wireframe.png)
* [Search Results Page](docs/wireframes/sfp-search-wireframe.png)


The final site adheres fairly closely to the initial images. I dropped the fixed-bottom footer as it interfered with site content on some devices. I moved the social media and email links to the right side of the navbar where they worked better anyway.


<hr>

### **Database Schema**

I used [DrawSQL](https://drawsql.app)​ to help visualise my database tables. See the image below:

![Database Schema](docs/data-model/sfp-drawsql-erd.png)

Unfortunately, the site did not provide adequate field type values but it was intrumental in helping create the Entity Relationship Diagram.

The exact models used in the project can be viewed [here](docs/data-model/sfp-data-models.png).

<hr>

### **Colour Scheme:**
​
After researching various options for this project, I opted for the color scheme below:

![Colour Palette](docs/images/colour-palette.png)

The contrast scores for all the colours used across the project can be seen below. I used [contrast-grid](https://contrast-grid.eightshapes.com/) to generate this chart.

![Colour Palette Contrast Scores](docs/images/contrast-checker.png)

<hr>​

#### **Typography**
​
I researched a number of fonts that would be in keeping with the sci-fi theme of the site. I used [Font Pair](https://www.fontpair.co/inspiration/space-mono-roboto-mono) to try a number of options and eventually chose the following:

* [Space Mono](https://fonts.google.com/specimen/Space+Mono)
Chosen for its sci-fi-esque appearance.


* [Roboto](https://fonts.google.com/specimen/Roboto)
Chosen for its softer edges to counter the harsher appearance of Space Mono.

The two are used evenly throughout the site.

​<hr>

## Agile Development

I used Github projects to create and track issues and User Stories. The Agile processes and methodologies can be viewed [here](/AGILE.md)

<br>
<hr>
<br>

# **Features**

## **Site Navigation**

### **Admin Page**

The Admin page was setup almost immediately. This was crucial as it provided the initial means of adding test data and users to the project.

![Screenshot of admin page](docs/images/admin.png)

<hr>

### **Navbar**
​
The Navbar is a bootstrap component which allows a registered User to navigate their way around the site with ease. When logged out, it displays just the SF|Portal logo and social media / email links:

![Screenshot of navbar](docs/images/navbar-logged-out.png)

When the User is logged in, it offers navigation to the profile, books, authors and about pages:

![Screenshot of navbar](docs/images/navbar-logged-in.png)

To display properly on smaller screens, I used a Bootstrap hamburger menu:

![Screenshot of small-screen navbar](docs/images/navbar-small-screen-before.png)
![Screenshot of small-screen navbar menu](docs/images/navbar-small-screen.png)


<hr>

### Social Media and Email Links

The social media and email icons are situated on the right of the Navbar. The Social Media links are functional and will open in a new tab. 
**NOTE:** There is no actual Social Media for this site at the time of writing.

The email icon opens the default email application with the recipient being a test email address for the site.

![Screenshot of social media and email links](docs/images/social-media-links.png)


<hr>

### **Home Page**

The Home Page uses a background chosen to evoke sci-fi imagery and features a human figure standing in front of a Portal, thus linking neatly with the name of the site. It features some simple text outlining the purpose of the site as well as a search bar, which logged-in Users can use to search for content:

![Screenshot of home page](docs/images/sfp-home-page.png)

The Home Page is responsive and works well on smaller devices. This is how it looks on an iPhone SE:

![Screenshot of small-screen home page](docs/images/sfp-home-small.png)

Users can search for books using the search function:

![Screenshot of home page search](docs/images/sfp-search.png)

<hr>

### **Books Page**

The Books Page features a background image of stars which complements the overall colour palette of the site. It consists of a 'Submit Review' button and a paginated list of book reviews made by other Users or Admin. Each review is a Bootstrap card displaying the title, author and an image of the book. If no image is uploaded by the User, it is assigned a default image showing 'Image not available'. This can always be assigned by Admin or the User at a later time. The card also displays a snippet of the synopsis, a User rating, who posted the review the number of likes and comments. 

There are a maximum of six reviews per screen, the User can click 'next' or 'previous' to navigate between the reviews:

![Screenshot of book page](docs/images/books1.png)
![Screenshot of book page](docs/images/books2.png)

The Books page is responsive on smaller screens and the reviews will stack so they can be scrolled. The following screenshot is from an iPhone SE:

![Screenshot of small-screen book page](docs/images/books-small.png)

Assuming the User is logged in, they are able to edit or delete reviews they have posted directly from the Books Page:

![Screenshot of edit and delete book page](docs/images/books-buttons.png)

The User can click on any of the book titles or images to go to the Book Detail page and read that particular review.

<hr>

### **Book Detail Page**

Upon clicking on a review in the Books Page, the User is taken to the Book Detail page:

![Screenshot of book detail page](docs/images/book-detail1.png)
![Screenshot of book detail page](docs/images/book-detail-2.png)

This dislays a larger image of the book - if uploaded, the book title, author, review rating and synopsis. The User review is situated below and there is also the opportunity for a User to edit or delete their own reviews. Users can also like or unlike reviews as well as see the number of both:

![Screenshot of book detail edit/delete/likes/comments page](docs/images/book-detail-likes.png)

***Likes***

The like button has two states: a [Font Awesome](https://fontawesome.com/) heart outline if the user has not liked the review:
<br>
![Screenshot of unliked](docs/images/book-likes-before.png)

or a solid heart if the user has liked it:

![Screenshot of liked](docs/images/book-likes-after.png)

The User can like or unlike a review.

<hr>

### **Add Book Page**

If a User clicks 'Submit a Review' they are taken to the Add Book Page:

![Screenshot of Add Book Page 1](docs/images/add-book-1.png)
![Screenshot of Add Book Page 2](docs/images/add-book-2.png)

The User must provide information for all fields in the form other than providing an image, rating and sub-genre. There are default values for the latter three but the User can still alter them.

Any mandatory form fields that are left blank will result in the following prompt:

![Screenshot of Add Book Form errors](docs/images/add-book-form-errors.png)

Upon successful submission of the form, the User is redirected to the Books Page and a message is displayed.


<hr>

***Comments***

Comments can be viewed below the reviews. This displays the User posting the comment, the date and time as well as the comment itself:

![Screenshot of book detail page comments](docs/images/book-detail-comments.png)

**NOTE** All comments must be approved by the Admin in order to filter out objectionable content.

In order to post a comment, the User must complete the comment form at the bottom of the page:

![Screenshot of book detail page comment form](docs/images/book-detail-comments-before.png)

Upon submission of the form, they are presented with the following message:

![Screenshot of book detail page comment submission](docs/images/book-detail-comment-after.png)

When the comment has been approved by the Admin, they will appear with the other comments in the order they were posted.

<hr>

### Edit Book Page

If the User clicks edit on the Books or Book Detail page then they are directed to the edit book page:

![Screenshot of edit book](docs/images/book-edit-1.png)
![Screenshot of edit book](docs/images/book-edit-2.png)

A User is only allowed to edit or delete an admin-approved review that they have posted. If these conditions are met, the edit book page will display a form pre-populated with the existing data from the initial review. This can be edited or updated. The primary reasons for doing so would be to edit typos pr perhaps add an image they couldn't find before.

Upon submission of the form, the User will be redirected to the Books page and shown a success message:

![Screenshot of successful edit book](docs/images/book-edit-success.png)

#### **Responsiveness**

The edit-book page is responsive and scales well on smaller devices. The screenshots below show how it renders on an iPhone SE:

![Screenshot of edit book small screen](docs/images/book-edit-smaller-1.png)
![Screenshot of edit book small screen](docs/images/book-edit-smaller-2.png)

<hr>


### Delete Book Page

If the user chooses to delete one of their book reviews, they are directed to the following page:

![Screenshot of delete book](docs/images/delete-book.png)

There are only two options: the User can click cancel and return to the previous page, or confirm delete of the review and are redirected to the books page where a message displays that the message has been successfully deleted. 

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of edit book page small screen](docs/images/delete-book-small.png)

<hr>


### Authors Page

If the User navigates to the Authors Page they can view a list of the Featured Authors:

![Screenshot of authors page 1](docs/images/authors1.png)
![Screenshot of authors page 2](docs/images/authors2.png)

This is an ever-growing list which will be to added by the admin over time. The layout is similar to the books page, with a paginated list of authors displayed. Each card displays the name, date of birth, famous works and a snippet of the author's bio. If no image is available, there is a default image displayed. In this instance, it is just for test purposes that there is no image of Isaac Asimov, as there were many available. This feature is reserved for more obscure or emerging artists for whom there might not be an image. The User can click on the image, author name or 'view full bio' link to navigate to the Author Detail Page.

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of authors page small screen](docs/images/authors-small.png)

<hr>


### Author Detail Page

The aim of this page is to introduce the User to new authors who might appeal to fans of the genre. These will include established authors and luminaries of the science fiction field or perhaps newer, emerging writers. For the purpose of consistency Author Detail Page is similar to the Book Detail Page. The same background image fits the sci-fi theme and the layout of the page features a large image of the author, their name, date of birth, famous works and a bio:

![Screenshot of author detail page 1](docs/images/author-det-1.png)
![Screenshot of author detail page 2](docs/images/author-det-2.png)

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of author detail page small screen](docs/images/author-det-small.png)

<hr>

### About Page

The About page displays information about the site. The text welcomes the User to the site and explains what they can do as a registered User. There are links to different areas of the site and a reminder to respect other Users in the community:

![Screenshot of about page ](docs/images/about.png)


#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of about page small screen](docs/images/about-small.png)

<hr>


### Profile Page

When the User registers a new account, a profile is automatically created for them to edit in their own time. The purpose of this is so that the User can register and immediately start using the site rather than have to waste time completing a profile they may not wish to use. If the User wishes to, they can click on the Profile icon in the Navbar to view their Profile card:

![Screenshot of Profile page](docs/images/profile-card.png)

If the User clicks the 'Edit Profile' button, it will reveal a form which the User can use to update their details:

![Screenshot of Profile page edit form](docs/images/profile-form.png)

Upon clicking the 'Update' button, the form is submitted and the page reloads with the new details and a success message:

![Screenshot of profile page success](docs/images/profile-form-success.png)

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of profile page card small screen](docs/images/profile-card-small.png)
![Screenshot of profile page form small screen](docs/images/profile-form-small.png)

<hr>


## Allauth Account Pages

All Account Pages use the same background, again evoking sci-fi imagery. The image is a swirling, nebulous portal which again complements the colour palette used site-wide.

#### Sign Up

I used allauth to handle the account pages for the project. In order to register, the User must complete the form on the Signup Page:

![Screenshot of signup page](docs/images/signup.png)

Once the User has successfully registered, they will be logged in and taken to the Home Page. The form will display error messages in several circumstances:

* The User chooses a Username that is already taken
* The password is not long enough
* The password is too similar to the username or too common
* The passwords do not match

See the example below: 

![Screenshot of signup page errors](docs/images/signup-errors.png)

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of signup small screen](docs/images/signup-small.png)

<hr>

#### Log In

Existing Users can log in by clicking the Log In button on the Home Page. This will bring them to the Log In Page:

![Screenshot of log in page](docs/images/login-page.png)

If the log in details are not valid, an error message is displayed. For example: 

![Screenshot of log in page errors](docs/images/login-error-message.png)

#### **Responsiveness**

Here is how the page displays on an iPhone SE:

![Screenshot of login small screen](docs/images/login-small.png)
![Screenshot of login error small screen](docs/images/login-error-small.png)

<hr>


#### Log Out

To log out of the site and end the current session, the User can navigate to Log Out in the Navbar. This will direct them to the Log Out Page:

![Screenshot of logout page](docs/images/logout.png)

The User can confirm by clicking the Log Out button or click the cancel button to return to the previous page. If the User chooses to log out, they are redirected to the Home Page and a success message informs them they have been logged out:

![Screenshot of home screen logout success](docs/images/home-logout-success.png)

#### **Responsiveness**

Here is how the pages display on an iPhone SE:

![Screenshot of logout small screen](docs/images/logout-small.png)
![Screenshot of logout success small screen](docs/images/home-logout-success-small.png)


<hr>

## Links and Buttons

### **Links**

I used two different effects for the links in the project. 

## **Messages**

User feedback is provided in the shape of success messages with the aim of providing a more involved User Experience. These messages are dismissable by clicking the 'x' and will be displayed in the following situations:

**Successful Login**

![Succesful login message](docs/images/login-success.png)

**Successful Update Profile**

![Succesful update profile](docs/images/profile-success.png)

**Successful Add Book Review**

![Succesful add book message](docs/images/add-book-success.png)

**Successful Edit Book Review**

![Succesful edit review message](docs/images/edit-success.png)

**Successful Delete Book Review**

![Succesful login message](docs/images/delete-success.png)

**Successful Comment Submission**

![Succesful Comment Submission message](docs/images/comment-success.png)

**Successful Logout**

![Succesful logout message](docs/images/logout-success.png)


<hr>

## **Defensive Programming**

In order to avoid the User unintentionally deleting their own content, some simple defensive programming was implemented. If a User is logged in and clicks delete on one of their reviews, they will be prompted for confirmation they want to do so here:

![Screenshot of delete page](docs/images/delete-book.png)


<hr>

### User Authentication

All pages feature User Authentication meaning that a User must be logged in to view all site content. This encourages Users to signup as well as preventing malicious attempts to edit or delete content. If a user knows or guesses a correct URL without being logged in they will encounter this screen:

![Screenshot of authentication](docs/images/user-authentication.png)


<hr>

### **404 Page**

A custom 404 page was added to catch instances when the User may have mis-typed a URL, or if content has been removed from the site. The 404 page features text dislaying the content is not available and features a back button:

![Screenshot of 404 page](docs/images/404.png)


<hr>

### **500 Page**

A custom 500 page was added to catch instances when a potentially malicious User might try to subvert the site, for example to access personal data or delete content. In this case the page below displays and features a back button to redirect them to the previous page:

![Screenshot of 500 page](docs/images/500-page.png)


<hr>

## **Future-Enhancements**
​
There are a number of areas with scope for future improvement. This project has been very challenging and ultimately the project deadline was looming. There is potential to add the following:
​
* Adding movies and games to fit into a 'Categories' drop-down menu.
* The option for Users to add to the Authors section.
* User images to be added to comments and book reviews.
* A community page for User who opt in to have their profiles diplayed publicly.
* The serach function to be updated to display results in the new categories.
* Using the Google Books API to retrieve book information. I did explore this option before the inception of the project but decided against including it due to time constraints.

<hr>

## User Authentication

All pages feature User Authentication meaning that a User must be logged in to view all site content. This encourages Users to signup as well as preventing malicious attempts to edit or delete content. If a user knows or guesses a correct URL without being logged in they will encounter this screen:

[Screenshot of authentication](docs/images/user-authentication.png)

<hr>

## **Testing Phase**

The testing process, along with bugs, can be viewed [here](/TESTING.md)​

<hr>

## **Deployment**

The Deployment was a fairly lengthy process so I have detailed it in a separate file. It can be found [here](/DEPLOYMENT.md)

The final deployment can be viewed [here](https://sci-fi-portal.herokuapp.com/)

<hr>

## **Software and Tech**

The following software and tech was used:

- [BootStrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) to provide key components such as the navbar and cards.
- [Cloudinary](https://cloudinary.com) to handle static images and files as well as to offer the User a front end method of uploading images.
- CSS to provide custom styling in addition to Bootstrap.
- [Django](https://www.djangoproject.com/) as a Python framework to develop the project.
- [Django all auth](https://django-allauth.readthedocs.io/en/latest/) used to handle user authentication.
- [DrawSQL](https://drawsql.app/) to develop the logic for the project.
- [ElephantSQL](https://www.elephantsql.com/) to handle the PostgreSQL database.
- [Figma](https://www.figma.com/) to assist with the planning phase of the project.
- [Font Awesome](https://fontawesome.com/) to provide search, heart, profile, social media icons etc.
- Git (Gitpod and Github) as my version control for the site.
- [Gitpod](https://gitpod.io/) and VS Code to create, load and push my code to Github.
- [Heroku](https://www.heroku.com/) to deploy the project.
- HTML - The base language to create templates for the site
- JavaScript - only used twice: for the back or cancel buttons and to populate the hidden created_by field in the add_book form.
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) used to implement logic from views.py and models.py.
- Microsoft Excel to develop the logic for the project.
- [Optimizilla](https://imagecompressor.com/) to compress background images for the site.
- Python - Installed packages can be found in the requirements.txt file.
- [Shutterstock](https://www.shutterstock.com/) to source the background images for the site.
- [Summernote](https://summernote.org/) to provide a WYSIWYG text editor in the admin area.

<hr>

## **Media**

* All book images are from [Amazon UK](https://www.amazon.co.uk/)
* All background images came from a free trial subscription to [Shutterstock](https://www.shutterstock.com/)
* All author images and bios are from [Wikipedia](https://www.wikipedia.org/) other than:
  * N.K. Jemisin: bio and image from [author webiste](https://nkjemisin.com/)
  * Adrian Tchaikovsky: bio taken from [author website](https://adriantchaikovsky.com/)
​
<hr>

## **Credits**

* The colour palette for the project is from [Pinterest](https://www.pinterest.co.uk/pin/204491639320145500/).

* The idea to use Cloudinary to handle static and media files came from the [Code Institute](https://codeinstitute.net/) walkthrough project: 'I Think, Therefore I Blog.

* The [Django Documentation](https://docs.djangoproject.com/en/4.1/) was immensely helpful in helping me gain a greater understanding of the project.

* The JavaScript code used to populate the hidden created-by field in the 'add book' form came from [this](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) series of videos by John Elder on YouTube.

* [This Post](https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/) from Shuaib Oseni was helpful when it came to creating the front end method to upload an image to CLoudinary.

* The idea to automatically create the User Profile came from [this article](https://groups.google.com/g/django-users/c/cvbuURVHN0w) on Google Groups.

* General References:
  * Stack Overflow
  * Code Institute LMS
  * Bootstrap Documentation
  * Jinja Documentation
  * Cloudinary Documentation
  * Geeks for Geeks
  * W3C School
  * Course material on the CodeCademy website which helped reinforce my understanding of Python.

<hr>

## **Honourable mentions**

* The biggest thank you goes to my mentor, Richard Wells, who gave a significant amount of his time to provide me with help, feedback and ideas on the project; he has been invaluable in so many ways and a genuine source of motivation for me.
* Thanks to the Code Institute team for providing me with some basic knowledge of Python and Django.
* Thanks to the Code Institute who helped me overcome a major bug in the final deployment of the project
* Thanks to the Code Institute community on Slack who helped remind me that everyone has difficult days.
* A huge thank you to my family who support my coding journey on a daily basis.

<hr>

Links to additional related files: [AGILE.md](/AGILE.md) | [DEPLOYMENT.md](/DEPLOYMENT.md) | [TESTING.md](/TESTING.md)
