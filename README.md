# Project 3
Web Programming with Python and JavaScript

## You can see this project on:
### https://cs50project3pizza.herokuapp.com/

#### For administrations, go to /admin and credentials are admin-admin

## Structure
This project contains the main directory (called pizza) and two Django projects: Users and orders

## Pizza

This contains the files necessary for the initialization of the project and small changes in those files:

### settings.py

I added MEDIA_ROOT AND MEDIA_URL to be able to upload photos in the database.

### urls.py

Lines have been added to allow routes for orders and users applications

## Users

This application manages the login, registration and logout of the project.

### views.py

Contains the register, sign-in and fun_logout functions that are used to register, log in and log out respectively.

### Templates/users

I have used two Colorlib templates (copyright in the footer) that I have modified to fit the theme of the project (a pizza restaurant) adding pizza background images.

Also, in register.html I have added more fields to be able to make the registration requested in the requirements through a form defined in forms.py

### forms.py
I have created forms for registration and login to make their validation easier (RegisterForm and UserLoginForm)


### static

Here all the static files of the users application are stored. I have the structure divided into different folders so that it is easier to find the different necessary files


## Orders

This application contains all the logic of the application to order different dishes from the online menu.

### Templates/orders

I have used a Colorlib template for the application. I have removed various categories that I was not interested in and added some of my own (order_list.html, single_order, admin_orders.html)

Also I have created a template that contains the navbar and the footer so that all the html inherit from it. I have also added a page for when an unexpected error happens.

### Models

I have decided to create the following models:

#### Category

Contains the categories of dishes.

#### MenuItem1

Contains the different Menu items that the restaurant has that will be displayed in menu.html. You can add a photo on them

#### Topping

Contains the possible toppings of the pizzas.

#### Sub_Extra

Contains the possible extras of the subs. The extras that are added to each Sub are controlled by a many-to-many relationship.

#### OrderItem

Represents the ordered items of an order.

#### Order

Represents a user's requested order. Contains a ForeignKey to the corresponding OrderItems

#### CartItem

They represent the items inside the shopping cart. These disappear when an order is placed.

## Personal Touch 
My personal touch is to send an email when the user places an order. 
I have added different settings in settings.py to allow sending emails via Gmail.

EMAIL_HOST_PASSWORD is an environment variable since it contains the password of the account from which emails are sent.

I have also used to send email the EmailMessage class provided by Django which creates an EmailMessage object which is then sent using the .send () method.


### Special Pizza

Is a pizza with Pepperoni, Mushrooms, Onions, Ham and Hamburguer

