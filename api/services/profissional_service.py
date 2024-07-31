from api.repositories.profissional_repository import ProfissionalRepository
from api.properties import Properties

properties = Properties()
profissional_repository = ProfissionalRepository()


def save(data):
    return profissional_repository.save(data)


def update(id, data):
    return profissional_repository.update(id, data)


def delete(id):
    return profissional_repository.delete(id)



