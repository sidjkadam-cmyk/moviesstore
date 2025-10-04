#!/usr/bin/env python3
"""
Deployment script for PythonAnywhere
This script helps prepare your Django project for PythonAnywhere deployment
"""

import os
import shutil
import subprocess
import sys

def create_deployment_package():
    """Create a clean deployment package"""
    print("🚀 Creating deployment package for PythonAnywhere...")
    
    # Create deployment directory
    deploy_dir = "moviesstore_deployment"
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)
    
    # Copy the moviesstore directory
    shutil.copytree("moviesstore", os.path.join(deploy_dir, "moviesstore"))
    
    # Copy requirements file
    shutil.copy("requirements_production.txt", os.path.join(deploy_dir, "requirements.txt"))
    
    # Copy production settings
    shutil.copy("moviesstore/moviesstore/settings_production.py", 
                os.path.join(deploy_dir, "moviesstore/moviesstore/settings_production.py"))
    
    print(f"✅ Deployment package created in '{deploy_dir}' directory")
    print(f"📁 Package contents:")
    for root, dirs, files in os.walk(deploy_dir):
        level = root.replace(deploy_dir, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files[:5]:  # Show first 5 files
            print(f"{subindent}{file}")
        if len(files) > 5:
            print(f"{subindent}... and {len(files) - 5} more files")
    
    return deploy_dir

if __name__ == "__main__":
    deploy_dir = create_deployment_package()
    print(f"\n🎉 Ready for deployment!")
    print(f"📦 Upload the '{deploy_dir}' folder to PythonAnywhere")
    print(f"🔗 Your site will be available at: https://yourusername.pythonanywhere.com/")
