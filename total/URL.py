import re


def URL(i):

    URL = "https://hk.jobsdb.com/hk/search-jobs/python/" + str(i)

    return URL


def BASEURL():
    query = 'python'
    BASEURL = f'https://hk.jobsdb.com/hk/search-jobs/{query}/1'

    return BASEURL
