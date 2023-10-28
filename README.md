# URL Shortener
A simple URL shortener built using Django and Django Rest Framework.

## Features
Convert long URLs into short links.
Quick access to basic stats for each shortened link (if implemented).
Setup & Run

Clone the repository

```bash
git clone https://github.com/uluk001/Neobis_Shortener_Project.git
cd Neobis_Shortener_Project
```

Set up a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```
Start the server


```bash

python manage.py runserver
```

The server should now be accessible at http://127.0.0.1:8000/.

## Usage
To shorten a URL:

Make a POST request to http://127.0.0.1:8000/shorten/ with a parameter original_url containing your long link.
You'll receive a shortened version of your URL in the response.



## Contribution
<br>

Pull requests: If you have a desire to fix a bug, add a new feature or improve an existing one, or you can improve the current interface, you can fork the project, make your changes in a separate branch and invite us to make a pull request with your changes. We will look at your contribution and, if everything is in order, we will add it to the main project.
<br>


## Author

[GitHub](https://github.com/uluk001)  
[LinkedIn](https://www.linkedin.com/in/ismailov-uluk-92784a233/)
