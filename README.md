#URL Shortener
A simple URL shortener built using Django and Django Rest Framework.

##Features
Convert long URLs into short links.
Quick access to basic stats for each shortened link (if implemented).
Setup & Run
Clone the repository

```bash

git clone https://github.com/yourusername/urlshortener.git
cd urlshortener
Set up a virtual environment and install dependencies
```

```bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Apply migrations
```

```bash

python manage.py migrate
Start the server
```

```bash

python manage.py runserver
The server should now be accessible at http://127.0.0.1:8000/.
```

##Usage
To shorten a URL:

Make a POST request to http://127.0.0.1:8000/shorten/ with a parameter original_url containing your long link.
You'll receive a shortened version of your URL in the response.