from ariadne import ObjectType
from api.queries import resolve_getSubscribedComic

def bindQueries():
    query = ObjectType("Query")
    query.set_field("getSubscribedComic", resolve_getSubscribedComic)

    return query