Project Overview
This is a Django web application for managing trainees and courses. The application allows users to:

View, add, update, and delete trainees
View, add, update, and delete courses
Navigate between trainees and courses using a homepage
Features
✅ List all trainees and courses
✅ Add new trainees and courses
✅ Update and delete trainees/courses
✅ Simple UI with navigation

Installation & Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/AmeraKhaled/Django_day1.git
cd Django_day1
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On Mac/Linux:
source myenv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Apply Migrations
bash
Copy
Edit
python manage.py migrate
5. Run the Development Server
bash
Copy
Edit
python manage.py runserver
Then open http://127.0.0.1:8000/ in your browser.

Project Structure
csharp
Copy
Edit
/ITIan/              # Main Django project folder
    ├── course_app/  # Course management app
    ├── trainee_app/ # Trainee management app
    ├── templates/   # HTML templates
    ├── static/      # CSS, JavaScript, images
    ├── manage.py    # Django command-line tool
