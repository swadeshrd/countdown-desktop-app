import os

from setuptools import find_packages, setup


def get_requirement(f):
    return open(os.path.join("requirements", f)).read().splitlines()


setup(
    name="countdown-desktop-app",
    version="0.0.0",
    author="Swadesh Ranjan Dash",
    description="Countdown Desktop App",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=get_requirement("app.txt"),
)
