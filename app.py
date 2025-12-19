from flask import Flask
from routes.public import public_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.secret_key = "flipr_secret"

app.register_blueprint(public_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
