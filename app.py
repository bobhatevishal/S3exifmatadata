# To fix ModuleNotFoundError: No module named 'flask'
# Run this command in your terminal or PowerShell:
# pip install flask boto3 pillow piexif


from flask import Flask, request, render_template
import boto3
from PIL import Image
import piexif
from werkzeug.utils import secure_filename
import os
from tempfile import NamedTemporaryFile

app = Flask(__name__)
BUCKET_NAME = "kavi1308"

def remove_exif(input_path):
    """Remove EXIF metadata from the image."""
    img = Image.open(input_path)
    data = list(img.getdata())
    img_no_exif = Image.new(img.mode, img.size)
    img_no_exif.putdata(data)

    temp_file = NamedTemporaryFile(delete=False, suffix='.jpg')
    img_no_exif.save(temp_file.name)
    return temp_file.name

def upload_to_s3(file_path, key):
    """Upload cleaned image to S3 bucket."""
    s3 = boto3.client('s3')
    s3.upload_file(file_path, BUCKET_NAME, key)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        file = request.files.get('image')
        if not file:
            message = "No file uploaded."
        else:
            filename = secure_filename(file.filename)
            raw_path = os.path.join('temp_' + filename)
            file.save(raw_path)

            try:
                cleaned_path = remove_exif(raw_path)
                upload_to_s3(cleaned_path, filename)

                os.remove(raw_path)
                os.remove(cleaned_path)

                message = f"✅ {filename} uploaded to S3 (EXIF removed)."
            except Exception as e:
                message = f"❌ Error: {str(e)}"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

