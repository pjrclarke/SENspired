
![SENspired](/media/readmeimages/logo.png)

SENspired, my latest web development endeavour, embodies the principles of Agile methodologies, fostering a dynamic and collaborative relationship with a real client. Our weekly meetings served as a platform for transparent communication and feedback, allowing for constant iteration and refinement of the website's features. Notably, the site boasts a robust event management system, providing administrators with a user-friendly interface to effortlessly create, modify, and remove events. This functionality ensures a streamlined and efficient booking process for the public, aligning perfectly with SENspired's mission.

Moreover, I have implemented a sophisticated system empowering users to manage booking requests for the organisation's rented rooms. This comprehensive solution enables individuals to seamlessly create, read, update, and delete their booking requests, enhancing the overall user experience. The design of the platform goes beyond functionality, incorporating a stylish aesthetic that reflects the organisation's ethos.

While the website's current iteration showcases the initial CRUD (Create, Read, Update, Delete) functionality for both administrators and users, it represents just the tip of the iceberg. The project's expansive scope necessitates a phased approach, and this initial release serves as a preview of the site's potential. As I continue to work on expanding its capabilities, I am excited about the positive impact SENspired will have on its users and the community it serves. The journey is ongoing, and I look forward to bringing even more innovative features and enhancements to the site in the future.

<br>

![SENspired](/media/readmeimages/responsive.png)

<br>
<br>

