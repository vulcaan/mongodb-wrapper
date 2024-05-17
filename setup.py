from setuptools import find_packages, setup

setup(
    name="mongodb-wrapper",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["mongodb-wrapper=mongodb_wrapper.main:main"]},
)
