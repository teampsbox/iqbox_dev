from flask import render_template, flash, redirect, url_for
from datetime import datetime
from app import app, db
from app.models import Quote
from app.forms import QuoteForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = QuoteForm()
    quotes = Quote.query.order_by(Quote.timestamp.desc()).all()
    if form.validate_on_submit():
        quote = Quote(title=form.title.data, body=form.body.data, by=form.by.data)
        db.session.add(quote)
        db.session.commit()
        flash('Shared successfully!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, quotes=quotes)
