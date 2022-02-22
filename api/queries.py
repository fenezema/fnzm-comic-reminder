from packutils.helper import fetchJSON, buildUserComicFilePath

def resolve_getSubscribedComic(obj, info, userID):
    comics = fetchJSON(buildUserComicFilePath(userID))

    resp = []
    for key in comics:
        resp.append(comics[key])
    
    return resp
