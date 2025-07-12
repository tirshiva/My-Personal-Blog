# Personal Blog Application

A simple, elegant personal blog built with Flask that allows you to write and publish articles. The blog features both a guest section for readers and an admin section for content management.

https://roadmap.sh/projects/personal-blog

## Features

### Guest Section
- **Home Page**: Displays a list of all published articles
- **Article Page**: Shows individual articles with full content and publication date

### Admin Section
- **Dashboard**: Manage all articles with options to view, edit, and delete
- **Add Article**: Create new articles with title and content
- **Edit Article**: Modify existing articles
- **Delete Article**: Remove articles from the blog
- **Authentication**: Secure admin access with username/password

## Technical Details

- **Backend**: Python Flask
- **Storage**: File-based storage using JSON format
- **Frontend**: HTML/CSS with modern, responsive design
- **Authentication**: Session-based admin authentication
- **Templates**: Jinja2 templating engine

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the blog**:
   - Open your web browser and go to `http://localhost:5000`
   - The blog will be accessible at the home page

## Usage

### For Readers (Guest Section)
1. Visit the home page to see all published articles
2. Click on any article title to read the full content
3. Navigate back to home using the navigation menu

### For Administrators
1. **Login**: Click "Admin Login" in the navigation and use:
   - Username: `admin`
   - Password: `password123`

2. **Dashboard**: After login, you'll see the admin dashboard with all articles

3. **Create New Article**:
   - Click the "+ New Article" button
   - Fill in the title and content
   - Click "Create Article"

4. **Edit Article**:
   - Click the "Edit" button next to any article
   - Modify the title and/or content
   - Click "Update Article"

5. **Delete Article**:
   - Click the "Delete" button next to any article
   - Confirm the deletion

6. **Logout**: Click "Logout" in the navigation when done

## File Structure

```
Blog App/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── articles/             # Directory for storing article JSON files
└── templates/            # HTML templates
    ├── base.html         # Base template with styling
    ├── home.html         # Home page template
    ├── article.html      # Individual article template
    └── admin/            # Admin templates
        ├── login.html    # Admin login page
        ├── dashboard.html # Admin dashboard
        └── article_form.html # Article creation/editing form
```

## Storage Format

Articles are stored as JSON files in the `articles/` directory. Each article file contains:
```json
{
  "id": "unique-article-id",
  "title": "Article Title",
  "content": "Article content with HTML support",
  "date": "2024-01-01 12:00:00"
}
```

## Customization

### Changing Admin Credentials
Edit the `ADMIN_USERNAME` and `ADMIN_PASSWORD` variables in `app.py`:
```python
ADMIN_USERNAME = 'your-username'
ADMIN_PASSWORD = 'your-secure-password'
```

### Styling
The blog uses custom CSS embedded in the `base.html` template. You can modify the styles to match your preferences.

### Content Formatting
Articles support basic HTML tags for formatting:
- `<strong>` for bold text
- `<em>` for italic text
- `<p>` for paragraphs
- `<br>` for line breaks
- `<h1>`, `<h2>`, etc. for headings

## Security Notes

- Change the default admin credentials before deploying
- Update the `secret_key` in `app.py` for production use
- Consider using environment variables for sensitive data
- The current authentication is basic; consider implementing more robust authentication for production

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py`:
   ```python
   app.run(debug=True, port=5001)
   ```

2. **Permission errors**: Ensure you have write permissions in the project directory

3. **Template errors**: Make sure all template files are in the correct directories

### Getting Help

If you encounter any issues:
1. Check that all dependencies are installed correctly
2. Verify that all template files are present
3. Check the console output for error messages
4. Ensure the `articles/` directory is created automatically

## Future Enhancements

Potential improvements for the blog:
- Rich text editor for article creation
- Image upload support
- Categories and tags
- Search functionality
- Comments system
- RSS feed
- Database storage (SQLite/PostgreSQL)
- User registration and multiple authors
- Social media sharing
- SEO optimization

## License

This project is open source and available under the MIT License. 