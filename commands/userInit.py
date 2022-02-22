import argparse
from packutils.user import generateUser
from packutils.comic import generateComic

def getArgs():
    parser = argparse.ArgumentParser(description="initialize user data if user is not yet available")
    parser.add_argument("-n", "--name", help="input name for user", required=True)

    return vars(parser.parse_args())

def main():
    args = getArgs()
    err = generateUser(args["name"])
    if err != None:
        raise Exception(err)    
    generateComic()

if __name__=="__main__":
    main()
