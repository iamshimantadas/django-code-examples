from rest_framework.permissions import BasePermission

# class isUser(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == "GET":
#             return True
#         return request.is_authenticated and not request.user.is_manager

class isManager(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            if request.user.is_manager:
                return False
            else:
                return True 
        elif request.method == "POST":            
            if request.user.is_manager:
                return True
            else:
                return False
        elif request.method == "PUT":
            if request.user.is_manager:
                return True
            else:
                return False
        elif request.method == "PATCH":
            if request.user.is_manager:
                return True
            else:
                return False
        
                