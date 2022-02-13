
from flask import Blueprint, render_template, redirect, url_for
from application import db
from application.models import Owner
from application.owners.forms import AddOwnerForm


owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddOwnerForm()

    if form.validate_on_submit():
        owner_name = form.name.data
        puppy_id = form.id.data

        owner = Owner(owner_name, puppy_id)
        db.session.add(owner)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add_owner.html', form=form)