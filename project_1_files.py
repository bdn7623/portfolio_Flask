from flask import Blueprint, render_template
import glob

project_1_files = Blueprint("project_1_files",
                            __name__,
                            template_folder="templates")

@project_1_files.route("/project_1_files")
def get_files():
    files = glob.glob("static/projects/*")
    return render_template("project_1_files.html", files=files)
