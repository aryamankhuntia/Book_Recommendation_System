from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
repo_name = "Book_Recommendation_System"
author_user_name = "Aryaman Khuntia"
src_repo="recommender"
list_of_requirements = []

setup(
    name=src_repo,
    version="0.0.1",
    author=author_user_name,
    description="A Book Recommendation System using Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aryamankhuntia/Book_Recommendation_System",
    author_email="aryaman.khuntia3@gmail.com",
    packages=find_packages(),
    install_requires=list_of_requirements,
    python_requires=">=3.7",
    license="MIT"
)
