import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name="dev-note-python-LCRUZ", # Replace with your own username
  version="1.0.0",
  author="Laurence Cruz",
  author_email="laurence.p.cruz@gmail.com",
  description="A binary utility to quickly make notes in markdown",
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
   ]
)