Please access the website through this link: [SENspired](https://senspired-efbab7dd64be.herokuapp.com/).


<br>

# Contents

- [Project](#project)
  - [Objective](#objective)
  - [Site User's Goal](#site-users-goal)
  - [Site Owner's Goal](#site-owners-goal)
- [User Experience (UX) user](#user-experience-ux-user)
  - [Primary Goal](#primary-goal)
    - [First Time Visitor](#first-time-visitor)
    - [Returning Visitor](#returning-visitor)
    - [Frequent Visitor](#frequent-visitor)
- [User Experience (UX) Site owner](#user-experience-ux-site-owner)
  - [User Stories](#user-stories)


- [Creation Process](#creation-process)
  - [Design Prototype (Wireframes)](#design-prototype-wireframes)
    - [Desktop Wireframes](#desktop-wireframes)
    - [Tablet Wireframes](#tablet-wireframes)
    - [Mobile Wireframes](#mobile-wireframes)
  - [Project Management](#project-management)
    - [GitHub Projects Board](#github-projects-board)
    - [Milestones](#milestones)
    - [Epics](#epics)
    - [User Stories](#user-stories-1)
  - [Database Schema (ERD)](#database-schema-erd)
  - [Site Structure](#site-structure)
- [Design Choices](#design-choices)
  - [Typography](#typography)
  - [Color Scheme](#color-scheme)
- [Features](#features)
  - [Site Responsive Navigation Bar](#site-responsive-navigation-bar)
  - [Carousel](#carousel)
  - [Footer](#footer)
  - [Home Page](#home-page)
  - [Find the Perfect Buddy Page](#find-the-perfect-buddy-page)
    - [Buddy Search](#buddy-search)
    - [Future Features for Buddy Search](#future-features-for-buddy-search)
    - [Buddy Details](#buddy-details)
    - [Future Features for Buddy Matching](#future-features-for-buddy-matching)
  - [Booking of the courts](#booking-of-the-courts)
    - [Booking requirements](#booking-requirements)
    - [Making a reservation](#making-a-reservation)
    - [Edit/Delete Functionality](#editdelete-functionality)
    - [Staff Dashboard](#staff-dashboard)
    - [Bookings in the past](#bookings-in-the-past)
    - [Future features for Booking](#future-features-for-booking)
  - [Contact Us page](#contact-us-page)
    - [Inquiry Confirmation Message](#inquiry-confirmation-message)
    - [Future Features for Contact Us](#future-features-for-contact-us)
      - [CLI Message](#cli-message)
  - [Profile Icon](#profile-icon)
    - [Contact Info](#contact-info)
      - [Add Contact Info](#add-contact-info)
      - [View Added Contact Info](#view-added-contact-info)
      - [Edit Contact Info](#edit-contact-info)
      - [Delete Contact Info](#delete-contact-info)
    - [Buddy Profile](#buddy-profile)
      - [Add Buddy Profile](#add-buddy-profile)
      - [View Added Buddy Details](#view-added-buddy-details)
      - [Edit Buddy Details](#edit-buddy-details)
      - [Delete Buddy Details](#delete-buddy-details)
    - [Your Bookings](#your-bookings)
  - [Sign Up Page](#sign-up-page)
  - [Sign In Page](#sign-in-page)
  - [Logout Page](#logout-page)
    - [Future Features Sign in functionality](#future-features-sign-in-functionality)
  - [403, 404 and 500 Error Pages](#403-404-and-500-error-pages)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks and Software](#frameworks-and-software)
- [Python Packages](#python-packages)
- [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [External Testing](#external-testing)
    - [Automated Testing](#automated-testing)
- [Project Deployment](#project-deployment)
  - [Create a new GitHub Repository from CI template](#create-a-new-github-repository-from-ci-template)
  - [Install Django and the supporting libraries](#install-django-and-the-supporting-libraries)
  - [ElephantSQL Database](#elephantsql-database)
  - [Cloudinary API](#cloudinary-api)
  - [Heroku Deployment](#heroku-deployment)
  - [To fork the repository on GitHub](#to-fork-the-repository-on-github)
  - [To create a local clone of a project](#to-create-a-local-clone-of-a-project)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

[Back to top](#contents)

# Project

### Objective

I've developed a strong passion for coding, finding immense enjoyment in this project. The site's potential is vast, with an ongoing scope. Inspired by my children's involvement in a kids' group, I collaborated with the organisers to create a platform tailored to their needs. Although the site currently focuses on individual tasks for admins and users, the project is set to evolve further.

My goal in this development was to leverage my skills in HTML, CSS, JavaScript, Python, Bootstrap, and the Django Framework. While the booking system and search functionality are works in progress, the project already features several custom models with complete CRUD functionality. The next version will see enhancements to both the booking system and search functionality, continuing to elevate this project.

### Site Users Goal

As a site user, my primary desire is to effortlessly book events and seamlessly request a room for personal use, with the added convenience of receiving updates when I click on the respective features.

### Site Owners Goal

As the site owner, my goal is to easily create events, providing comprehensive information such as the event name, time, destination, and additional details for user clarity. Additionally, I aim to efficiently manage booking requests from the public, having the ability to approve or deny them as needed.

[Back to top](#contents)

# User Experience (UX) User

### Primary Goal

The site's primary goal for users is to effortlessly stay informed about SENspired events and easily submit booking requests for the available rooms.

### First Time Visitor

-  When A first time user arrives on the the index page, it hits you with a burst of colors and a bunch of cool features. It's like a lively playground, with loads of different things to check out and explore.
- A user can register, log in and logout.
- A user can see events. 
- A user can see details of events including an dates, address and time when they have signed in.
- A signed in user can create a booking request for the SENspired room. 
- A signed in user can update, read and delete their booking request. 
- A signed is user can see the status of their booking request on the my bookings page.
- A user is informed about a successful booking.
- A user can go onto their booking page to see all events booked and see the requests for any room bookings.
- A user can add/edit/delete their contact information which can be accessed from the Profile Icon on the right. They are informed about having created, updated or deleted their Contact info.
- A user can access useful information in the footer:
    - Links to social media
    - Opening hours
    - Site navigation
    - Contact information
    - My website
- A user can see the coming soon pages so know that the site is currently under maintenance. 


### Returning Visitor

- A user can easily sign in and access majority of the features of the website.
- A user with filled in Contact info can also register for an event.
- A user can make requests to book the room. 

### Frequent Visitor

- A frequent user can check the events and register for the new ones.
- a frequent user can make room booking requests.

### User Stories
- As a **user**, I would like to **view the apps homepage** so that I can **learn about the app and see what services it provides**.
- As a **user** I can **locate the navigation area** so that I can **easily access different parts of the website**
- As a **user**, I can **access relevant information about contact information and social media links without having to scroll back to the top of the page** so that I can **visit SENspired, contact SENspired and follow SENSpired online**.
- As an **unregistered user** I want to be able **to sign up onto the website** so that I can **access websites functionality and content**.
- As a **registered user** I want to be able **to sign in into my account** so that I can **get access to the website's functionality and options**.
- As a **signed in user** I want to be able **to sign out of my account** so that I can **keep my account private and safe**.
- As a **signed in user with an active profile** I can **create a booking request** so that **I can see the my bookings area to check in for updates.**
- As a **user**, I can **edit my booking request** as long as the status isn't approved, to **update my preferences regarding the booking time, date and name**.
- As a **registered user** I can **press delete button on my request** so that I can **delete all provided information regarding my booking**
- As a **registered user** I can **press delete button on my user profile** so that I can **delete all provided information regarding my contact details**.
- As a **user**, I can **edit my user profile** to **update my personal details**.
- As a **user** I can **open the events booking** so that I can **register for an event**.
- As a **user** I can **be visually attracted to the app and see the main site features** so that I can **quickly get an idea what the app offers**.
- As a **user I want to be informed about different user actions** so that I can **be sure that the intended action took place**.
- As a **user** I can **enjoy browsing the webpage while looking for information** so that **I don't feel compelled to leave**.
- As a **user** I want to **press a cancel button which will take me to the previous page** so that I **don't have to use the Back button**.
- As a **user** I can **easily understand what the table labels mean** so that I can **avoid any unnecessary confusion**.

<br>

[Back to top](#contents)

# User Experience (UX) Site owner / Admin

### User Stories

- As the **site owner**, I want to be able to **sign in to my account so that I can get access to the website's functionality and options**.
- As a **signed-in site owner**, I want to be able to **sign out of my account so that I can keep my account private and safe**.
- As a **signed-in site owner** via the **admin panel**, I can **create events with a name, description, time, date and image**.
- As a **signed-in site owner** via the **admin panel** , I can **Edit the events name, description, time, date and image**.
- As a **signed-in site owner** via the **admin panel**, I can **delete the events name, description, time, date and image**.
- As a **signed-in site owner** via the **admin panel**, I can **View requests made by general users for room bookings**.
- As a **signed-in site owner** via the **admin panel**, I can **approve requests made by general users for room bookings**.
- As a **signed-in site owner** via the **admin panel**, I can **delete requests made by general users for room bookings**.


[Back to top](#contents)