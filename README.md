[README.md](https://github.com/user-attachments/files/30515251/README.md)
# 🧩 Sudoku Solver

A simple web-based Sudoku solver built with **Flask**. Enter a puzzle into a 9×9 grid, and the app validates it and solves it using a backtracking algorithm — all in your browser.

![Sudoku Solver](static/logo.png)

## Features

- 🧩 **Interactive 9×9 grid** — type numbers directly into the board
- ✅ **Board validation** — checks that the entered puzzle follows Sudoku rules before attempting to solve
- 🧠 **Backtracking solver** — computes a valid solution when one exists
- 📜 **Solve history** — keeps a record of previously solved boards during the current server session
- 🔄 **Clear button** — resets the grid to start over
- ✨ **Animated intro screen** — a short loading/splash screen before landing on the solver

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Jinja2 templates

## Project Structure

```
.
├── app.py              # Flask app: routes, validation, and solving logic
├── templates/
│   ├── intro.html      # Animated splash screen (auto-redirects to /home)
│   ├── index.html      # Main Sudoku grid / solver page
│   └── history.html    # List of previously solved boards
├── static/
│   ├── style.css        # Stylesheet
│   └── logo.png          # App logo
└── settings.json        # Editor/Live Server config (not used by the app itself)
```

## Getting Started

### Prerequisites

- Python 3.7+
- Flask

### Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install flask
```

### Running the app

```bash
python app.py
```

Then open your browser to:

```
http://127.0.0.1:5000/
```

You'll see a brief animated intro screen before being redirected to the solver at `/home`.

## Usage

1. Enter known digits into the grid (leave cells blank for unknowns).
2. Click **Solve** to validate and solve the puzzle.
3. If the puzzle is invalid or has no solution, an error message is shown.
4. Click **History** to view previously solved boards from this session.
5. Click **Clear** to reset the grid.

## Routes

| Route      | Method    | Description                                  |
|------------|-----------|-----------------------------------------------|
| `/`        | GET       | Intro/splash screen, redirects to `/home`     |
| `/home`    | GET, POST | Main grid — displays and solves the puzzle    |
| `/history` | GET       | Shows previously solved boards                |
| `/clear`   | GET       | Resets the grid                                |

## Notes

- Solve history is stored in memory and will reset whenever the server restarts.
- The app currently runs with `debug=True`; disable this before deploying to production.

## License

This project is open source and available under the [MIT License](LICENSE).
