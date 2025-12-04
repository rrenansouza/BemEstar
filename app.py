import os
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'bem-estar-secret-key-2024')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'bemestar2024'

class ContactSubmission(db.Model):
    __tablename__ = 'contact_submissions'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    mensagem = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    lido = db.Column(db.Boolean, default=False)

class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    vaga = db.Column(db.String(100), nullable=False)
    curriculo_filename = db.Column(db.String(300))
    aceita_freelance = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    lido = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/api/contato', methods=['POST'])
def submit_contact():
    try:
        data = request.json
        submission = ContactSubmission(
            nome=data.get('nome'),
            telefone=data.get('telefone'),
            email=data.get('email'),
            mensagem=data.get('mensagem', '')
        )
        db.session.add(submission)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Mensagem enviada com sucesso!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/trabalhe-conosco', methods=['POST'])
def submit_job_application():
    try:
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        vaga = request.form.get('vaga')
        aceita_freelance = request.form.get('aceita_freelance', 'nao') == 'sim'
        
        curriculo_filename = None
        if 'curriculo' in request.files:
            file = request.files['curriculo']
            if file and file.filename:
                filename = secure_filename(f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                curriculo_filename = filename
        
        application = JobApplication(
            nome=nome,
            telefone=telefone,
            email=email,
            vaga=vaga,
            curriculo_filename=curriculo_filename,
            aceita_freelance=aceita_freelance
        )
        db.session.add(application)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Candidatura enviada com sucesso!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/admin')
def admin_login():
    if session.get('admin_logged_in'):
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        session['admin_logged_in'] = True
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html', error='Usuário ou senha incorretos')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    contacts = ContactSubmission.query.order_by(ContactSubmission.created_at.desc()).all()
    applications = JobApplication.query.order_by(JobApplication.created_at.desc()).all()
    return render_template('admin_dashboard.html', contacts=contacts, applications=applications)

@app.route('/admin/contact/<int:id>/mark-read', methods=['POST'])
@login_required
def mark_contact_read(id):
    contact = ContactSubmission.query.get_or_404(id)
    contact.lido = True
    db.session.commit()
    return jsonify({'success': True})

@app.route('/admin/application/<int:id>/mark-read', methods=['POST'])
@login_required
def mark_application_read(id):
    application = JobApplication.query.get_or_404(id)
    application.lido = True
    db.session.commit()
    return jsonify({'success': True})

@app.route('/admin/download/<filename>')
@login_required
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/admin/contact/<int:id>/delete', methods=['POST'])
@login_required
def delete_contact(id):
    contact = ContactSubmission.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/admin/application/<int:id>/delete', methods=['POST'])
@login_required
def delete_application(id):
    application = JobApplication.query.get_or_404(id)
    if application.curriculo_filename:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], application.curriculo_filename))
        except:
            pass
    db.session.delete(application)
    db.session.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
