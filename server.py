from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """view homepage"""

    return render_template("homepage.html")

@app.route("/search-input-form")
def search():
    """search and return time slots.  """
    selected_date = request.form.get("reservation-date")
    start_hour = request.form.get("start_hour")

    return render_template("search_results.html")






if __name__ == "__main__":
    connect_to_db(app) # connect to your database before app.run gets called, so that Flask can access your database.
    app.run(host="0.0.0.0", debug=True)
