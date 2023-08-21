# Django RestFramework Custom User API

This repository contains a Django RestFramework project that showcases the implementation of a custom user model with various user-related APIs. The custom user model allows for more flexibility in managing user data and authentication processes.

## Features

- User Registration: Register new users with required information.
- User Login: Authenticate users and provide access tokens for API authorization.
- Profile: Retrieve and update user profile information.
- Change Password: Allow users to change their account passwords.
- Send Reset Password Email: Send email notifications to reset forgotten passwords.
- Verify Reset Password: Verify the reset password token and update the password.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AnilMohite/django_backend.git
   cd django-restframework
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Contributions

Contributions are welcome! If you find any issues or would like to add more features, feel free to create a pull request or open an issue in this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
