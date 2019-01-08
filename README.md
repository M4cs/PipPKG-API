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
from pippkg-api import packages
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

# This Documentation is Not Complete! If you would like to find more functions look above in the source code. Most functions are pretty self explainatory.
