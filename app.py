from flask import Flask, jsonify
from models import db, User
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    @app.route('/api/users', methods=['GET'])
    def get_all_users():
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
    
    return app

    if __name__ == '__main__':
        app = create_app()
        app.run(debug=True)
    

