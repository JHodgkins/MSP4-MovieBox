# Testing  document
This document details how the MovieBox e-commerce web application was tested throughout its development and deployment stages to ensure that complience, a good user experiance was achieved and to make the application as accessible to all its end users.  
Tests were carried out throughout development in an intergrated way, the tests were carried out at each main application development stage or when a new feature addition was being developed to ensure PEP8 complence within Python code was maintained and ensure when developng fromtend elements that, HTML, CSS and JS complience was maintained also, alongside ensuring scren reader enhancements using WAI-ATIA functioned also.  

## Table of contents
 
1. [User stories](#user-stories)  
    1.1 [First time user](#first-time-user)  
    1.2 [Returning user](#returning-user)  
    1.3 [Site owner](#site-owner)  


## User stories testing from the UX section  
### First time user  
- __As a first-time user, I want to understand what the applications purpose is so that I can decide if it meets my needs.__  

![User stories - First time user q1](/docs/testing/user_stories_testing_images/first_time_user/first_time_user_question_1.png)  

When a first time user arrives at the e-commerce website, they will immediately be presented with a bold and easy to understand heading message that outlines the purpose of the e-commerce web application.
A new visitor would be immediately aware of the applications purpose.  

- __As a first-time user, I want to be able to easily navigate to the various categories of products.__  

![User stories - First time user q2](/docs/testing/user_stories_testing_images/first_time_user/first_time_user_question_2.png)  

Located at the top of every page site the main navigation bar, this navigation clearly labels the available areas of the site such as new arrivals, all movies and categories of movies based on their genre.  

- __As a first-time user, I want to be able to add a movie to my shopping basket.__  

![User stories - First time user q3](/docs/testing/user_stories_testing_images/first_time_user/first_time_user_question_3.png)  

On main results pages for movies, the user can add one movie directly to their basket using the add to basket button, alternatively they can view the item details page and add an item through that page using the same distinctive labelled button.  

- __As a first-time user, I want to be able to easily view the items in my shopping basket.__  

![User stories - First time user q4](/docs/testing/user_stories_testing_images/first_time_user/first_time_user_question_4.png)  

On every page of MovieBox, the basket is available to view by selecting the icon in the main navigation bar.  
The basket section auto updates and gives a short overview of the number of items held and the total price including postage and packaging.  

- __As a first-time user, I want to find out more information about a movie product.__  

![User stories - First time user q5](/docs/testing/user_stories_testing_images/first_time_user/first_time_user_question_5.png)  

On every product card there is a more info link which will take a user to a detailed prodct description page.  
The details page shows a wealth of information including certificate, format, director and actor information.  

- __As a first-time user, I want to find out how much a product costs.__  

![User stories - First time user q6](/docs/testing/user_stories_testing_images/first_time_user/first_time_user_question_6.png)  

On every card, the product price is shown, the product price is also shown on the product details page where more information about the product is given.  

- __As a first-time user, I want to know how to proceed to the checkout section so I can purchase an item.__  

![User stories - First time user q7](/docs/testing/user_stories_testing_images/first_time_user/first_time_user_question_7.png)  

Located within the shopping basket page is a clearly marked button titled ‘complete purchase’, activating this button will take a user to the purchase page to complete their purchase.  

### Returning user  
- __As a returning user, I want to be able to easily navigate to the account sign in page.__  

![User stories - Returning user q1](/docs/testing/user_stories_testing_images/returning_user/returning_user_question_1.png)  

Located at the top right of the account bar which is available on every page of MovieBox e-commerce website is a link to take the user to a sign in page where they can login.  

- __As a returning user, I want to be able to see a previous order I have made.__  

![User stories - Returning user q2](/docs/testing/user_stories_testing_images/returning_user/returning_user_question_2.png)  

When a user is signed in, activating the profile link in the account bar will take a user to their personalised profile.  
Within this area is a section titled past purchases where a user can view and activate a view purchase link to view its details.  

- __As a returning user, I want to be able to see how many movies are in my shopping basket.__  

![User stories - Returning user q3](/docs/testing/user_stories_testing_images/returning_user/returning_user_question_3.png)  

A user can see briefly within the navigation bar shopping basket area an indicator number or when visiting the shopping basket page, a user is told within the main page heading of the page how many items are within their shopping basket, this counter adjusts automatically from singular to plural dependant on the count.  

- __As a returning user, I want to be able to view items based on a filter I select.__  

![User stories - Returning user q4](/docs/testing/user_stories_testing_images/returning_user/returning_user_question_4.png)  

Located on every product listing page, there is a sort field, this allows a user to select filters such as price highest to lowest and imdb rating from lowest to highest.  


- __As a returning user, I want to be able to view the latest offers available.__  

![User stories - Returning user q5](/docs/testing/user_stories_testing_images/returning_user/returning_user_question_5.png)  

Located along the main navigation bar are links to the latest offers, these links include limited time offers and clearance items, selecting these filters will display all items within that category.  


- __As a returning user, I want to be able to update my account delivery details.__  

![User stories - Returning user q6](/docs/testing/user_stories_testing_images/returning_user/returning_user_question_6.png)  

When a registered user is signed in, they can access their personalised profile section, within this area is a form that holds their delivery information.  
The user can amend as many times as they wish, this information will be used the next time that they purchase an item.  

### Site owner  
- __As the site owner, I want visitors to be able to find the correct information about a product and make an informed choice to purchase.__  

![User stories - Site owner q1](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_1.png)  

Located on each movie product listing is a detailed information box, this area contains more detailed information about a product including no of discs, running time and a detailed section on MovieBoxes grading system and delivery information.  

- __As the site owner, I want staff admins to be able to edit the information about a product to ensure information is kept up to date.__  

![User stories - Site owner q2](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_2.png)  

When an admin user is logged in, they will be able to select the edit movie button located below the movie cover art and edit its details in real time, if an error was discovered by a customer this allows quick editing and saving of product information.  

- __As the site owner, I want visitors to be able to easily add their movie choices to their shopping basket and amend the quantity if necessary for them to purchase.__  

![User stories - Site owner q3](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_3.png)  

Located within every movie product page is a quantity select box where customers can decide on the amount of an item they wish to purchase, also located within the shopping bag area is a quantity selector box where a customer can update and remove items before purchase.  

- __As the site owner, I want the site visitors to be able to see what they have previously bought.__  

![User stories - Site owner q4](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_4.png)  

Located within every registered user’s profile is a breakdown of every purchase a customer has made, the listing includes a view purchase link where they can see a historic receipt of. When they purchased the item.  

- __As the site owner, I want to encourage users to visit clearance and sale areas.__  

![User stories - Site owner q5](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_5.png)  

Located on the home page are listings for the items within clearance and limited time category, this is done as the prices are lower and will help entice curiosity about other products available within MovieBox e-commerce website.  

- __As the site owner, I want to be able to add new products to the site easily and efficiently.__  

![User stories - Site owner q6](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_6.png)  

When a suer user is signed in, their profile will have a new admin section added where they can add, edit and delete products from the MovieBox website without the need to go through the management console.  

- __As the site owner, I want to be able to view a real time record of purchases and amend where necessary customer orders.__  

![User stories - Site owner q7](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_7.png)  

A super user can login with their details into the management console which is accessed through the admin link located within the account navigation bar.  
The user will then be able to select purchases table and view or amend, and delete purchases made on MovieBox.  

- __As the site owner, I want to encourage users to visit MovieBox’s sister site Movie2Archive.__  

![User stories - Site owner q8](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_8.png)  

Located across the site is an advertisement to sugget trying out Movie2Archive as a tool to catalogue the items bought through MovieBox or to help archive the customers current movie collection.  

