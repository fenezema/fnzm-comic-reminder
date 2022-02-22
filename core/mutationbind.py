from ariadne import ObjectType
from api.mutations import resolve_addNewComic, resolve_updateUserComicLastRead

def bindMutations():
    mutation = ObjectType("Mutation")
    mutation.set_field("addNewComic", resolve_addNewComic)
    mutation.set_field("updateUserComicLastRead", resolve_updateUserComicLastRead)
    
    return mutation