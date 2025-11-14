from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="orchestratransposer",
    version="1.0.0",
    description="Convert an Orchestra XML file to or from another schema",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FIXTradingCommunity/unified2orchestra",
    packages=find_packages(),
    package_data={
        "orchestratransposer.orchestra": ["schemas/**/*.xsd"],
        "orchestratransposer.sbe": ["schemas/**/*.xsd"],
        "orchestratransposer.unified": ["schemas/**/*.xsd"],
    },
    entry_points={
        "console_scripts": [
            "orchestratransposer=orchestratransposer.__main__:main",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    license="Apache License 2.0",
    keywords="FIX protocol, Orchestra, Unified Repository",
    project_urls={
        "Bug Reports": "https://github.com/FIXTradingCommunity/unified2orchestra/issues",
        "Source": "https://github.com/FIXTradingCommunity/unified2orchestra",
    },
)
