# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


version = '0.3'


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='bobtemplates.migration',
    version=version,
    description='Templates for Plone projects.',
    long_description=long_description,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='web plone zope skeleton project',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/bobtemplates.migration',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
        'lxml',
        'case-conversion',
        'colorama',
        'bobtemplates.plone',
    ],
    setup_requires=[],
    tests_require=[],
    extras_require={},
    entry_points={
        'mrbob_templates': [
            'jsonify = bobtemplates.migration.bobregistry:jsonify',  # NOQA E501
        ],
    },
)
