from sqlalchemy.testing.provision import stop_test_class_outside_fixtures

from services.user_service import UserService

user_service = UserService()
user_service.add_user(1)
user_service.add_user(3)
user_service.add_user(5)
print(user_service.is_admin(5))
user_service.close()
