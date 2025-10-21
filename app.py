"""
Portfolio Website Backend
Author: Umair Khan
Description: Flask backend for personal portfolio website with contact form handling
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Email configuration (you can use environment variables)
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', '587'))
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS', 'your-email@gmail.com')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', 'your-app-password')

class ContactFormHandler:
    """Handle contact form submissions and email sending"""
    
    def __init__(self):
        self.smtp_server = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.email_address = EMAIL_ADDRESS
        self.email_password = EMAIL_PASSWORD
    
    def validate_form_data(self, data):
        """Validate contact form data"""
        errors = []
        
        # Required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field) or not data.get(field).strip():
                errors.append(f"{field.capitalize()} is required")
        
        # Email validation
        email = data.get('email', '')
        if email and not self.is_valid_email(email):
            errors.append("Please enter a valid email address")
        
        # Message length validation
        message = data.get('message', '')
        if len(message) > 1000:
            errors.append("Message is too long (maximum 1000 characters)")
        
        return errors
    
    def is_valid_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def send_email(self, form_data):
        """Send email notification"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = self.email_address
            msg['Subject'] = f"Portfolio Contact: {form_data['subject']}"
            
            # Email body
            body = f"""
            New contact form submission from your portfolio website:
            
            Name: {form_data['name']}
            Email: {form_data['email']}
            Subject: {form_data['subject']}
            
            Message:
            {form_data['message']}
            
            Submitted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_address, self.email_password)
            text = msg.as_string()
            server.sendmail(self.email_address, self.email_address, text)
            server.quit()
            
            return True, "Email sent successfully"
            
        except Exception as e:
            return False, f"Failed to send email: {str(e)}"

# Initialize contact form handler
contact_handler = ContactFormHandler()

@app.route('/')
def index():
    """Serve the main portfolio page"""
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        # Get form data
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'No data received'
            }), 400
        
        # Validate form data
        errors = contact_handler.validate_form_data(data)
        if errors:
            return jsonify({
                'success': False,
                'message': 'Validation failed',
                'errors': errors
            }), 400
        
        # Send email
        success, message = contact_handler.send_email(data)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Message sent successfully! I\'ll get back to you soon.'
            })
        else:
            return jsonify({
                'success': False,
                'message': message
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Portfolio Backend'
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'message': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'message': 'Internal server error'
    }), 500

if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=5000)
