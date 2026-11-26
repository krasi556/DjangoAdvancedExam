from rest_framework.permissions import BasePermission, SAFE_METHODS


class EmployeeTierAccess(BasePermission):
    METHOD_GROUPS = {
        'POST': ['Super Sponsor', 'Inner Circle', 'No Lifer'],
        'PATCH': ['Inner Circle', 'No Lifer'],
        'PUT': ['Inner Circle', 'No Lifer'],
        'DELETE': ['No Lifer']
    }

    def has_permission(self, request, view):
        print(request.user.profile.tier)
        if request.method in SAFE_METHODS:
            return True
        group_found = self.METHOD_GROUPS.get(request.method, [])
        return request.user.groups.filter(name__in=group_found).exists()
