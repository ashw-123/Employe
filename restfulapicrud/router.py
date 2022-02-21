from employeeapi.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register('Department', DepartmentViewSet)
router.register('Leaves', LeavesViewSet)
router.register(r'projects', ProjectsViewSet)
