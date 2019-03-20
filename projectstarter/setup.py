from setuptools import setup
setup(
    name='projectstarter',
    version='0.4.2',
    description=(
    ),
    long_description='''This package will build a Python package for U.''',
    author='fjy',
    author_email='2589660302@qq.com',
    maintainer='fjy',
    maintainer_email='2589660302@qq.com',
    license='BSD License',
    platforms=["all"],
    url='https://github.com/fjy202/projectstarter/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=["wheel","click"],
    scripts=["bin/projectstarter.py"]
)
