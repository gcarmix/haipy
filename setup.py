'''
setup.py
'''
import os
from setuptools import setup

def read(fname):
    '''
    Utility function to read the README file
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    '''
    return open(os.path.join(os.path.dirname(__file__), fname),encoding="utf-8").read()


setup(
  # METADATA...
  name = 'haipy',
  version = '1.0.3',
  url = 'https://github.com/gcarmix/haipy',
  download_url = "https://github.com/gcarmix/haipy/archive/master.zip",
  project_urls = {
    "Bug Tracker": "https://github.com/gcarmix/haipy/issues",
    "Documentation": "https://github.com/gcarmix/haipy/blob/master/README.md",
    "Source Code": "https://github.com/gcarmix/haipy.git",
  },
  author = 'gcarmix',
  author_email = 'carmixdev@gmail.com',
  maintainer = 'gcarmix',
  maintainer_email = 'carmixdev@gmail.com',
  description = 'Haipy: Hash Identifier for Python',
  license = 'MIT',
  long_description = read('README.md'),
  long_description_content_type = 'text/markdown',
  platforms = ['LINUX', 'MAC', 'WINDOWS'],
  # OPTIONS...
  entry_points = {'console_scripts': ['haipy=haipy.haipy:main']},
  include_package_data = True,
  install_requires = ['importlib_resources'],
  packages = ['haipy','haipy.data'],
  package_dir = {'haipy': 'src/haipy'},
  package_data = {'haipy': ['data/*']},
)
