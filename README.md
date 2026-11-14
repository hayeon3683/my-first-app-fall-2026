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

## Testing

To run tests:

```sh
pytest
```
