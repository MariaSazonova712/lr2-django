from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    bob = Animals("Рэди", 3)
    return JsonResponse(bob, safe=False, encoder=AnimalsEncoder)


class Animals:

    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека


class AnimalsEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Animals):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)