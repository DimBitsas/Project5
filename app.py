from flask import (Flask, g, render_template, flash, 
                   redirect, url_for)

import models
import forms


app = Flask(__name__)
app.secret_key = "soemsecretkey312388"


@app.before_request
def before_request():
  """Connect to the database before each request"""
  g.db = models.DATABASE
  g.db.connect()
  
@app.after_request
def after_request(response):
  """Close the database connection after each request"""
  g.db.close()
  return(response)

@app.route('/')
@app.route('/entries')
def entries():
    """List of journal entries"""
    entries = models.Entry.select()
    return render_template('index.html', entries=entries)

@app.route('/entry', methods=('GET', 'POST'))
def new_entry():
    """ Add new entry """
    form = forms.EntryForm()
    if form.validate_on_submit():
        models.Entry.create(title=form.title.data.strip(),
                            date=form.date.data,
                            time_spent=form.time_spent.data,
                            learned=form.learned.data.strip(),
                            resources=form.resources.data.strip())
        flash('New entry added!!', 'success')
        return redirect(url_for('entries'))
    return render_template('new.html', form=form)

@app.route('/entries/edit/<entryid>', methods=('GET', 'POST'))
def edit_entry(entryid=None):
    """ Edit entry """
    entry = models.Entry.get(models.Entry.id == entryid)
    form = forms.EntryForm()
    if form.validate_on_submit():
      models.Entry.update(title=form.title.data.strip(),
                          date=form.date.data,
                          time_spent=form.time_spent.data,
                          learned=form.learned.data.strip(),
                          resources=form.resources.data.strip()
                          ).where(models.Entry.id == entryid).execute()
      flash('Edit successful!!', 'success')
      return redirect(url_for('entries'))

    form.title.data = entry.title
    form.date.data = entry.date
    form.time_spent.data = entry.time_spent
    form.learned.data = entry.learned
    form.resources.data = entry.resources

    return render_template('edit.html', form=form)

@app.route('/details/<entryid>')
def entry_details(entryid=None):
    """ Displaying journal entry with all fields """
    entry = models.Entry.get(models.Entry.id == entryid)
    return render_template('detail.html', entry=entry)

@app.route('/delete/<entryid>')
def delete_entry(entryid=None):
    """ Delete a journal entry """
    models.Entry.delete().where(models.Entry.id == entryid).execute()
    flash('Deleted successfully!!', 'successfully' )
    return redirect(url_for('entries'))

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True)