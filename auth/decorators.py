from flask import request, g
from functools import wraps
from services.auth_service import AuthService

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        
        if not auth_header or not auth_header.startswith("Token "):
            return {"erro": "Token ausente ou inválido"}, 401
            
        token = auth_header.split(" ")[1]
        user = AuthService.get_user_by_token(token)
        
        if not user:
            return {"erro": "Token inválido"}, 401
        
        g.current_user = user
        return f(*args, **kwargs)
    
    return wrapper

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        @auth_required
        def wrapper(*args, **kwargs):
            if g.current_user.role not in roles:
                return {"erro": "Acesso negado"}, 403
            return f(*args, **kwargs)
        return wrapper
    return decorator