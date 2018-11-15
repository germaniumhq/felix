from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

packages = find_packages()

setup(
    name='germanium_build_monitor',
    version='0.1.master',
    description='germanium_build_monitor',
    long_description=readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',
    entry_points={
        "console_scripts": [
            "germanium_build_monitor = germanium_build_monitor.mainapp:main"
        ]
    },
    install_requires=[
        "PySide2",
        "mopyx==0.5.3",
        "python-jenkins",
        "PyYAML >=3.12, <3.13",
        "arrow >= 0.12.1, < 0.13"],
    packages=packages,
    package_data={
        '': ['*.txt', '*.rst']
    })
