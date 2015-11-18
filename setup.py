"""
psql_to_csv
-----------------

when you forget to properly format the results of a query that takes forever
"""
from setuptools import setup

setup(
    name='psql_to_csv',
    version='0.1',
    packages=['psql_to_csv'],
    url='http://github.com/eriktaubeneck/psql_to_csv',
    license='MIT',
    author='Erik Taubeneck',
    author_email='erik.taubeneck@gmail.com',
    description='when you forget to properly format the results of a query that takes forever',
    long_description=__doc__,
    py_modules=['psql_to_csv'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'docopt>=0.6',
    ],
    entry_points="""
    [console_scripts]
    psql_to_csv = psql_to_csv:main
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English ',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
