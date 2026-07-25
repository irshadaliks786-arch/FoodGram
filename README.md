🍔 FoodGram

Instagram + MyFitnessPal ka mix. Share your food photos, flex your nutrition, and let the world see what you're eating — calories, protein, carbs, and fat included.


✨ Features
📸 Upload food photos with captions
🔥 Auto nutrition detection — just type the food name and hit "Get Nutrition" to pull calories, protein, carbs, and fat from Open Food Facts (free, no API key needed)
🍽️ Feed — see everyone's posts, newest first
❤️ Like / Unlike posts
💬 Comment on posts
👤 Profile page — total posts and total calories flexed
🔐 Auth — signup, login, logout
🛠️ Admin panel — manage posts, likes, and comments
🎨 Clean, Instagram-style UI — pure CSS, no frameworks
🛠️ Tech Stack
Layer	Technology
Backend	Django 6.0 (Python)
Database	SQLite (dev)
Frontend	Django Templates + custom CSS
Image handling	Pillow
Nutrition data	Open Food Facts API
📁 Project Structure
foodgram/
├── templates/
│   ├── base.html                  # Navbar + global CSS
│   └── registration/login.html
├── posts/
│   ├── models.py                  # Post, Like, Comment
│   ├── views.py                   # feed, upload, like, comment, profile, nutrition search
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   └── templates/posts/
│       ├── feed.html
│       ├── upload.html
│       └── profile.html
├── users/
│   ├── views.py                   # signup
│   ├── urls.py
│   └── templates/users/signup.html
├── foodgram/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
🚀 Getting Started
1. Clone the repo
bash
git clone https://github.com/irshadaliks786-arch/FoodGram.git
cd FoodGram
2. Create a virtual environment
bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
3. Install dependencies
bash
pip install -r requirements.txt
4. Set up the database
bash
python manage.py migrate
python manage.py createsuperuser
5. Run the server
bash
python manage.py runserver
6. Open in your browser
App: http://127.0.0.1:8000/
Signup: http://127.0.0.1:8000/accounts/signup/
Admin: http://127.0.0.1:8000/admin/
🔥 How Nutrition Auto-Detection Works
Type a food name (e.g. "Chicken Biryani") on the upload page
Click Get Nutrition
The app queries the free Open Food Facts API and auto-fills calories, protein, carbs, and fat (per 100g)
Edit the values freely before posting — auto-fill is a starting point, not the final word

No API key required — it's a free, open database.

🗺️ Roadmap / Ideas
 Deploy to Render / Railway (free tier)
 Pagination for the feed
 Profile pictures and bios
 Post editing / deletion
 Serving-size adjustment for nutrition values
 Dark mode
📄 License

This project is open source and available under the MIT License.

🙌 Acknowledgements
Open Food Facts for free nutrition data
Built with Django
FoodGram is a Django-based social platform for sharing food photos along with nutrition details such as calories, protein, carbs, and fat. Users can sign up, log in, upload food posts, like and comment on posts, view profiles, and track total calories shared.
>>>>>>> 0cf4324f3cf2483790d9dc8d22d19232bc1ba9ee
