from flask import Flask

app = Flask(__name__, template_folder='templates')

# Register blueprint here
from routes import conversation_bp
app.register_blueprint(conversation_bp)

if __name__ == "__main__":
    app.run(debug=True)