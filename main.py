import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create/', methods=['GET', 'POST'])
def create():
    donors = Donor.select()
    if request.method == 'GET':
        return render_template('create.jinja2', donors=donors)
    donor_name = request.form['donor']
    donor_amount = int(request.form['amount'])
    Donation(donor=donor_name, value=donor_amount).save()
    return redirect(url_for('home'))

@app.route('/donor/', methods=['GET', 'POST'])
def donor():
    donors = Donor.select()
    if request.method == 'GET':
        return render_template('donor.jinja2')
    donor_name = request.form['donor']
    Donor(name=donor_name).save()
    return redirect(url_for('home'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

