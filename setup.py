import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gainz-jwfu", # Replace with your own username
    version="0.0.1",
    author="Jun Wei Fu",
    author_email="pypi.solecistic@aleeas.com",
    description="Calculates returns of equities available on AlphaVantage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jwfu/gainz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)