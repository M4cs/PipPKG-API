<p align="center">
  <a href="https://pepy.tech/project/pippkg-api"><img src="https://pepy.tech/badge/pippkg-api/week"></a>
  <a href="https://pepy.tech/project/pippkg-api"><img src="https://pepy.tech/badge/pippkg-api/month"></a>
  <a href="https://pepy.tech/project/pippkg-api"><img src="https://pepy.tech/badge/pippkg-api"></a></br>
  <a href='https://github.com/M4cs/PipPKG-API/issues/'><img src='https://img.shields.io/github/issues/M4cs/PipPKG-API.svg'></a>
  <a href='https://github.com/M4cs/PipPKG-API/forks/'><img src='https://img.shields.io/github/forks/M4cs/PipPKG-API.svg'></a>
  <a href='https://github.com/M4cs/PipPKG-API/blob/master/LICENSE.md/'><img src='https://img.shields.io/github/license/M4cs/PipPKG-API.svg'></a>
  <a href='https://github.com/M4cs/PipPKG-API/stars/'><img src='https://img.shields.io/github/stars/M4cs/PipPKG-API.svg'></a>
  <a href="https://discord.gg/7VN9VZe"><img src="https://img.shields.io/badge/discord-join-blue.svg?syle=popout"></a>
</p>

# PipPKG API

PipPKG is a GUI for Pip that I have been working on in order to make managing your pip packages easier. While the GUI isn't complete I have completed the API wrapper for PyPi.org I will be using in it. I decided to open source it and release it on pip so that you guys could use it in your projects as well. You **do not need any API keys to use this**. Read on for more documentation.

# Getting Started

*Installing with VirtualEnv and Pip*
```
cd project-name
virtualenv env
source env/bin/activate on Unix or source .\env\bin\activate on Windows
pip3 install pippkg-api requests
```

*Installing without VirtualEnv w/ Pip*
```
pip3 install pippkg-api requests --user
cd project-name
```

*Installing with VirtualEnv w/ Setup.py*
```
cd project-name
virtualenv env
source env/bin/activate on Unix or source .\env\bin\activate on Windows
git clone https://github.com/M4cs/PipPKG-API.git
cd PipPKG-API/
python3 setup.py install
```

*Installing without VirtualEnv w/ Setup.py*
```
git clone https://github.com/M4cs/PipPKG-API.git
cd PipPKG-API/
python3 setup.py install
```

# PipPKG API - Packages

The packages module in PipPKG API is used for gaining general information about the most recent version of the package. With this module you can grab basically any general info about the package in question. Below is documentation on how to use the module.


## Getting Started

Import PipPKG API Packages like this:
```
from pippkgapi import packages
```

To get the info for the package define pkginfo (or any variable) like so:
```
pkginfo = packages.package('name-of-pip-package')
```

**You must include the above two lines in order to use both the Packages and Releases module in PipPKG API. In the rest of this documentation pkginfo will refer to the variable above.**

### package('name of package') - Returns Dictionary of JSON Response

The `package()` module is the function that grabs and stores all the information about the queried package in a dictionary. The rest of the functions then read from this dictionary to return a value. 

### getAuthor(pkginfo) - Returns String

The `getAuthor()` function does exactly what it sounds like. It returns the Author of the package.

Usage:
```
author = packages.getAuthor()
```

### getLongDesc(pkginfo) - Returns String

The `getLongDesc()` function gets the main description of the package. This is the description you will see when visiting the PyPi page for said module.

Usage:
```
longDescription = packages.getLongDesc(pkginfo)
```

### getLicense(pkginfo) - Returns String

The `getLicense()` function gets the license of the queried package and returns it.

Usage:
```
licenseType = packages.getLicense(pkginfo)
```

### getSummary(pkginfo) - Returns String

The `getSummary()` function returns the short summary of the package. Like the one you would see when quering with pip.

Usage:
```
summary = packages.getSummary(pkginfo)
```

### getReqs(pkginfo) - Returns List

The `getReqs()` function returns a list of requirements for the said project.

Usage:
```
requirements = packages.getReqs(pkginfo)
>> ['requests', 'colorama']
requirements[0]
>> 'requests'
```

### getHomePage(pkginfo) - Returns String

The `getHomePage()` function returns the URL for the home page of the pip package.

Usage:
```
homepage = packages.getHomePage(pkginfo)
>> https://example.com/and/file/path.html
```

### getClassifiers(pkginfo) - Returns List

The `getClassifiers()` function returns a list of all classifiers of said package.

Usage:
```
classifiers = packages.getClassifiers(pkginfo)
```

### getProjectURLs(pkginfo) - Returns List

The `getProjectURLs()` function returns a list of the defined urls the author uploaded the package with.

Usage:
```
projectURLs = packages.getProjectURLs(pkginfo)
```

### getReleases(pkginfo) - Returns List

The `getReleases()` function returns a list of release versions that are available on PyPi for said package. You can use these release numbers and values in the Releases module of PipPKG API.

Usage:
```
releases = packages.getReleases(pkginfo)
print(releases)
>> ['1.1.11', '1.1.12']
from pippkgapi import releases
releaseOneSize = releases.getSize(pkginfo, releases[0])
```

This will return the size of the first release in the releases list.

# PipPKG API - Releases:

## Getting Started

In order to use the releases module of PipPKG you must first get your pkginfo with the packages module. *Refer to **PipPKG API - Packages**.* It also requires a release version for each function. You can use the `packages.getReleases(pkginfo)` function to get a list of available packages.

```
from pippkgapi import packages
pkginfo = packages.package('package name')
releases = packages.getReleases(pkginfo)
rnum = releases[0]
from pippkgapi import releases
releaseFilenames = releases.getSize(pkginfo, rnum)
```

**The argument that is rnum is = to the release number you want to grab info about.**

### getReleaseMD5Hashes(pkginfo, rnum) - Returns String(s)

The `getReleaseMD5Hashes()` function will return the MD5 hashes for the packages of that specific release.

Usage:
```
md5hashes = releases.getReleaseMD5Hashes(pkginfo, rnum)
```

### getReleaseSHA256Hashes(pkginfo, rnum) - Returns String(s)

The `getReleaseSHA256Hashes()` function works the same as the `getReleaseMD5Hashes()` function but instead it returns the SHA256 Hash.

Usage:
```sha256hashes = releases.getReleaseSHA256Hashes(pkginfo, rnum)```

### getReleaseFilenames(pkginfo, rnum) - Returns List

The `getReleaseFilenames()` function returns a list including the packagetype, filename, and the version.

Usage:
```
releaseFilenames = releases.getReleaseFilenames(pkginfo, rnum)
```

### getReleaseFileURLs(pkginfo, rnum) - Returns List

The `getReleaseFileURLs()` function returns a list including the package type and the url to that package.

Usage:
```
releaseURLs = releases.getReleaseFileURLs(pkginfo, rnum)
```

### getReleaseSize(pkginfo, rnum) - Returns List
The `getReleaseSize()` function returns a list including the package type and the size of that said package.

Usage:
```
releaseSize = release.getReleaseFileURLs(pkginfo, rnum)
```
**This function works best in conjunction with `getReleaseSize()`**

# Contributions:

If you would like to contribute and add more functions or fix something up feel free to make a Pull Request. If I find your changes useful and working I will more than likely merge it! So feel free to add something if you feel it's lacking something important.
