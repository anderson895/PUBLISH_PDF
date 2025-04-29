import os
import webbrowser
from flask import Flask, send_from_directory, abort, Response

app = Flask(__name__)

# Relative path to the PDF file from the location of app.py
pdf_dir = os.path.join(os.path.dirname(__file__), 'static', 'pdf')
pdf_filename = 'sequence-practice-problems.pdf'

# Route to serve the PDF and dynamically set the title
@app.route('/')
def open_pdf():
    pdf_path = os.path.join(pdf_dir, pdf_filename)
    if not os.path.exists(pdf_path):
        # If the file doesn't exist, return a 404 error
        abort(404)
    
    # HTML content with dynamic title, and full-screen PDF display
    html_content = f'''
        <html>
            <head>
                <title>{pdf_filename}</title>
                <meta name="google-site-verification" content="mLf59s4voF-nhDphRX215iJRKv9MwssnZ2_78qtUxJA" />
                <style>
                    html, body {{
                        height: 100%;
                        margin: 0;
                        padding: 0;
                        overflow: hidden;
                    }}
                    object {{
                        width: 100%;
                        height: 100%;
                    }}
                </style>
            </head>
            <body>
                <object data="/static/pdf/{pdf_filename}" type="application/pdf">
                    <p>Your browser does not support PDF viewing. <a href="/static/pdf/{pdf_filename}">Download the PDF</a>.</p>
                </object>
            </body>
        </html>
    '''

    # Return the HTML response with the title and embedded PDF
    return Response(html_content, content_type='text/html')

if __name__ == '__main__':
    # Automatically open the PDF URL when the app starts
    webbrowser.open('http://127.0.0.1:5000/')
    
    # Run the Flask app
    app.run(debug=True)
