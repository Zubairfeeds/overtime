from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in overtime/__init__.py
from overtime import __version__ as version

setup(
	name="overtime",
	version=version,
	description="An app to calculate Overtime Of employees and make Expense Claim or add in Additional Salary base on requirenment",
	author="Atom Global",
	author_email="info@atom-global.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
