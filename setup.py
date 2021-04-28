import re

from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
]

requirements = []
with open('requirements.txt') as f:
    requirements.extend(f.read().splitlines())

version = ''
with open('SheriAPI/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='SheriAPI',
    version='1.0.0',
    description='A simple API wrapper to interact with the Sheri Blossom API.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    author='Nanofaux',
    author_email='nanofaux@hotmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='furry,SheriAPI,sheri blossom,yiff,fur,discord',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
