#!/usr/bin/env python3
"""
Setup script for RetailBot - AI-Powered Inventory Assistant

This script helps you set up the environment for the RetailBot project.
"""

import os
import shutil
import sys

def setup_environment():
    """Set up the environment for the project"""
    
    print("🤖 RetailBot Setup")
    print("=" * 50)
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file already exists")
    else:
        # Copy .env.example to .env
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            print("✅ Created .env file from .env.example")
            print("⚠️  Please edit .env file and add your actual credentials")
        else:
            print("❌ .env.example file not found")
            return False
    
    # Check required environment variables
    required_vars = ['GOOGLE_API_KEY', 'DB_PASSWORD']
    
    # Load .env file
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        missing_vars = []
        for var in required_vars:
            if not os.getenv(var) or os.getenv(var) == f'your_{var.lower()}_here':
                missing_vars.append(var)
        
        if missing_vars:
            print(f"❌ Please set the following environment variables in .env file:")
            for var in missing_vars:
                print(f"   - {var}")
            return False
        else:
            print("✅ All required environment variables are set")
            
    except ImportError:
        print("❌ python-dotenv not installed. Run: pip install python-dotenv")
        return False
    
    print("\n🎉 Setup complete! You can now run:")
    print("   streamlit run main.py")
    
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    try:
        import subprocess
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
            return True
        else:
            print(f"❌ Failed to install dependencies: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

if __name__ == "__main__":
    print("Starting RetailBot setup...\n")
    
    # Install dependencies first
    if install_dependencies():
        # Then setup environment
        if setup_environment():
            print("\n🚀 RetailBot is ready to use!")
        else:
            print("\n❌ Setup failed. Please check the error messages above.")
    else:
        print("\n❌ Failed to install dependencies. Please install manually.")
