try :
	from setuptools import setup

except ImportError :
	from distutils.core import setup


config = {
	'name' : 'projectname',
	'description' : "My Project's Description",
	'version' : "0.1",
	'url' : 'URL to get to it',
	'download_url' : "Where to download it.",
	'author' : "David Lartey",
	'author_email' : "me@davidlartey.com",
	'install_requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : []
}

setup(**config)

