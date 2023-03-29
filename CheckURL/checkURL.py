import request


def BASEURL():
    BASEURL = "https://hk.jobsdb.com/hk/search-jobs/python/"
    return BASEURL


def URL(i):
    URL = "https://hk.jobsdb.com/hk/search-jobs/python/" + str(i)
    return URL


def checkURL(URL):
    table = request.request(URL).findAll('h1')

    if len(table) == 0:
        return False
    else:
        return True


# checkURL(str(BASEURL()))
# checkURL(URL(1))
