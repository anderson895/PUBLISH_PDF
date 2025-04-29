import os
import webbrowser
from flask import Flask, send_from_directory

app = Flask(__name__)

# Relative path to the PDF file from the location of app.py
pdf_dir = os.path.join(os.path.dirname(__file__), 'static', 'pdf')
pdf_filename = 'sequence-practice-problems.pdf'

# Route to serve the PDF
@app.route('/')
def open_pdf():
    return send_from_directory(pdf_dir, pdf_filename)

if __name__ == '__main__':
    # Automatically open the PDF when the app starts using relative path
    webbrowser.open(f'file:///{os.path.join(pdf_dir, pdf_filename)}')
    
    # Run the Flask app
    app.run(debug=True)
