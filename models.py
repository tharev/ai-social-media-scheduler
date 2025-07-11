"""
AI Social Media Scheduler - Database Models
==========================================
SQLAlchemy database models for AI-powered social media scheduling platform
"""

from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
import uuid

db = SQLAlchemy()

class PostStatus(Enum):
    """Post status enumeration"""
    DRAFT = "draft"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    FAILED = "failed"
    CANCELLED = "cancelled"

class Platform(Enum):
    """Social media platform enumeration"""
