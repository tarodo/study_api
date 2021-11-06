# Bit.ly using by console
## Start
Make sure you have a python3

Install virtual environment:

```python3 -m venv \venv```

And start it:

```venv\Scripts\activate.bat```

Install requirements:

```pip install -r requriements.txt```

## Key

Create your own api key on https://app.bitly.com/settings/api/

Create ```.env``` file by

```.env.Example > .env``` and add there your own key


## Usage
Do not forget replace ```your_link``` with real link

```python main.py your_link```

You will have a shorten link if you use a real link.

You will have a count of clicks if you use bitlink with this script.