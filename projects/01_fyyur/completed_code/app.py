#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import dateutil.parser
import babel
from datetime import datetime
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from forms import *
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
DEBUG = True
migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key=False)
    start_time = db.Column(db.DateTime(timezone=False), nullable=False)


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=False), nullable=True, default=db.func.current_timestamp())
    name = db.Column(db.String, nullable=False, unique=True)
    genres = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(500))
    website = db.Column(db.String(200))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref=db.backref('venue', lazy=True))


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=False), nullable=True, default=db.func.current_timestamp())
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    genres = db.Column(db.String(120), nullable=False)
    seeking_venue = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(500))
    website = db.Column(db.String(200))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref=db.backref('artist', lazy=True))


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  venues_recent = Venue.query.filter(Venue.created_at.isnot(None)).order_by(Venue.created_at.desc()).limit(10).all()
  artists_recent = Artist.query.filter(Artist.created_at.isnot(None)).order_by(Artist.created_at.desc()).limit(10).all()

  return render_template('pages/home.html', venues=venues_recent, artists=artists_recent)


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  data=[]
  areas_list = Venue.query.distinct('city', 'state').all()
  for area in areas_list:
    record = {
      'city': area.city,
      'state': area.state,
      'venues': Venue.query.filter_by(city=area.city, state=area.state)
    }
    data.append(record)

  return render_template('pages/venues.html', areas=data);

