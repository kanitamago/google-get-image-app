from app import app
from app.scripts import get_photo
from flask import render_template, request, url_for, redirect
from google_images_download import google_images_download
import os

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        try:
            search_word = request.form["search-word"]
            get_pages = request.form["get-pages"]
            get_photo.options["keywords"] = search_word
            get_photo.options["limit"] = int(get_pages)
            image_path = os.path.expanduser("~") + "/Desktop"
            get_photo.options["output_directory"] = image_path
            get_photo.google_obj.download(get_photo.options)
            return render_template("result.html", search_word=search_word, get_pages=get_pages, error=None, image_path=image_path)
        except:
            return render_template("result.html", search_word=None, get_pages=None, error="エラーが発生しました")
    return redirect(url_for('index'))
