from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta  #used for token expiry time

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Hash Password
def hash_password(password):

    return pwd_context.hash(password)


# Verify Password
def verify_password(plain_password, hashed_password):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# Create JWT Token
def create_access_token(data):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token