@app.route('/venues/search', methods=['POST'])
def search_venues():
  search_term = request.form.get('search_term', '')

  # search by city and state, should be improved by providing a picklist with by what term to search
  if search_term.count(','):
    city_state = search_term.split(',')
    city=city_state[0]
    state=city_state[1]
    data = Venue.query.filter_by(city=city.strip(), state=state.strip()).all()
  else:
    data = Venue.query.filter(Venue.name.ilike('%{}%'.format(search_term.lower()))).all()

  response={
    "count": len(data),
    "data": data
  }

  return render_template('pages/search_venues.html', results=response, search_term=search_term)

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id

  show_dict = {}
  upcoming_shows = []
  past_shows = []
  current_time = datetime.now()

  data = Venue.query.get(venue_id)
  data.genres = data.genres.strip('{,}').split(',')

  shows = data.shows
  for show in shows:
    show_dict['artist_id']=show.artist.id
    show_dict['artist_name'] = show.artist.name
    show_dict['artist_image_link'] = show.artist.image_link
    show_dict['start_time']=format_datetime(str(show.start_time))
    if show.start_time > current_time:
      upcoming_shows.append(show_dict.copy())
    else:
      past_shows.append(show_dict.copy())

  data.upcoming_shows = upcoming_shows
  data.upcoming_shows_count = len(upcoming_shows)
  data.past_shows = past_shows
  data.past_shows_count = len(past_shows)

  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  error = False
  try:
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']
    address = request.form['address']
    phone = request.form['phone']
    genres = VenueForm(request.form).genres.data
    facebook_link = request.form['facebook_link']

    venue = Venue(name=name, city=city, state=state, address=address, phone=phone, genres=genres, facebook_link=facebook_link)
    db.session.add(venue)
    db.session.commit()

  except Exception:
    error = True
    db.session.rollback()
  finally:
    db.session.close()
    if error:
      flash('An error occurred. Venue ' + name + ' could not be listed.', 'error')
    else:
      flash('Venue ' + name + ' was successfully listed!', 'success')

  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  response = {}
  try:
    Venue.query.filter_by(id=venue_id).delete()
    db.session.commit()
    response['success'] = True
  except Exception:
    db.session.rollback()
    response['success'] = False
    flash('An error occurred deleting a Venue!', 'error')
  finally:
    db.session.close()
    return jsonify(response)

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  data = Artist.query.all()
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  search_term = request.form.get('search_term', '')

  # search by city and state, should be improved by providing a picklist with by what term to search
  if search_term.count(','):
    city_state = search_term.split(',')
    city=city_state[0]
    state=city_state[1]
    data = Artist.query.filter_by(city=city.strip(), state=state.strip()).all()
  else:
    data = Artist.query.filter(Artist.name.ilike('%{}%'.format(search_term.lower()))).all()

  response = {
    "count": len(data),
    "data": data
  }
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id

  show_dict = {}
  upcoming_shows = []
  past_shows = []
  current_time = datetime.now()

  data = Artist.query.get(artist_id)
  data.genres = data.genres.strip('{,}').split(',')

  shows = data.shows
  for show in shows:
    show_dict['venue_id'] = show.venue.id
    show_dict['venue_name'] = show.venue.name
    show_dict['venue_image_link'] = show.venue.image_link
    show_dict['start_time'] = format_datetime(str(show.start_time))
    if show.start_time > current_time:
      upcoming_shows.append(show_dict.copy())
    else:
      past_shows.append(show_dict.copy())

  data.upcoming_shows = upcoming_shows
  data.upcoming_shows_count = len(upcoming_shows)
  data.past_shows = past_shows
  data.past_shows_count = len(past_shows)

  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist = Artist.query.get(artist_id)
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  error = False
  try:
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']
    phone = request.form['phone']
    genres = ArtistForm(request.form).genres.data
    facebook_link = request.form['facebook_link']

    artist = Artist.query.get(artist_id)
    artist.name = name
    artist.city = city
    artist.state = state
    artist.phone = phone
    artist.genres = genres
    artist.facebook_link = facebook_link

    db.session.commit()

  except Exception:
    error = True
    db.session.rollback()
  finally:
    db.session.close()
    if error:
      flash('An error occurred. Artist ' + name + ' could not be updated.', 'error')
    else:
      flash('Artist ' + name + ' was successfully updated!', 'success')

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue = Venue.query.get(venue_id)
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  error = False
  try:
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']
    address = request.form['address']
    phone = request.form['phone']
    genres = VenueForm(request.form).genres.data
    facebook_link = request.form['facebook_link']

    venue = Venue.query.get(venue_id)
    venue.name = name
    venue.city = city
    venue.state = state
    venue.address = address
    venue.phone = phone
    venue.genres = genres
    venue.facebook_link = facebook_link

    db.session.commit()

  except Exception:
    error = True
    db.session.rollback()
  finally:
    db.session.close()
    if error:
      flash('An error occurred. Venue ' + name + ' could not be updated.', 'error')
    else:
      flash('Venue ' + name + ' was successfully updated!', 'success')

  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  error = False
  try:
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']
    phone = request.form['phone']
    genres = ArtistForm(request.form).genres.data
    facebook_link = request.form['facebook_link']

    artist = Artist(name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)
    db.session.add(artist)
    db.session.commit()

  except Exception:
    error = True
    db.session.rollback()
  finally:
    db.session.close()
    if error:
      flash('An error occurred. Artist ' + name + ' could not be listed.', 'error')
    else:
      flash('Artist ' + name + ' was successfully listed!', 'success')

  return render_template('pages/home.html')

@app.route('/artists/<artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
  response = {}
  try:
    Artist.query.filter_by(id=artist_id).delete()
    db.session.commit()
    response['success'] = True
  except Exception:
    db.session.rollback()
    response['success'] = False
    flash('An error occurred deleting a Artist!', 'error')
  finally:
    db.session.close()
    return jsonify(response)

#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  data = Show.query.all()

  for show in data:
    show.venue_name = show.venue.name
    show.artist_name = show.artist.name
    show.artist_image_link = show.artist.image_link
    show.start_time = format_datetime(str(show.start_time))

  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  error = False
  try:
    artist_id = request.form['artist_id']
    venue_id = request.form['venue_id']
    start_time = request.form['start_time']

    show = Show(artist_id=artist_id, venue_id=venue_id, start_time=start_time)
    db.session.add(show)
    db.session.commit()

  except Exception:
    error = True
    db.session.rollback()
  finally:
    db.session.close()
    if error:
      flash('An error occurred. Show could not be listed.', 'error')
    else:
      flash('Show was successfully listed!', 'success')

  return render_template('pages/home.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run(debug=DEBUG, use_reloader=False)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
