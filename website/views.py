from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import  login_required, current_user
from .models import Note, Componente
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    '''if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')'''
    return render_template("home.html", user=current_user)

@views.route('/comprados')
@login_required
def bought():
    return render_template("bought.html", user=current_user)

@views.route('/comprar', methods=['GET', 'POST'])
@login_required
def to_buy():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cartao = request.form.get('precoCartao')
        pix = request.form.get('precoPix')
        estado = request.form.get('estado')
        if len(nome) < 1:
            flash('Part is too short', category='error')
        else:
            new_part = Componente(nome=nome, precoCartao=cartao, precoPix=pix, estado=estado, user_id=current_user.id)
            db.session.add(new_part)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("to_buy.html", user=current_user)

@views.route('/guest')
def guest_home():
    return render_template("guest.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})