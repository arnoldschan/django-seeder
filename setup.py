import codecs
import os
import re
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Why read it, and not import?
# https://packaging.python.org/en/latest/single_source_version.html
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string')


setup(
    name='django-seeder',
    version=find_version('django_seeder', '__init__.py'),
    author='Arnold Samuel Chan',
    author_email='arnoldsamuelc@gmail.com',
    packages=['django_seeder', 'django_seeder.management',
              'django_seeder.management.commands'],
    include_package_data=True,
    url='http://github.com/arnoldschan/django-seeder',
    license='MIT',
    description='Seed your Django project with fake data',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    keywords='faker fixtures data test django seed',
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    install_requires=['django>=1.11', 'Faker>=0.7.7', 'toposort>=1.5'],
    tests_require=['django>=1.11', 'fake-factory>=0.5.0',
                   'coverage', 'django-nose'],
    test_suite="runtests.runtests",
    zip_safe=False,
)
