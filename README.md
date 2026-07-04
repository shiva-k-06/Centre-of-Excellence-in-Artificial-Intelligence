# CAIM + Bodhi Shala Website

This repository contains the Django-based website for the **Centre of Excellence in AI, NIT Trichy**, which includes:

- **Landing page** — introduces the Centre of Excellence in AI
- **CAIM** (`/caim/`) — the TATA Centre for AI & ML full website (People, Research, Publications, Events, Projects, Contact)
- **Bodhi Shala** (`/bodhishala/`) — a mini-site under the same umbrella (Research, People, Facilities, Publications, Contact)

---

## Tech Stack

- **Backend:** Django 6.0.5 (Python)
- **Database:** SQLite 
- **Frontend:** Bootstrap 5.3, Open Sans font
- **Brand colors:** Navy `#012951`, Teal `#007b6e`

---

## Setup Instructions (Local Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/shiva-k-06/Centre-of-Excellence-in-Artificial-Intelligence.git
   cd Centre-of-Excellence-in-Artificial-Intelligence
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. Visit `http://127.0.0.1:8000/` in your browser.

---

## ⚠️ Important: Admin Login (Read Before Anything Else)

This repository **includes the database file** (`db.sqlite3`) so that the real content already added — Events and Bodhi Shala Publications — comes with the code instead of starting empty.

Because of this, a superuser account already exists in the database:

- **Username:** `shivv06`

**Before doing anything else, please:**

1. Create your own superuser account:
   ```bash
   python manage.py createsuperuser
   ```
2. Log in to `/admin/`  with your **new** account.
3. Once confirmed working, **delete the `shivv06` account** from the admin panel (Users section).

Do not rely on the `shivv06` account for anything beyond initial setup — it should be removed before this site is used for real / handed off further.

---

## Admin Panel Guide

The admin panel header is labeled **"TATA CAIM — Admin Panel"**. Log in at `/admin/` using your superuser credentials.

The following content types can be managed directly from the admin panel:

| Section | What it controls |
|---|---|
| **Events** | Upcoming/past events shown on `/caim/events/`. Includes an expandable "Event Statistics" panel (registrations, attendees, teams shortlisted, winning teams). |
| **Publications** | CAIM publications shown on `/caim/publications/` (filterable by year/type). |
| **Bodhi Shala Publications** | Separate table, shown on `/bodhishala/publications/`. |
| **Projects** | Student project submissions on `/caim/projects/`. Includes a bulk **"approve_projects"** action, and a status field (pending / approved / rejected). |
| **Contact Messages** | Messages submitted via `/caim/contact/`. |
| **Bodhi Shala Contact Messages** | Messages submitted via `/bodhishala/contact/`. Kept as a separate table from CAIM contact messages. |

### To add / edit / delete any of the above:
1. Go to `/admin/` and log in.
2. Click the relevant section (e.g. "Events").
3. **Add:** click "Add" in the top right, fill in the fields, click "Save".
4. **Edit:** click on any existing entry, make changes, click "Save".
5. **Delete:** either open the entry and click "Delete" at the bottom, or select the checkbox next to one/multiple entries on the list page, choose "Delete selected" from the action dropdown, and confirm.

### ⚠️ Important exception — the People sections are NOT admin-managed

The People listings (Governance, Advisory, Administrative, and Domain Innovation Heads committees) shown on:
- `/caim/people/`
- `/bodhishala/people/`

are **hardcoded directly into the HTML template files** — they are not stored in the database and will not appear anywhere in the admin panel.

To add, edit, or remove a person, you need to directly edit the relevant template file in a code editor:
- `people.html` — for CAIM People
- `bodhishala_people.html` — for Bodhi Shala People

If ongoing editing without touching code is important going forward, this would be a good candidate to convert into a proper Django model + admin section in a future update.

---

## Project Structure (Brief Overview)

```
Centre-of-Excellence-in-Artificial-Intelligence/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── core/
│   ├── settings.py
│   ├── urls.py
├── website/
│   ├── models.py         # ContactMessage, Event, Project, Publication,
│   │                      # BodhiShalaPublication, BodhiShalaContactMessage
│   ├── views.py
│   ├── admin.py           # Custom admin classes for all models
├── templates/
│   ├── people.html
│   ├── bodhishala_people.html
│   └── ... (other page templates)
├── static/
```

### URL Map

```
/                        → Landing page
/caim/                   → CAIM home
/caim/people/
/caim/research/
/caim/facilities/        → placeholder (content moved to Bodhi Shala)
/caim/publications/
/caim/events/
/caim/projects/
/caim/projects/submit/
/caim/register/
/caim/login/
/caim/logout/
/caim/contact/
/bodhishala/
/bodhishala/research/
/bodhishala/people/
/bodhishala/facilities/
/bodhishala/publications/
/bodhishala/contact/
```

---

## Deployment Notes 

The following settings in `settings.py` are currently configured for **local development** and must be changed before going live on the actual domain:

| Setting | Current (dev) | Change to (production) |
|---|---|---|
| `SECRET_KEY` | Hardcoded in `settings.py` | Move to an environment variable |
| `DEBUG` | `True` | `False` |
| `ALLOWED_HOSTS` | `['*']` | `['caim.nitt.edu']` (or actual domain) |
| Database | SQLite (`db.sqlite3`) | Switch to MySQL |
| Superuser | `shivv06` (dev/test account) | Create a new one, e.g. with `coeai@nitt.edu`, then delete `shivv06` |

Additional notes:
- `TIME_ZONE` is set to `Asia/Kolkata`.
- Static files are served from `STATIC_URL = 'static/'`, with `STATICFILES_DIRS` pointing to the project's `static/` folder — confirm static file collection (`collectstatic`) is run as part of deployment if using a production web server.
- Since `db.sqlite3` is included in this repo, it already contains real data (see below). If migrating to MySQL, this data will need to be exported/re-entered — it will not carry over automatically.

---

## Data Currently in the Database

- **Events:** 1 real event — "AI For All — One Day Ideathon" (Feb 2026), with registration/attendee/team stats already filled in.
- **Bodhi Shala Publications:** 2 real papers already added.
- **CAIM Publications:** empty — real publication data is still pending from the mentor.
- **Projects:** empty — no real student submissions yet.

All test/dummy accounts and test entries used during development have been removed prior to this handover.

---
