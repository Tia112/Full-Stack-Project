**Full Stack Development Project – MS4**
https://dessertscapital.herokuapp.com/

**Project Outline**

The goal of this project is to build a fully functioning full stack site using
business logic that will control a centrally owned data-set. I will be setting
up a complete end-to-end site, using a range of technologies from the front-end,
middleware and backend.

**Strategy**

The site will be a Dessert Shopping site with a catalogue of products, user
profiles, authentication and payment system.

I will be using a simple relational database to store:

 -  Products – descriptions, price, category information and image

 -  User Profile - username, name, address, Password, order history, payment

 -  Admin functions

**User Stories**

- As a user I would be able to easily select the product I want
- As a user I would like to see more information about the product
 - As a user I would be able to view this site on any device
 - As a user I should be able to sign-up/sign in easily
 - As a user I should get confirmation of my order
- As a user I should be able to see my order history
- As a user I should be able to add/remove items/increase/decrease quantity of items in my cart
- As a user I should be able to search for an item independent of its category
- As a user I should be able to return to my cart without losing its contents
- As a user I would like to ensure the safety of my data

**Administrator stories:**

-   As an administrator I should be able to login securely and separately from
    the main site

-   As an administrator I should be able view details about all aspects of my
    client base

-   As an administrator I should be able manage my product catalogue

-   As an administrator I should be able to add new images to my product listing

-   As an administrator I should be able change products (prices, description
    etc…) as required

-   As an administrator I should be able remove products

-   As an administrator I should be able to view payments

-   As an administrator I should be able to view orders

**Structure**

**(Start) Home page** - This page has a non-moving banner with a description of
the business, inviting users in with the option to browse categories
independently, login or signup. Users will NOT be able to add items to the cart WITHOUT logging on (defensive design).

**Nav-bar** (logged in) – the navbar provides links to each category as required
by the user:

**Sundaes \| Waffles \| Cheesecake \| Milkshake \| Cake**

At each user click, a page is rendered with an image, and price for each
product.

**Product page** – selecting a product, the user is presented with a large image
of the product, a description and its cost. With the option to Add to Cart, or
Continue Shopping.

**Cart** – The user is shown a listing of the item(s) they have added to the
cart, with the option of increasing/decreasing the quantity, the overall price
with the option to Continue Shopping or Proceed to Checkout.

**Checkout** – the Checkout page takes in input from the user including delivery
address, post code and country. The page also shows a snippet of the order
reminding the user of cart contents and the total price to pay. From this point,
the user is directed to a Payment page once the details entered on the page have
been validated.

**Payment** – the payment page requires the user to enter a valid card number,
including valid to dates, and security code. All the while an order snippet is
again shown on this page for completeness and user experience.

**Order Confirmation** – the final step is the confirmation page where the user
is presented a Success message once the transaction has been verified by Stripe.
From this point the user, is also sent an email confirmation of their order.

**Order History –** lists all previous orders by the user. **(End)**

**(Not logged in)** – Sign Up – create a user profile with name, email address
and Passedword. All are required fields and the email address is sent a
confirmation email in order to activate the profile. Links back to Sign-In page
to ease navigation. All fields are validated before the user is allowed to
proceed.

**Login/Sign In** – username and Password required for login. Also links back to
SignUp page to ease navigation between pages and user experience. Details are
validated

**Surface**

The site aesthetics of the site was made possible by using a variety of sources:

-   Unsplash.com
-   Pexels.com
-   Freeimages.com
-   Freepik.com
-   Thegraphicsfairy.com
-   Freedigitalphotos.net

The colour theme complements the images used in the banner on the home page. The
font is simple, and easy to read so the customers can read the description of
the desserts clearly – in mobile or desktop view.

**Skeleton**

Wireframes were drawn for mobile and desktop representation and can be found
here:

**Languages Used**

-   HTML
-   CSS
-   JavaScript
-   Python+Django
-   SQLite
-   Postgres

**Technologies used**

-   MDBootstrap
-   Fontawsome
-   Stripe
-   Heroku
-   Github
-   Gunicorn
-   VS code
-   AWS (S3)

