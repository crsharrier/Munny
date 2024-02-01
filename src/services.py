import model
from repository.abstract_repository import AbstractRepository

repo: AbstractRepository = None
# current date = 


PATH_TO_DB = 'Munny.db'

def set_repository(new_repo: AbstractRepository):
    global repo
    repo = new_repo

