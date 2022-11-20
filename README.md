# MY CRED

A basic password manager rest API, that I build for my college presentation. This project was made with collaboration of my friend [Lakhan](https://github.com/1akhanBaheti).
Lakhan utilized this API to build a flutter app. The app is not yet published, but you can find the code [here](https://github.com/1akhanBaheti/Password-Manager).

I have used the following technologies:

- Django
- Django restframework
- Postgresql

## Features

1. Uses rest API, therefore can be used anywhere.
2. Encrypt the password before storing it to the database.
3. Uses token based authentications.
4. Uses MVC architecture.

## How do I use this?

1. Setup environment variables, by taking the .env.example file as reference. (You cannot use same file you will have to create a .env file or change the name of .env.example to .env).
2. Make and activate virtual environment, by using the following commands:
   ```
   python3 -m venv env
   source env/bin/activate
   ```
3. Install the requirements, by using the following command:
   `pip install -r requirements.txt`
4. Make migrations, by using the following command:

```
python manage.py makemigrations
python manage.py migrate
```

5. (Optionally)Create a superuser, by using the following command:

   ```
   python manage.py createsuperuser
   ```

6. Run the server, by using the following command:

   ```
   python manage.py runserver
   ```

Now go to the browser and type `http://127.0.0.0:8000/admin` to access admin panel. NOTE: You need to create a superuser first(step 5).

I have provided the postman collection, so you can use that to test the API.

You can use the endpoints to:

- Register a user.
- Login a user.
- Create a password.
- Get all passwords, related to logged in user.
- Update a password, given that the creator of password is trying to update it.
- Delete a password, given that the creator of password is trying to delete it.

## Future Scope

1. Use OTP based authentication, to avoid remembering even one password.
2. Use asymmetric encryption.
3. Use JWT for authentication.
4. Use test based development.

## How do I contribute?

1. Fork the repository.
2. Clone the repository.
3. Make changes.
4. Create a pull request.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
