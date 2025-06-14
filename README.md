🔐 Verification Backend API
This is the backend API for the Verification System, built with Django and Django REST Framework. It provides endpoints for managing user registration, OTP/email verification, document uploads, and approval workflows.

Ideal for integrating with mobile apps, web clients, or admin dashboards that need secure identity verification flows.

📌 Features
✅ User Registration & Login

✉️ Email Verification using OTP

📄 Document Upload for manual review

👨‍💼 Admin Approval Dashboard (via Django Admin)

🛡 Token-Based Authentication (JWT or DRF token auth)

📊 Verification Status Tracking (Pending, Verified, Rejected)

🔍 RESTful, scalable API design

🛠 Tech Stack
Framework: Django 4.x

API: Django REST Framework (DRF)

Database: PostgreSQL / SQLite (dev)

Auth: JWT (via djangorestframework-simplejwt) or TokenAuth

Email: SMTP or SendGrid (for OTP)

Storage: Local or Cloud (e.g., AWS S3, Cloudinary for documents)

🚀 Getting Started
Prerequisites
Python 3.8+

pip

PostgreSQL (optional for production)

Virtual environment (recommended)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/reginaldtadiwa/verification-backend.git
cd verification-backend
