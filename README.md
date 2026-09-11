# Atikes Flask - Simple Manual Editing Structure

## Structure

```text
templates/
├── base.html
├── navbar.html
├── footer.html
├── home.html
├── services.html
├── solutions.html
├── success-stories.html
├── iam-health-check.html
├── partners.html
├── about.html
├── contact.html
├── consultation.html
└── 404.html

static/
├── css/
│   └── style.css
├── js/
│   └── main.js
└── images/
```

## How the application works

```text
Browser
  ↓
app.py
  ↓
individual page template
  ↓
base.html
  ├── navbar.html
  └── footer.html
  ↓
style.css + main.js
```

## Manual editing

- Home UI → `templates/home.html`
- Services UI → `templates/services.html`
- Success Stories UI → `templates/success-stories.html`
- IAM Health Check UI → `templates/iam-health-check.html`
- Contact UI → `templates/contact.html`
- Book Consultation UI → `templates/consultation.html`
- Navbar → `templates/navbar.html`
- Footer → `templates/footer.html`
- All CSS → `static/css/style.css`
- All JS → `static/js/main.js`
- Images → `static/images/`

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

## Notes

The contact and consultation forms currently show a success message but do not save to a database or send email yet. Add that backend logic later in `app.py`.
