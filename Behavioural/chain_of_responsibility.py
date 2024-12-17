from abc import ABC, abstractmethod
from typing import Optional, Dict

# Handler interface
class Handler(ABC):
    def __init__(self):
        self._next_handler: Optional[Handler] = None
    
    def set_next(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: Dict) -> str:
        pass

# Concrete handlers
class AuthenticationHandler(Handler):
    def handle(self, request: Dict) -> str:
        if "username" not in request or "password" not in request:
            return "Authentication failed: Missing credentials"
        
        if request["username"] == "admin" and request["password"] == "password":
            if self._next_handler:
                return self._next_handler.handle(request)
            return "Authentication successful"
        
        return "Authentication failed: Invalid credentials"

class AuthorizationHandler(Handler):
    def handle(self, request: Dict) -> str:
        if "role" not in request:
            return "Authorization failed: Missing role"
        
        if request["role"] in ["admin", "manager"]:
            if self._next_handler:
                return self._next_handler.handle(request)
            return "Authorization successful"
        
        return "Authorization failed: Insufficient privileges"

class ValidationHandler(Handler):
    def handle(self, request: Dict) -> str:
        if "data" not in request:
            return "Validation failed: Missing data"
        
        data = request["data"]
        if not isinstance(data, str) or len(data) < 1:
            return "Validation failed: Invalid data format"
        
        if self._next_handler:
            return self._next_handler.handle(request)
        return "Validation successful"

# Client code
def main():
    # Create handlers
    authentication = AuthenticationHandler()
    authorization = AuthorizationHandler()
    validation = ValidationHandler()
    
    # Build the chain
    authentication.set_next(authorization).set_next(validation)
    
    # Test with valid request
    valid_request = {
        "username": "admin",
        "password": "password",
        "role": "admin",
        "data": "some valid data"
    }
    print("\nProcessing valid request:")
    print(authentication.handle(valid_request))
    
    # Test with invalid credentials
    invalid_auth_request = {
        "username": "admin",
        "password": "wrong",
        "role": "admin",
        "data": "some valid data"
    }
    print("\nProcessing request with invalid credentials:")
    print(authentication.handle(invalid_auth_request))
    
    # Test with insufficient privileges
    invalid_role_request = {
        "username": "admin",
        "password": "password",
        "role": "user",
        "data": "some valid data"
    }
    print("\nProcessing request with insufficient privileges:")
    print(authentication.handle(invalid_role_request))
    
    # Test with invalid data
    invalid_data_request = {
        "username": "admin",
        "password": "password",
        "role": "admin",
        "data": ""
    }
    print("\nProcessing request with invalid data:")
    print(authentication.handle(invalid_data_request))

if __name__ == "__main__":
    main() 