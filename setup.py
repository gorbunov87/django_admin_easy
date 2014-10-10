# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-admin-easy',
    version='0.1.1',
    url='http://github.com/ebertti/django-admin-easy/',
    author='Ezequiel Bertti',
    author_email='ebertti@gmail.com',
    install_requires=['django'],
    packages=['easy'],
    include_package_data=True,
    license='MIT License',
    platforms=['OS Independent'],
    description="Collection of admin fields to help to create computed or custom fields more friendly and easy way",
    long_description=(open('README.rst').read()),
    keywords='admin field fields django easy simple',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
)
