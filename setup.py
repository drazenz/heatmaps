import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
	name="heatmapz",
	version="0.0.1",
	author="Drazen Zaric",
	author_email="drazen.zaric@gmail.com",
	description="Create heatmaps with shapes and size as a parameter",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/drazenez/heatmap",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: BSD License",
		"Operating System :: OS Independent",
	],
	install_requires=[
		'matplotlib>=3.0.3',
		'pandas',
		'seaborn'
	],
	python_requires='>=3.5',
)

