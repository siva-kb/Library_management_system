# Library_management_system
Welcome to our Library Management System repository! This repository houses the source code and resources for our comprehensive library management application built with Django. Whether you're a librarian or administrator, this system provides a robust platform for efficiently managing library operations.
Features:

Book Management: Easily add, update, and remove books from the library catalog.
Borrower Management: Maintain borrower records, register new borrowers, and manage their borrowing privileges.
Borrowing Transactions: Facilitate borrowing and returning of books, including tracking due dates and managing fines.
An additional fine of Rs. 5 will be applied for each day past the due date, commencing after a 14-day grace period
Ensure that a member's accrued debt does not exceed Rs. 500.


Installation:


Follow these steps to set up the project on your local machine:

1.Clone the repository:
                  git clone <repository_url>

2.Navigate to the project directory:
                cd library_management_system

3.Install dependencies:
               pip install -r requirements.txt

4.Install python and django:
               pip install django

5.Perform database migrations:
               python manage.py migrate

Start the development server:
               python manage.py runserver

6.Create a superuser account:
               python manage.py createsuperuser
           or  login with username: admin123 , password:admin

7.Access the application in your web browser at http://localhost:8000.

USAGE

Login: Use the superuser credentials created earlier to log in or using given username and password.
Explore: Navigate through the intuitive interface to access different functionalities.
Manage Books and Borrowers: Add, update, or remove books and borrower information as needed.
Handle Borrowing Transactions: Process borrowing and returning of books, keeping track of due dates and fines.
Logout: Always remember to log out for security purposes.

Contact:
For any questions or support, please reach out to sivamuruganb637@gmail.com

![Homepage](https://github.com/siva-kb/Library_management_system/assets/163427874/47b5ed06-5ac2-4676-b9c6-b6e6d8f9d70b)

![Admin login page](https://github.com/siva-kb/Library_management_system/assets/163427874/8b2f441f-fa64-41d4-a69c-3e5fb0f32ea5)

![Add new books](https://github.com/siva-kb/Library_management_system/assets/163427874/3f5f767e-9ae8-490d-87c8-be052d31d7b2)

![book list](https://github.com/siva-kb/Library_management_system/assets/163427874/055b84b5-e605-40db-9a53-19b5bff8969e)

![Issue book](https://github.com/siva-kb/Library_management_system/assets/163427874/64e741b7-c673-4700-ad74-e83e6f4665e0)

![borrow details](https://github.com/siva-kb/Library_management_system/assets/163427874/516a2fb8-9400-4d92-acfc-7a65a817d83e)

