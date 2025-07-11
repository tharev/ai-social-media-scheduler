"""
AI Social Media Scheduler
AI-powered social media content scheduling and management platform

Features:
- Multi-platform social media posting (Twitter, Facebook, LinkedIn, Instagram)
- AI-powered content generation with OpenAI and Fellou AI
- Advanced scheduling with timezone support
- Analytics and performance tracking
- Content calendar management
- Hashtag optimization
- Image and video processing
- Integration with Zapier, n8n, Google Cloud, Manus AI
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
import json
import requests
import tweepy
import facebook
