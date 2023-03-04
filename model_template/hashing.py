# contains the utils functions related to the password encryption


from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hash_pass, plain_pass):
        return pwd_cxt.verify(plain_pass, hash_pass)


