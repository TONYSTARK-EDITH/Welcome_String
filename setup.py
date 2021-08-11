import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wstring",
    version="1.0.3",
    author="Tony Stark",
    author_email="manthirajak@gmail.com",
    description="A library to print a welcome message in patterns",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TONYSTARK-EDITH/Welcome_String",
    install_requires=[
        'colorama',
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'wstring = wstring.wstring:main'
        ]
    },
    keywords="Welcome String,python,terminal"
    ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
