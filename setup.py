import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="passg",
	version="1.2",
	author="Yasin Amirany",
	author_email="yasin.amirany@gmail.com",
	description="strong password generator",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/yasin1ar/passg",
	packages=setuptools.find_packages(),
	license="MIT",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
	package_data={"passg": ["py.typed"]},
    include_package_data=True,
)
