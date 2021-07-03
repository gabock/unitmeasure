import setuptools



setuptools.setup(
    name="unitmeasure",
    version="0.1.0",
    author="Greg Bock",
    description="Python units and measurements",
    url="https://github.com/gabock/unitmeasure",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)