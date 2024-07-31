from api.repositories.consulta_repository import ConsultaRepository
from api.properties import Properties

properties = Properties()
consulta_repository = ConsultaRepository()


def save(data):
    return consulta_repository.save(data)


def get_by_id_profissional(id_profissional):
    return consulta_repository.get_by_id_profissional(id_profissional)


def update(id, data):
    return consulta_repository.update(id, data)


def delete(id):
    return consulta_repository.delete(id)



