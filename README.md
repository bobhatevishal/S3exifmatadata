# 🧼 EXIF Cleaner + AWS S3 Uploader

A simple Flask-based web application that allows users to upload images, removes sensitive **EXIF metadata** (like GPS location, device info), and securely uploads the cleaned images to an **AWS S3 bucket**.

---

## 🚀 Features

- 📷 Upload image files from the browser
- 🧽 Automatically removes EXIF metadata using `Pillow` and `piexif`
- ☁️ Uploads sanitized image files to AWS S3 using `boto3`
- 🖥️ Clean and responsive web UI with modern styling
- 🔒 Enhances privacy and security by removing hidden metadata

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (basic form UI)
- **Backend**: Python, Flask
- **Image Processing**: Pillow, piexif
- **Cloud Storage**: Amazon S3 (via boto3)

---

## 📸 Why EXIF Cleaning?

Most modern cameras and smartphones embed sensitive metadata (EXIF) inside image files, including:
- GPS location
- Device make/model
- Timestamp

This app helps protect user privacy by stripping that data before storing or sharing.

---

## 🧪 How It Works

1. User uploads an image through the web form
2. The image is saved temporarily on the server
3. All EXIF metadata is stripped out
4. Clean image is uploaded to the specified S3 bucket
5. Temporary files are deleted from the server

---

## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/bobhatevishal/S3exifmatadata
   cd S3exifmatadata

