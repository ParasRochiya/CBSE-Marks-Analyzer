#!/usr/bin/env python3
"""
Simple run script for the Flask grade processing app
"""
import os
from app import app

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    print("Starting Grade Processing Web App...")
    print("Access the application at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
