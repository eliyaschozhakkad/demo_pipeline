from setuptools import setup, find_packages

setup(name="census_income",
      version="0.0.1",
      author="eliyas",
      author_email="eliyasch@gmail.com",
      packages=find_packages(),
      install_requires = ["pandas", "numpy", "flask"]
      )
