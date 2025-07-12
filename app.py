from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
import json
import os
from datetime import datetime
import uuid
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Configuration
ARTICLES_DIR = 'articles'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password123'

# Create articles directory if it doesn't exist
if not os.path.exists(ARTICLES_DIR):
    os.makedirs(ARTICLES_DIR)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

def load_articles():
    """Load all articles from the articles directory"""
    articles = []
    if os.path.exists(ARTICLES_DIR):
        for filename in os.listdir(ARTICLES_DIR):
            if filename.endswith('.json'):
                with open(os.path.join(ARTICLES_DIR, filename), 'r', encoding='utf-8') as f:
                    article = json.load(f)
                    articles.append(article)
    # Sort articles by date (newest first)
    articles.sort(key=lambda x: x['date'], reverse=True)
    return articles

def save_article(article_data):
    """Save an article to a JSON file"""
    article_id = article_data.get('id', str(uuid.uuid4()))
    filename = f"{article_id}.json"
    filepath = os.path.join(ARTICLES_DIR, filename)
    
    article_data['id'] = article_id
    if 'date' not in article_data:
        article_data['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(article_data, f, indent=2, ensure_ascii=False)
    
    return article_id

def get_article(article_id):
    """Get a specific article by ID"""
    filename = f"{article_id}.json"
    filepath = os.path.join(ARTICLES_DIR, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def delete_article(article_id):
    """Delete an article by ID"""
    filename = f"{article_id}.json"
    filepath = os.path.join(ARTICLES_DIR, filename)
    
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    return False

# Guest Section Routes
@app.route('/')
def home():
    """Home page - displays list of published articles"""
    articles = load_articles()
    return render_template('home.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    """Article page - displays a specific article"""
    article = get_article(article_id)
    if article is None:
        abort(404)
    return render_template('article.html', article=article)

# Admin Section Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('Successfully logged in!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    flash('Successfully logged out!', 'success')
    return redirect(url_for('home'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """Admin dashboard - displays list of articles with management options"""
    articles = load_articles()
    return render_template('admin/dashboard.html', articles=articles)

@app.route('/admin/article/new', methods=['GET', 'POST'])
@login_required
def admin_new_article():
    """Add new article page"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if title and content:
            article_data = {
                'title': title,
                'content': content,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            save_article(article_data)
            flash('Article created successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Title and content are required!', 'error')
    
    return render_template('admin/article_form.html', article=None)

@app.route('/admin/article/<article_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_article(article_id):
    """Edit article page"""
    article = get_article(article_id)
    if article is None:
        abort(404)
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if title and content:
            article['title'] = title
            article['content'] = content
            save_article(article)
            flash('Article updated successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Title and content are required!', 'error')
    
    return render_template('admin/article_form.html', article=article)

@app.route('/admin/article/<article_id>/delete', methods=['POST'])
@login_required
def admin_delete_article(article_id):
    """Delete article"""
    if delete_article(article_id):
        flash('Article deleted successfully!', 'success')
    else:
        flash('Article not found!', 'error')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
