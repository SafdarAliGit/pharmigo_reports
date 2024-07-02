from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pharmigo_reports/__init__.py
from pharmigo_reports import __version__ as version

setup(
	name="pharmigo_reports",
	version=version,
	description="This is Pharmigo Reports",
	author="VUT",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
