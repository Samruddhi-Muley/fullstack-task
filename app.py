from flask import Flask
from routes.public import public_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.secret_key = "flipr_secret"

app.register_blueprint(public_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")

if __name__ == "__main__":
    app.run(debug=True)
