from flask import Flask, render_template, session, redirect, \
    url_for, request, jsonify
from settings import settings

app = Flask(__name__)
app.secret_key = settings.SECRET
app.config.from_object(__name__)
