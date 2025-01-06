# Django Open Source Shakespeare API

This project is a read-only API for consuming the Open Source Shakespeare Database, which is hosted at [Open Source Shakespeare](https://github.com/catherinedevlin/opensourceshakespeare). The API is built using Django and provides a user-friendly interface to access Shakespeare's works. For more information about Open Source Shakespeare, please visit [www.opensourceshakespeare.org](www.opensourceshakespeare.org)

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- Read-only access to Shakespeare's works
- User-friendly interface
- Built with Django for robust performance

## Technologies Used

This project is built using the following technologies:

- **Django**: 4.2.16
- **django-environ**: 0.11.2 (for environment variable management)
- **django-ninja**: 1.3.0 (for building APIs)
- **psycopg2-binary**: 2.9.10 (PostgreSQL adapter for Python)
- **Python**: 3.10.7

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

   ```
   git clone https://github.com/MGadhvi/project-shakespeare
   cd project-shakespeare
   ```
   
2. **Create a virtual environment (optional but recommended)**: 
   
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required packages**:
   
   ```
   pip install -r requirements.txt
   ```
4. **Set up environment variables**:

Create a .env file in the root directory of the project and add your environment variables. For example:

   ```
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/dbname
   ```
    
5. **Run database migrations** :
   ```
   python manage.py migrate
   ```
6. **Run the development server**: 
	
   ```
   python manage.py runserver
   ```
7. **Access the application**:

Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the frontend. 

## Usage

This project provides a read-only interface to access the works of Shakespeare. You can navigate through the various plays and poems, view their contents, and explore the rich literary heritage of Shakespeare.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to report a bug, please open an issue or submit a pull request.
