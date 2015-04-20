from flask import Flask, render_template, session, redirect, \
    url_for, request, jsonify
from settings import settings

app = Flask(__name__)
app.secret_key = settings.SECRET
app.config.from_object(__name__)

from views import instrument as instruments_views, user as user_views
from auth.views import login
