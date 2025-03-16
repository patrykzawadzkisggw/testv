# testv

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/patrykzawadzkisggw/testv.git
   cd testv
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install djangorestframework:
   ```bash
   pip install djangorestframework
   ```

5. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser account:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Running the Application

To run the Django application, follow these steps:

1. Ensure the virtual environment is activated:
   ```bash
   source venv/bin/activate
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

3. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## API Endpoints

The following API endpoints are available:

1. User Registration and Login:
   - `POST /api/register/` - Register a new user
   - `POST /api/login/` - Login an existing user

2. Upload Encrypted Folder:
   - `POST /api/upload/` - Upload an encrypted folder

3. Download Encrypted Folder:
   - `GET /api/download/` - Download an encrypted folder

4. Change Encryption Password:
   - `POST /api/change-password/` - Change the encryption password
