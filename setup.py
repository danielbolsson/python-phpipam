from distutils.core import setup
import setuptools

setup(
    name='phpipam',
    version='0.2.1',
    author="Jonas Gunz",
    author_email="himself@jonasgunz.de",
    url="https://github.com/kompetenzbolzen/python-phpipam",
    description="phpIPAM API implementation",
    packages=['phpipam'],
    install_requires=[
        "requests>=2.25.1",
        "python-dateutil>=2.8.1"
    ],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

