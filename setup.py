from setuptools import setup

setup(
    name='pyxmr',
    version='0.1',
    packages=['pyxmr'],
    include_package_data=True,
    license='BSD License',
    description='Provides an async interface to the Monero RPC, HTTP & CLI',
    url='http://r1b.solutions/',
    author='Robert C Jensen',
    author_email='sysop@r1b.solutions',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
