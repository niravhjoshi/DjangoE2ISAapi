from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True

         if obj.owner == request.user:

             return True
         else:
             return False

# class AnonPermission(permissions.BasePermission):
#     # Persmission for non authenticated user
#     def has_permission(self, request, view):
#         return not request.user.is_authenticated()  # request.user.is_authenticated

