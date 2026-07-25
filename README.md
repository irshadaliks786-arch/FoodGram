<<<<<<< HEAD
# FoodGram 🍔

Instagram + MyFitnessPal ka mix — food photos share karo, nutrition (calories/protein/carbs/fat) flex karo.

## Features (Sab Ready Hai)

- ✅ Signup / Login / Logout
- ✅ Feed — sabke posts, newest first
- ✅ Upload — photo + caption + nutrition (calories/protein/carbs/fat)
- ✅ Like / Unlike (toggle)
- ✅ Comments
- ✅ Profile — total posts + total calories flexed
- ✅ Admin panel — Posts/Likes/Comments manage karne ke liye
- ✅ Clean Instagram-style UI (pure CSS, no framework)

## Folder Structure

```
foodgram/
├── templates/
│   ├── base.html                  ← navbar + saara CSS
│   └── registration/login.html
├── posts/
│   ├── models.py, views.py, forms.py, admin.py, urls.py
│   └── templates/posts/
│       ├── feed.html
│       ├── upload.html
│       └── profile.html
├── users/
│   ├── views.py (signup), urls.py
│   └── templates/users/signup.html
├── foodgram/settings.py, urls.py
├── manage.py
└── requirements.txt
```

## How to Run

1. Extract the zip and go into the project folder:
   ```
   cd foodgram
   ```

2. (Recommended) Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      (Windows)
   source venv/bin/activate   (Mac/Linux)
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create the database and an admin account:
   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```
   (set your own username/password when asked)

5. Run the server:
   ```
   python manage.py runserver
   ```

6. Open in browser:
   - Website: http://127.0.0.1:8000/
   - Signup: http://127.0.0.1:8000/accounts/signup/
   - Admin panel: http://127.0.0.1:8000/admin/

## Notes

- Uploaded photos are saved locally under `media/` (fine for development).
  For production, connect Cloudinary or similar for image storage.
- `db.sqlite3` is not included in this zip — it will be created fresh
  by the `migrate` command above.
- This uses Django's built-in `User` model — no custom user model needed.

## Next Steps (Optional Ideas)

- Connect Open Food Facts API to auto-fill nutrition by food name
- Deploy free on Render/Railway (PostgreSQL free tier)
- Add pagination to the feed for many posts
- Add profile pictures / bio
=======
# FoodGram
FoodGram is a Django-based social platform for sharing food photos along with nutrition details such as calories, protein, carbs, and fat. Users can sign up, log in, upload food posts, like and comment on posts, view profiles, and track total calories shared.
>>>>>>> 0cf4324f3cf2483790d9dc8d22d19232bc1ba9ee
