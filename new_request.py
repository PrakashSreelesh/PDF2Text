from flask import Flask, request
from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage
import main

app = Flask(__name__)


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        pdf_file1 = f.filename
        print(pdf_file1)
        text_file = main.pdffile_convert(pdf_file1)
        with open(text_file, "r") as f:
            content = f.read()
            return(content)


if __name__ == '__main__':
    app.run(debug=True)

