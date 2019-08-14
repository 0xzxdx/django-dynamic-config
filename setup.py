import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-dynamic-config",
    version='0.0.1',
    author="ansheng",
    author_email='ianshengme@gmail.com',
    description="Django Dynamic Config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anshengme/django-dynamic-config",
    keywords=['django', 'django config', 'django dynamic config'],
    packages=setuptools.find_packages(),
    license='LICENSE',
    install_requires=[
        'django'
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
    ]
)