**Code Validation**

-   PEP 8 Online Validator-Python
-   W3C validator-HTML
-   W3C validator-CSS

**Testing**

| Test Description                  | Expected outcome                                                                                                                                                                      | Actual Outcome                                                                                                                                                                            | Result                             |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Navigation Links                  | The links for categories should be able to display the sub-categories                                                                                                                 | Passed                                                                                                                                                                                    | Passed                             |
| Image hyperlinks                  | Image hyperlinks when selected should display the sun-categories                                                                                                                      | Passed- they display the category selected                                                                                                                                                | Passed                             |
| Search bar                        | User should be able to search for items within the site                                                                                                                               | Passed- searched for cake All cakes are displayed                                                                                                                                         | Passed                             |
| Register                          | User should be able to register details after clicking on signup User to enter valid credentials with non-repeatable email addresses User must meet the minimum Password requirements | Passed - details registered without a problem Passed – use of a previously registered email address is flagged to the user Passed – users are unable to use common/simple/short passwords | Passed                             |
| Logging in                        | User should be able to log-in easily after clicking on login                                                                                                                          | If registered users can log in with their details                                                                                                                                         | Passed                             |
| Order history                     | When user clicks on orders they should be able to see the items they have purchased in the past (if available).                                                                       | Passed - the customer order history is displayed in detail after they have logged in                                                                                                      | Passed                             |
| Add to cart                       | When clicked on, the product is sent to cart                                                                                                                                          | Item is successfully added to cart                                                                                                                                                        | Passed                             |
| Authentication                    | User should not be able to make purchases without logging in                                                                                                                          | Passed- Message to the user informing them that they need to make an account                                                                                                              | Passed                             |
| Stripe                            | The payment for purchase is confirmed                                                                                                                                                 | Fail- had to set up a new account and get new keys                                                                                                                                        | Passed                             |
| Admin                             | Should be able to store purchases Should be able to add on products Delete products Add new/replace product images                                                                    | Passed- checked by making a purchase Passed Passed Passed                                                                                                                                 | Passed Passed                      |
| Email                             | Email confirmation of order                                                                                                                                                           | Passed                                                                                                                                                  | Passed                             |
| Defensive design                  | “Nothing found” message when search returns no results All user inputs require validation (Bootstrap) Stripe API-for validation Stripe-Handling Network errors /invalid parameters    | Passed Passed Passed- User is unable to go to the next stage of payment without filling in the required field Passed                                                                      | Passed Passed Passed Passed        |
| Responsiveness in mobile view     | Images and content                                                                                                                                                                    | Fail- images distorted on home page -deleted images to one image                                                                                                                          | Passed                             |
| Responsiveness in 5K              | Images and Content                                                                                                                                                                    | Passed- well responsive                                                                                                                                                                   | Passed                             |
| Deployment to AWS                 | Static file code changes Created S3 bucket in AWS Configured Bucket policies and permissions to make public Upload static files Added secret/access key to test programmatic access   | Fail- added necessary libraries Passed Passed Passed - manually uploaded folder Passed – used python collectfiles to populate bucket                                                      | Passed Passed Passed Passed Passed |
| Deployment to Heroku              | Updated remote git repository with latest build to deploy to Heroku Procfile added                                                                                                    | Failed- had to import other libraries Failed- changed the code syntax from webapp to wsgi application                                                                                     | Passed Passed                      |                                                                                                                                                                                      

**Deployment to Heroku**

The following steps were taken in order to deploy this site to Heroku:

1.  Create a new app in Heroku

2.  Added Postgres from **Resources \> Submit Order**

3.  From Postgres link provided, viewed Settings and retrieve URL

4.  In virtual environment, install required dependencies:

>   Pip install **dj_database_url**

>   Pip install **install psycopg2**

5.  Create a requirements.txt file in the terminal with:

    **pip freeze \> requirements.txt**

6.  In settings.py  add import **dj_database_url** and add the following line in place of the current databases line: 

