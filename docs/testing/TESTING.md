# Testing  document for MovieBox e-commerce web application  
This document details how the MovieBox e-commerce web application was tested throughout its development and deployment stages to ensure that complience, a good user experiance was achieved and to make the application as accessible to all its end users.  
Tests were carried out throughout development in an intergrated way, the tests were carried out at each main application development stage or when a new feature addition was being developed to ensure PEP8 complence within Python code was maintained and ensure when developing frontend elements that, HTML, CSS and JS complience was maintained also, alongside ensuring screen reader enhancements using WAI-ATIA functioned also.  

## Table of contents
 
1. [User stories](#user-stories)  
    1.1 [First time user](#first-time-user)  
    1.2 [Returning user](#returning-user)  
    1.3 [Site owner](#site-owner)  
2. [Testing overview](#testing-overview)  
3. [Test results overview](#test-results-overview)  
4. [Validation Testing](#validation-testing)  
    4.1 [HTML validation](#html-validation)  
    4.2 [CSS validation](#css-validation)  
    4.3 [JS validation](#js-validation)  
    4.4 [PEP8 validation](#pep8-validation)  
5. [Database and application testing stages](#database-and-application-testing-stages)  
6. [Stripe Webhook api test](#stripe-webhook-api-test)  
7. [Manual testing](#manual-testing)  
    7.1 [Rendering in the browser & Reflow tests](#rendering-in-the-browser--reflow-tests)  
    7.2 [Link testing](#link-testing)  
    7.3 [Tab order test](#tab-order-test)  
    6.4 [Landmark test](#landmark-test)  
    7.5 [Heading test](#heading-test)  
    7.6 [Screen reader testing](#screen-reader-testing)  
8. [Automated testing](#automated-testing)  
    8.1 [Lighthouse](#lighthouse)  
    8.2 [Simulated device testing](#simulated-devive-testing)  


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

Located within the shopping basket page is a clearly marked button titled ???complete purchase???, activating this button will take a user to the purchase page to complete their purchase.  

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

Located within every registered user???s profile is a breakdown of every purchase a customer has made, the listing includes a view purchase link where they can see a historic receipt of when they purchased the item.  

- __As the site owner, I want to encourage users to visit clearance and sale areas.__  

![User stories - Site owner q5](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_5.png)  

Located on the home page are listings for the items within clearance and limited time category, this is done as the prices are lower and will help entice curiosity about other products available within MovieBox e-commerce website.  

- __As the site owner, I want to be able to add new products to the site easily and efficiently.__  

![User stories - Site owner q6](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_6.png)  

When a super user is signed in, their profile will have a new admin section added where they can add, edit and delete products from the MovieBox website without the need to go through the management console.  

- __As the site owner, I want to be able to view a real time record of purchases and amend where necessary customer orders.__  

![User stories - Site owner q7](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_7.png)  

A super user can login with their details into the management console which is accessed through the admin link located within the account navigation bar.  
The user will then be able to select purchases table and view or amend, and delete purchases made on MovieBox.  

- __As the site owner, I want to encourage users to visit MovieBox???s sister site Movie2Archive.__  

![User stories - Site owner q8](/docs/testing/user_stories_testing_images/site_owner/site_owner_question_8.png)  

Located across the site is an advertisement to sugget trying out Movie2Archive as a tool to catalogue the items bought through MovieBox or to help archive the customers current movie collection.  

## Testing Overview  

__Automated testing__  
All automated tests were carried out using incognito mode to eliminate extension conflicts or false positives and errors due to the extension requests.  

__Manual testing__   
All manual testing was carried out in standard browser mode to simulate a real-world users experience of the MovieBox e-commerce web application.  

__Libraries__   
As the project technologies used the Bootstrap framework and Font Awesome for icons there is a possible effect on performance audit scored, this is due to the js scripts and in the instance of Bootstrap, jQuery library has to be loaded to enable features of Bootstrap 4 to function.  

The features include popper.js which is used for modals and is used for the responsive navigation.  
CDN's were used where possible across MovieBox, this was done to provide a minified cached version of frameworks and to ensure reliability, but this can still be a larger file when the page initially loads until it is cached.  

CSS pre-loader tags were used to eliminate render blocking script flag within Lighthouse and deferring of scripts where necessary was used on JavaScript libraries and custom scripts.    

__External apis__  
External apis were used during the development of MovieBox, the apis include imdb data searching and Stripe payment api.  
Imdb data searching was tested manually for the information provided back through its api using official imdb website data store and Stripe was tested manually to verify its transaction was validating using the Stripe website developer portal and also automated testing verifies that the data was being passed back through to the MovieBox application.  
Throughout and in deployment, test card numbers are used to simulate a real-world example of a real purchase being made.  

__Performance__  
Due to experiance and the restrictions of the shared environment of Heroku for compiling and serving the application on the frontend, certain performance metrics are affected as the shared hosting will sleep after a few minutes of inactivity to conserve resources and wake when needed which can take a few moments to be responsive, a paid plan would provide an always on connection and produce a higher performance which would yield faster performance for the end user.    

__PEP8 complience__  
PEP8 complience has been followed throughout the project, the project was developed using GitPod and the full template provided by Code Institute which includes Python linting to ensure compliance.  

There is some string too long lints, the tuition we have been taught is only how to expand to two lines, after research it is also worth noting that dependant on operating system, expanding to multiple 
lines can introduce incompatible code and may fail to run.  

The lint and PEP8 line too long are also a style guide and this varies from 80 characters up to 150 characters dependant on the technology industry the application is running within, it is also similar to a warning in CSS, HTML validators or WCAG guidelines and is not an actual error but a visual cue to aim for a written best practice standard.  

__Stripe payment testing__  
All scenerios have been tested through the form on MovieBox and checked using the Stripe console to ensure payments go through and are reflected within the admin console of Django.  
Stripe provides test card numbers to test each scenerio and these have been tested to ensure that each one is successful and causes the action it should.  
Stripe hides the card details and states they should not be ublically shared, these card numbers have been shared along with the project so that they can be checked.  

__Accessibility extensions__  
All results from accessibility extensions were verified using manual tests and where relevant were validated using real Screen Reader software using a human tester.  

__Screen Reader software__  
NVDA and JAWS were used in some tests, this is software which I own and was run in real time and not simulated through an extension or virtual environment on a non-windows environment machine.  

## Test results overview  
Below is a table which represents a high level overview of the various tests undertaken during and through development of the MovieBox e-commerce web application, results of these tests and issues were collected and stored in an Excel document for functionality and accessibility reasons due to my sight loss for easier navigation using a screen reader, the excel document contains 3 sheets of tests.  
Please find the [moviebox_test_and_issue_record.xlsx](/docs/testing/moviebox_test_and_issue_record.xlsx) file on the GitHub repository.  
 
| Test             | Logged out user | logged in user | Admin user |
|------------------|----------|-------------------|------|
| Database connection  | PASS     | Pass              | PASS | 
| HTML Validation  | PASS     | Pass              | PASS | 
| CSS Validation   | PASS     | PASS               | PASS | 
| JShint           | PASS     | PASS              | PASS | 
| PEP8            | Code PASS     | Code PASS              | Code PASS | 
| Links            | PASS     | PASS              | PASS | 
| Landmark Regions | PASS     | PASS              | PASS |
| Headings            | PASS     | PASS              | PASS | 
| Screen reader    | PASS     | PASS              | PASS |
| Lighthoise - <br>Performance,<br>Accessibility,<br>Best practice,<br>SEO | PASS         | PASS         | PASS          |

## Validation Testing

### HTML validation  
-  Homepage - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_homepage.png)  

-  Login - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_login.png)  

-  Logout - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_logout.png)  

-  Profile - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_profile.png)  

-  New arrivals - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_new_arrivals.png)  

-  Genre (action) - PASS   
All genre pages load the same, this is why there is only one test as the page is the same.  
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_new_arrivals.png)  

-  All movies - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_all_movies.png)  

-  All deals - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_all_deals.png)  

-  Product_details - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_product_details.png)  

-  Basket - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_basket.png)  

-  Purchase - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_purchase.png)  

-  Purchase complete - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_purchase_complete.png)  

-  Add movie - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_add_movie.png)  

-  Edit movie - PASS   
![W3C HTML Validator result](/docs/testing/validator_testing_images/test_html_validator_edit_movie.png)  

### CSS validation  
As the site uses one CSS style sheet, the style sheet was validated by pasing in the raw code to the validator.  

-  CSS stylesheet - PASS  
![W3C CSS Validator result](/docs/testing/validator_testing_images/test_css_validator_main_css_stylesheet.png)  

### JS validation  
![JShint Validator result](/docs/testing/validator_testing_images/test_validator_js_hint_js_scripts.png)  
JS hint was used and no errors were detected, Stripe variable is mentioned because the JSHint does not have access to the installed python package Stripe.  

### PEP8 validation  
Pylint, Flake8 were used in the CI institute template to endure complience and online tools such as [Python checker](https://www.pythonchecker.com/) and [Black formatter](https://black.vercel.app/?version=stable&state=_Td6WFoAAATm1rRGAgAhARYAAAB0L-Wj4ARsAnNdAD2IimZxl1N_WlkPinBFoXIfdFTaTVkGVeHShArYj9yPlDvwBA7LhGo8BvRQqDilPtgsfdKl-ha7EFp0Ma6lY_06IceKiVsJ3BpoICJM9wU1VJLD7l3qd5xTmo78LqThf9uibGWcWCD16LBOn0JK8rhhx_Gf2ClySDJtvm7zQJ1Z-Ipmv9D7I_zhjztfi2UTVsJp7917XToHBm2EoNZqyE8homtGskFIiif5EZthHQvvOj8S2gJx8_t_UpWp1ScpIsD_Xq83LX-B956I_EBIeNoGwZZPFC5zAIoMeiaC1jU-sdOHVucLJM_x-jkzMvK8Utdfvp9MMvKyTfb_BZoe0-FAc2ZVlXEpwYgJVAGdCXv3lQT4bpTXyBwDrDVrUeJDivSSwOvT8tlnuMrXoD1Sk2NZB5SHyNmZsfyAEqLALbUnhkX8hbt5U2yNQRDf1LQhuUIOii6k6H9wnDNRnBiQHUfzKfW1CLiThnuVFjlCxQhJ60u67n3EK38XxHkQdOocJXpBNO51E4-f9z2hj0EDTu_ScuqOiC9cI8qJ4grSZIOnnQLv9WPvmCzx5zib3JacesIxMVvZNQiljq_gL7udm1yeXQjENOrBWbfBEkv1P4izWeAysoJgZUhtZFwKFdoCGt2TXe3xQ-wVZFS5KoMPhGFDZGPKzpK15caQOnWobOHLKaL8eFA-qI44qZrMQ7sSLn04bYeenNR2Vxz7hvK0lJhkgKrpVfUnZrtF-e-ubeeUCThWus4jZbKlFBe2Kroz90Elij_UZBMFCcFo0CfIx5mGlrINrTJLhERszRMMDd39XsBDzpZIYV4TcG7HoMS_IF8aMAAAxI-5uTWXbUQAAY8F7QgAAP01Vc6xxGf7AgAAAAAEWVo=) [Black formatter docmentation](https://black.readthedocs.io/en/stable/getting_started.html#try-it-out-online) were used also.  
Between these tools PEP8 style guide were met, a screenshot below shows an example.  
![Python checker image](/docs/testing/validator_testing_images/test_python_checker_validation.png)  

## Database and application testing stages
- Construct and render Django application to browser:  
PEP8 complience - Python, django structure files - PASS  
- Django homepage app created.  PEP8 complience - PASS  
- Django products app created, models Category, Product  PEP8 complience - PASS  
- Django basket app created.  PEP8 complience - PASS  
- Django purchase app created, models Order, OrderLineItem  PEP8 complience - PASS  
- Django profile app created, models UserProfile  PEP8 complience - PASS  
- Test deployment to Heroku - No deployment issues - PASS  
- Creation of Postgresql data base on Heroku and import of models - No issues - PASS  
- Test new webhook with stripe using Heroku domain name - No issues - PASS  
- Connect AWS S3 Bucket to MovieBox - No issues with transfer of Static files - PASS  
- Test django email message confirmation of order through Heroku app - No issues - PASS   

## Stripe Webhook api test  
The image shows below the api webhook payment_intent.succeeded being confirmed, this is te hook that can take care of processing payments should the browser close unexpectedly or a user accidently closes the session during processing a purchase.  
This test shows a record of an order would be placed n MovieBox admin console if a customer had a query.  
![Stripe webhook payment_intent.succeeded](/docs/testing/stripe/stripe_payment_intent.png)  

## Manual testing  
### Rendering in the browser & Reflow tests.  
Devices used: Windows 10 PC, Mac Studio, iPad Air 2, iPhone 14 Pro Max  
Desktops  
-  Chrome, EDGE, Firefox on PC - PASS  
-  Safari, Chrome on Mac - PASS  
Tablet and mobile
-  Safari - PASS  
I found that the e-commerce website application and all components reflowed and displayed correctly as expected on the various different screen sizes and systems that were used to test the MovieBox e-commerce web application.  

### Link testing  
All links within the e-commerce web application were tested to ensure that internal links behaved correctly, and external facing links such as social media links, third party links such as Movie2Archive opened in a new tab and did not take the user away from MovieBox.  
A screen reader was also used during these tests on PC and MAC to ensure that the Sr-Only CSS help text classes and aria-hidden classes which have been applied at various sections throughout the application were announced and behaved as expected correctly by the screen reader software.  
an example of such code is shown below:  
```
<li class="ms-3">
    <a target="_blank" href="https://www.instagram.com/" rel="noopener">
        <i class="fab fa-instagram" aria-hidden="true"></i>
            <span class="sr-only">Find us on Instagram (opens in a new window)</span>
    </a>
</li>
```  
All pages were tested, and no issues were discovered.  

### Tab order test  
The Accessibility insights extension was used to visually test the tab order on all pages.  
The tab order was tested to ensure all focusable elements could receive focus for keyboard only users of the e-commerce web application, this also ensures that screen reader users assistive technology will be able to read these elements to when they recieve focus.    
No issues were found during tests, an Example page of the test being carried out is shown below:  
![Tab order test](/docs/testing/accessibility_testing_images/test_tab_order.jpg)  

### Landmark test  
Screen reader users can use landmarks to navigate to sections within a page more quickly and effectively rather than navigating through each element on the page, landmarks are used as a form of quick navigation and understanding placement of page sections.    
These landmarks have been implemented using HTML5 semantic markup and where appropriate, ARIA has also been used where an item would need a role to identify itself or additional functionality added using ARIA.    
![Landmark test](/docs/testing/accessibility_testing_images/test_landmarks.png)  

### Heading test  
Heading structure was also checked and meets Wcag guidelines for headings appearing in a sequential order as to distinguish priority, H1 through to H6.  
![Landmark test](/docs/testing/accessibility_testing_images/test_headings.png)   

### Screen reader testing  
All areas of the e-commerce web application behaved as expected and no keyboard traps or block points were found during testing using a screen reader.  
Devices used: Windows 10 using NVDA 2022 and JAWS 2022, Mac using VoiceOver for Mac and iPhone 14 Pro Max using VoiceOver.  

## Automated testing  
### Lighthouse  
Google Chrome DevTools was used to run the audit and test the Performance, Accessibility, Best practice, and SEO of each page within the e-commerce web application.  

- Homepage desktop  
![Lighthouse test - Homepage desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_homepage.png)  

- Homepage mobile  
![Lighthouse test - Homepage mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_homepage.png)  

- Login desktop  
![Lighthouse test - Log in desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_login.png)  

- Login mobile  
![Lighthouse test - Log in mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_login.png)  

- Log out desktop  
![Lighthouse test - Log out desktop](/docs/testing/lighthouse_testing/desktop/lighthuse_test_desktop_logout.png)  

- Log out mobile  
![Lighthouse test - Log out mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_logout.png)  

- Profile desktop  
![Lighthouse test - Profile desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_profile.png)  

- Profile mobile  
![Lighthouse test - Profile mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_profile.png)  

- New arrivals desktop  
![Lighthouse test - New arrivals desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_profile.png)  

- New arrivals mobile  
![Lighthouse test - New arrivals mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_new_arrivals.png)  

- Genre (action) desktop  
![Lighthouse test - Genre (action) desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_genre_action.png)  

The genre displays titles based on their category and is the same page, results were the same across filters and this is why only one result is shown.

- Genre (action) mobile  
![Lighthouse test - Genre (action) mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_genre_action.png)  

- All movies desktop  
![Lighthouse test - All movies desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_all_movies.png)  

- All movies mobile  
![Lighthouse test - All movies mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_all_movies.png)  

- All deals desktop  
![Lighthouse test - All deals desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_all_deals.png)  

- All deals mobile  
![Lighthouse test - All deals mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_all_deals.png)  

- Product details desktop  
![Lighthouse test - Product details desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_product_details.png)  

- Product details mobile  
![Lighthouse test - Product details mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_product_details.png)  

- Basket desktop  
![Lighthouse test - Basket desktop](/docs/testing/lighthouse_testing/desktop/lighthuse_test_desktop_basket.png)  

- Basket mobile  
![Lighthouse test - Basket mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_basket.png)  

- Purchase desktop  
![Lighthouse test - Purchase desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_purchase.png)  

- Purchase mobile  
![Lighthouse test - Purchase mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_purchase.png)  

- Purchase complete desktop  
![Lighthouse test - Purchase complete desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_purchase_complete.png)  

- Purchase complete mobile  
![Lighthouse test - Purchase complete mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_purchase_complete.png)  

- Add movie desktop  
![Lighthouse test - Add movie desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_add_movie.png)  

- Add movie mobile  
![Lighthouse test - Add movie mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_add_movie.png)  

- Edit movie desktop  
![Lighthouse test - Edit movie desktop](/docs/testing/lighthouse_testing/desktop/lighthouse_test_desktop_edit_movie.png)  

- Edit movie mobile  
![Lighthouse test - Edit movie mobile](/docs/testing/lighthouse_testing/mobile/lighthouse_test_mobile_edit_movie.png)  

### Simulated devive testing  
Chromes built in device simulator which covers many different device sizes was used to simulate the application on a variety of device screen sizes.  
All simulated screen sizes rendered the e-commerce web application correctly and as expected.  

[Back to Repository](https://github.com/JHodgkins/MSP4-MovieBox)   