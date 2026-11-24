# this is the "web_app/routes/stocks_routes.py" file ...

import re

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.stocks import fetch_stocks_csv, format_usd

stocks_routes = Blueprint("stocks_routes", __name__)


@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")


@stocks_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def stocks_dashboard():
    fields = request.form if request.method == "POST" else request.args
    symbol = fields.get("symbol", "NFLX").strip().upper()
    if not re.fullmatch(r"[A-Z0-9][A-Z0-9.-]{0,19}", symbol):
        flash("Enter a valid ticker symbol, such as MSFT or BRK.B.", "danger")
        return redirect(url_for("stocks_routes.stocks_form"))

    try:
        prices = fetch_stocks_csv(symbol=symbol)
    except (OSError, ValueError):
        flash("Stock data is temporarily unavailable. Please try again shortly.", "danger")
        return redirect(url_for("stocks_routes.stocks_form"))

    if prices.empty or not {"timestamp", "adjusted_close"}.issubset(prices.columns):
        flash(f"No price data was returned for {symbol}. Check the ticker or try again later.", "danger")
        return redirect(url_for("stocks_routes.stocks_form"))

    prices = prices[["timestamp", "adjusted_close"]].dropna().sort_values("timestamp", ascending=False)
    if prices.empty:
        flash(f"No closing prices were found for {symbol}. Try another ticker.", "danger")
        return redirect(url_for("stocks_routes.stocks_form"))

    latest = prices.iloc[0]
    return render_template(
        "stocks_dashboard.html",
        symbol=symbol,
        latest_close_usd=format_usd(latest["adjusted_close"]),
        latest_date=latest["timestamp"],
        data=prices.to_dict("records"),
    )


#
# API ROUTES
#

@stocks_routes.route("/api/stocks.json")
def stocks_api():
    print("STOCKS DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    symbol = url_params.get("symbol") or "NFLX"

    try:
        df = fetch_stocks_csv(symbol=symbol)
        data = df.to_dict("records")
        return {"symbol": symbol, "data": data}
    except Exception as err:
        print('OOPS', err)
        return {"message": "Market Data Error. Please try again."}, 404
