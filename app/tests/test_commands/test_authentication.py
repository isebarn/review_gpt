from app.logic.commands.authentication import sign_up
from app.logic.commands.authentication import login

def test_signup(app):
    # Arrange
    valid_signup = {
        "email": "asd@isebarn.com",
        "password": "password123"
    }


    # Act
    with app.app_context():
        response = sign_up(**valid_signup)
    
    assert response

    # verify that you cannot sign up again with the same email
    with app.app_context():
        response = sign_up(**valid_signup)

    assert not response

def test_invalid_signup_email(app):
    # Arrange
    invalid_signup = {
        "email": "asdisebarn.com",
        "password": "password123"
    }

    # Act
    with app.app_context():
        response = sign_up(**invalid_signup)

    # Assert
    assert not response

def test_invalid_signup_password(app):
    # Arrange
    invalid_signup = {
        "email": "asd2@isebarn.com",
        "password": "pass"
    }

    # Act
    with app.app_context():
        response = sign_up(**invalid_signup)

    # Assert
    assert not response

def test_login(app):
    # Arrange
    valid_signup = {
        "email": "isebarn1@isebarn.com",
        "password": "password123"
    }

    # Act
    with app.app_context():
        response = sign_up(**valid_signup)
        assert response

        response = login(**valid_signup)

        # Assert
        assert response

# test login incorrect password
def test_login_incorrect_password(app):
    # Arrange
    valid_signup = {
        "email": "isebarn2@gmail.com",
        "password": "password123"
    }

    # Act
    with app.app_context():
        response = sign_up(**valid_signup)
        assert response

        invalid_login = {
            "email": "isebarn2@gmail.com",
            "password": "aapeogjaepgoj"
        }

        response = login(**invalid_login)

        # Assert
        assert not response