>   **DATABASES =
>   {'default':dj_database_url.parse(os.environ.get('DATABASE_URL'))} **

At the same time, create an env.py file to store variables and add to .gitignore
folder.

Add reference for SECRET KEY (from settings.py) and DATABASE URL (from Heroku).

7.  Whilst in the Settings file, add the following change:

    **ALLOWED_HOSTS = ["(whatever name you chose).herokuapp.com"]**

7.  In the terminal run the following commands in order:

>   **Python manage.py makemigrations**

>   **Python manage.py migrate**

>   To migrate current SQLite database to Postgres database

9.  Run:

    **Python manage.py createsuperuser**

    To create a superuser to access admin functionality once the site is
    accessible

    **Collecting Static Files for AWS S3 Retrieval**

2.  Log in to Amazon AWS, go to S3 and create a new S3 bucket
    (**'dessertscapital-static')** in the region closest to you. Configure the
    bucket for static web site hosting, and enable public access as directed.
    Copy the CORS configuration as specified and create a bucket user in IAM
    (remember to download the credentials.csv when prompted).

3.  Go to terminal window and run:

    **pip install Django-storages**

    **pip install boto3**

4.  Go to settings.py and add **‘storages’, **to **INSTALLED_APPS**. Then add
    the lines below in the relevant section, replacing previous references:

    **STATIC_URL = '/static/'**

    **MEDIA_URL = '/media/'**

    **STATIC_ROOT = os.path.join(BASE_DIR, 'static')**

    **MEDIA_ROOT = os.path.join(BASE_DIR, 'media_store')**

    **AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")**

    **AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")**

    **AWS_STORAGE_BUCKET_NAME = 'dessertscapital-static'**

    **AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME**

    **AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}**

    **AWS_DEFAULT_ACL = None**

    **AWS_LOCATION = 'static'**

    **STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)**

    **STATICFILES_STORAGE= 'storages.backends.s3boto3.S3Boto3Storage'**

    **DEFAULT_FILE_STORAGE= 'storages.backends.s3boto3.S3Boto3Storage'**

5.  Create a new file in project folder (same folder where settings.py is
    located) called **custom_storages.py** with following commands:

    **from django.conf import settings**

    **from storages.backends.s3boto3 import S3Boto3Storage**

    **class StaticStorage(S3Boto3Storage):**

    **location = settings.STATICFILES_LOCATION**

    **class MediaStorage(S3Boto3Storage):**

    **location = settings.MEDIAFILES_LOCATION**

6.  Return to the terminal window and run:

>    **python3 manage.py collectstatic**

>   This command will populate the S3 bucket with all of the relevant static
>   files.

15.  Return to Heroku dashboard, and click on **Settings** \> **Reveal Config
    Vars** and add the specified keys from relevant py, Heroku-Postgres, email
    service provider and AWS credentials as required:

![](media/e7e7f997bd3d186e4b64b757d4673270.png)

16.  At the Heroku dashboard, click **Deploy** and then select **Github** as the
    Deployment method.

2.  Search repositories for correct project and click **Connect**.

3.  Back at the terminal window, run the following command:

    **pip install gunicorn**

4.  Create requirements file using the following command:

    **pip freeze \> requirements.txt**

5.  Finally, create a Procfile (be sure to use a capital P) and add the
    following command and save:

    **web: gunicorn store.wsgi**

6.  In the terminal, run the following commands to push changes to GitHub:

>   **Git init**

>   **Git add . (or git add –all)**

>   **Git commit – m “message”**

>   **Git push**

22.  From the Heroku dashboard, click **Deploy Branch** from **Manual Deploy**

2.  On completion of the build, ensure there are no errors, and click Open App
    in the top-right of the screen.

**Future Features**

-   Different payment methods other than Stripe

-   Use live API to show location of deliveries (Uber, just eat)

**Acknowledgements**

I would like to say a huge Thankyou to Brian for his help and support throughout
the course. His advice and support went a long way.

Thank you to Alexander at student care for his support.

**DISCLAIMER: This project and its use are entirely for education purposes
ONLY**
