# Drawing App with Flask

A simple web-based drawing application created with Flask, HTML, CSS, and JavaScript. This app allows users to draw on a canvas, change colors, clear the canvas, and save their creations as PNG images.

## Features
- 🎨 Draw on a canvas using the mouse
- 🌈 Select from different brush colors (Black, Red, Blue, Yellow, Green)
- 🧹 Clear the canvas with ease
- 📥 Download your drawing as a PNG image

## Installation & Setup

### Prerequisites
Ensure you have Python 3 installed on your machine.

### Steps

1. **Clone the Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/StealthBuilder/drawing-app-flask.git
   cd drawing-app-flask
   ```

2. **Install Dependencies**  
   Create a virtual environment and install the necessary packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install flask pillow
   ```

3. **Run the Application**  
   Start the Flask server:
   ```bash
   python app.py
   ```
   The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

```
.
├── static/
│   ├── style.css  # Styles for the UI
│   ├── script.js  # JavaScript logic
│   └── drawing.png  # Saved drawings (generated dynamically)
├── templates/
│   └── index.html  # Frontend UI
├── app.py  # Flask backend
├── README.md  # Project documentation
```

## API Endpoints

| Route       | Method | Description               |
|-------------|--------|---------------------------|
| `/`         | GET    | Loads the drawing page    |
| `/save`     | POST   | Saves and allows you to download the drawing |

## Usage

1. Open the web application in your browser.
2. Use the mouse to draw on the canvas.
3. Click the color buttons to choose your preferred brush color.
4. Click **Clear** to reset the canvas.
5. Click **Download** to save your artwork as a PNG file.

💡 Built with Flask & Love ❤️
