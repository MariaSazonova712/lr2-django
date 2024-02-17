from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    bob = Person("Bob", 41)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)


class Person:

    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека


class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)