from setuptools import setup

## edit below variables as per your requirements -
AUTHOR_USER_NAME = "Shweta Gupta"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description="A small package for Movie Recommender System",
    long_description_content_type="text/markdown",
    author_email="entbappy73@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)