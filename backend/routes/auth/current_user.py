from app_setup import Resource, db, jwt_required, get_jwt_identity
from models.users import User

class CurrentUser(Resource):
    @jwt_required()
    def get(self):
        try:
            if (current_user := db.session.get(User, get_jwt_identity())):
                return current_user.to_dict(), 200
            else:
                return {'error': 'Could not find a user with that id'}, 404
        except Exception as e:
            return {'error': str(e)}