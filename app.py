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
                <meta name="description" content="View and download the PDF file {pdf_filename} with ease on our platform jpdftest.">
                <meta property="og:title" content="{pdf_filename}">
                <meta property="og:description" content="View and download the PDF file {pdf_filename} easily on our platform.">
                <meta property="og:url" content="https://publish-pdf.vercel.app/">
                <meta property="og:type" content="website">
                <meta property="og:image" content="https://publish-pdf.vercel.app/static/images/your-image.jpg">
                <meta name="twitter:card" content="summary_large_image">
                <meta name="twitter:title" content="{pdf_filename}">
                <meta name="twitter:description" content="View and download the PDF file {pdf_filename} with ease.">
                <meta name="twitter:image" content="https://publish-pdf.vercel.app/static/images/your-image.jpg">
                <link rel="icon" href="/static/images/favicon.ico" type="image/x-icon">
                <link rel="canonical" href="https://publish-pdf.vercel.app/" />
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
                    .download-button {{
                        display: inline-block;
                        padding: 10px 20px;
                        margin-top: 20px;
                        background-color: #007bff;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                    }}
                </style>
            </head>
            <body>
                <object data="/static/pdf/{pdf_filename}" type="application/pdf" aria-label="PDF Viewer">
                    <p>Your browser does not support PDF viewing. <a href="/static/pdf/{pdf_filename}">Download the PDF</a>.</p>
                </object>
                <a href="/static/pdf/{pdf_filename}" class="download-button">Download PDF</a>
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
