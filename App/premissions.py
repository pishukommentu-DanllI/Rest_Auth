from rest_framework.permissions import BasePermission


class ClassPermission(BasePermission):
    message = 'Нет доступа'
    methods_list = ['GET', ]
    group_names = ['Может изменять  только Class и просматривать остальное', 'Может полностью взаимодействовать с журналом']

    def has_permission(self, request, view):
        if request.method in self.methods_list or request.user.is_staff:
            return True

        flag = False

        for name in self.group_names:
            if request.user.groups.filter(name__exact=name).exists():
                flag = True
                break
        return flag

    def has_object_permission(self, request, view, obj):
        if request.method in self.methods_list or request.user.is_staff:
            return True

        flag = False

        for name in self.group_names:
            if not request.user.groups.filter(name__exact=name).exists():
                flag = True
                break

        return flag


class SubjectPermission(ClassPermission):
    message = 'Нет доступа'
    methods_list = ['GET', ]

    group_names = ['Может изменять Student и просматривать все', 'Может полностью взаимодействовать с журналом']


class StudentPermission(ClassPermission):
    message = 'Нет доступа'
    methods_list = ['GET', ]

    group_names = ['Может изменять Student и просматривать все', 'Может полностью взаимодействовать с журналом']


