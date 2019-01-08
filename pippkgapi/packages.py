import requests as r
import json

def package(pkgname):
    url = 'https://pypi.org/pypi/'
    resptype = '/json'
    request = r.get(url+pkgname+resptype).text
    pkginfo = json.loads(request)
    return pkginfo

def getName(pkginfo):
    name = pkginfo['info']['name']
    return name

def getAuthor(pkginfo):
    author = pkginfo['info']['author']
    return author

def getLongDesc(pkginfo):
    longDesc = pkginfo['info']['description']
    return longDesc

def getLicense(pkginfo):
    licenseType = pkginfo['info']['license']
    return licenseType

def getSummary(pkginfo):
    summary = pkginfo['info']['summary']
    return summary

def getReqs(pkginfo):
    requirements = pkginfo['info']['requires_dist']
    return requirements

def getHomePage(pkginfo):
    homePage = pkginfo['info']['home_page']
    return homePage

def getClassifiers(pkginfo):
    classifiers = pkginfo['info']['classifiers']
    return classifiers

def getProjectURLS(pkginfo):
    projURLs = pkginfo['info']['project_urls']
    return projURLs

def getURL(pkginfo):
    projURL = pkginfo['info']['project_url']
    return projURL

def getVersion(pkginfo):
    version = pkginfo['info']['version']
    return version

def getReleases(pkginfo):
    releases = []
    for i in pkginfo['releases']:
        releases.append(i)
    return releases