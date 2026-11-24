# my-first-app-fall-2026

## prerequisites

Install python version 3.x (i.e. using Anaconda)

## setup

1. Clone [the repo](https://github.com/hayeon3683/my-first-app-fall-2026) from GitHub, and put it somewhere like your Desktop.
2. Navigate to the local repo from the command line:

```sh
cd ~/Desktop/my-first-app-fall-2026
```

3. Create a new anaconda virtual environment called "rps-env" (first time only):

```sh
conda create -n rps-env python=3.11
```

4. Activate the virtual environment:

```sh
conda activate rps-env
```

5. Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

The stocks functionality requires an AlphaVantage API key. Obtain an AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"
```

## Usage

### Command Line App

Run the example script:

```sh
python app/my_script.py

# alternatively:
python -m app.my_script
```

Rock-Paper-Scissors:

```sh
python -m app.rps
```

Stocks dashboard:

```sh
python -m app.stocks
```

### Web App

```sh
# if we have the FLASK_APP=web_app env var in the ".env" file:
flask run

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

To run tests:

```sh
pytest
```

## Web App Attribution

- The shared layout uses [Jinja template inheritance](https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance) and a [Bootstrap 5 responsive navbar](https://getbootstrap.com/docs/5.3/components/navbar/). The plum color palette and page layouts were customized for Hayeon's Web Lab, using a [compass icon from Bootstrap Icons](https://icons.getbootstrap.com/icons/compass/).
- The stock route uses [Flask message flashing](https://flask.palletsprojects.com/en/stable/patterns/flashing/) to show a message after redirecting users back to the stock form when a ticker is invalid or returns no price data. The shared layout shows the message as a [dismissible Bootstrap alert](https://getbootstrap.com/docs/5.3/components/alerts/). The dashboard uses [Plotly.js](https://plotly.com/javascript/line-charts/) for its interactive price chart.

## AI Assistance

I used [OpenAI ChatGPT](https://chatgpt.com/) to help implement the shared Bootstrap layout, customize the plum navbar and compass icon, improve stock lookup error messages, and add a daily price table to the stocks dashboard.
