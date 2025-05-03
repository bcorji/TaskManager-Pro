from fastapi import HTTPException, status
from functools import wraps
from typing import List, Callable
from ..models.user import UserRole

def check_permissions(allowed_roles: List[UserRole]) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_user = kwargs.get('current_user')
            if not current_user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User not authenticated"
                )
            
            if current_user.role not in allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not enough permissions"
                )
            
            return await func(*args, **kwargs)
        return wrapper
    return decorator