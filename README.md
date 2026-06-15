# Galaxy Boys Hostel - Web Application

Welcome to the **Galaxy Boys Hostel** repository. This is a modern, beautifully designed web application built with a hybrid approach using Python (Flask) and Frozen-Flask for static deployment to GitHub Pages.

## 🚀 Technologies Used
*   **Backend:** Python, Flask
*   **Static Generation:** Frozen-Flask
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Design System:** Calm & Professional Palette (Midnight Blue, Royal Purple, Gold)

## 📁 Project Structure
```text
.
├── app.py               # Main Flask application file
├── freeze.py            # Script to generate static files for deployment
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
│   └── index.html       # The main Home Page
└── static/              # Static assets
    ├── css/             # Stylesheets
    ├── js/              # Interactive scripts
    └── images/          # Logo, hero backgrounds, and assets
```

## 🛠️ Local Development Setup

To run the project locally and make changes:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HaronKhalid/Hostel-Managment-System.git
   cd Hostel-Managment-System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask development server:**
   ```bash
   python app.py
   ```
   *Open your browser and navigate to `http://127.0.0.1:5000` to see the live site.*

## 🚀 Deployment (GitHub Pages)

This project uses **Frozen-Flask** to convert the dynamic Flask application into a static website that can be hosted for free on GitHub Pages.

To update the live website:

1. **Freeze the application:**
   ```bash
   python freeze.py
   ```
   *This creates a `build/` directory containing all static files.*

2. **Push source code to main:**
   ```bash
   git add .
   git commit -m "Update source code"
   git push origin main
   ```

3. **Deploy the `build` directory to the `gh-pages` branch:**
   ```bash
   cd build
   git init
   git checkout -b gh-pages
   git add .
   git commit -m "Deploy to GitHub Pages"
   # Replace <your-repo-url> with your remote URL
   git push -f <your-repo-url> gh-pages
   ```

Once pushed, ensure that GitHub Pages is enabled in your repository settings and set to deploy from the `gh-pages` branch.