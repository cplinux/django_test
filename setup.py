import setuptools

setuptools.setup(
    name="webapp",
    version="0.1.1",
    author="lcp",
    author_mail="lcp@linux98.com",
    description="Test",
    url="https://linux98.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.8.8",
    data_files=[('', ['requirements', 'start.sh', 'uwsgi.ini'])],
    py_modules=['manage']
)
