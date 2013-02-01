from flask import request, flash, redirect, url_for, render_template
from braviapp import braviapp, db
from braviapp.forms import NewsCreateForm
from braviapp.models import News

@braviapp.errorhandler(404)
def not_found(error):
	flash('You tried access a page that not exists')
	return redirect(url_for('all')) 

@braviapp.route('/')
def all():
	#from news_model import News
	news = News.query.all()
	return render_template('news_list.html', news=news)

@braviapp.route('/create/', methods=['GET', 'POST'])
def create():
	form = NewsCreateForm(request.form)

	# make sure data are valid
	if form.validate_on_submit():

		news = News(form.title.data, form.text.data)
		# save on database
		db.session.add(news)
		db.session.commit()

		flash('The news has been created successfully')
		return redirect(url_for('all'))
	return render_template('news_create.html', form=form)
