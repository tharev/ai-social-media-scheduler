"""
AI Social Media Scheduler - Configuration Settings
===============================================
Configuration management for AI-powered social media scheduling platform
"""

import os
from datetime import timedelta
from typing import Dict, List, Optional

class Config:
    """Base configuration class"""
    
    # === CORE APPLICATION SETTINGS ===
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None
    
    # === DATABASE CONFIGURATION ===
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///social_scheduler.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True
    }
    
