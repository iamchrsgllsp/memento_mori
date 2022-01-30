from flask import Flask, request, abort, render_template

app = Flask(__name__)

# import declared routes
import routes

