import re
import hashlib

def validar_contrasena(password):
    if len(password) < 6:
        return False
    if not re.search(r'[A-Za-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True

def encriptar_contrasena(passwd):
    return hashlib.sha256(passwd.encode()).hexdigest()