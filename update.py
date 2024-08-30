from flask_bcrypt import Bcrypt
from flaskblog import db, app
from flaskblog.models import User  # Adjust the import based on your project structure

bcrypt = Bcrypt(app)

def update_password(username, new_password):
    hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
    user = User.query.filter_by(username=username).first()
    if user:
        user.password = hashed_password
        db.session.commit()
        print(f"Password for user '{username}' has been updated.")
    else:
        print(f"User '{username}' not found.")

if __name__ == "__main__":
    username = "amisha"  # Replace with your admin username
    new_password = "amishaflaskjr10"  # Replace with the new password
    with app.app_context():
        update_password(username, new_password)



#sawanjr10 ===sawanflaskjr10
#amisha===