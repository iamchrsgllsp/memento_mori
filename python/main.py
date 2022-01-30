from flask import Flask, request, abort, render_template, url_for

app = Flask(__name__)

# import declared routes
import routes

