# default code
import setuptools

# Handle missing README.md
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A detailed description of the project."

__version__ = "0.0.0"

REPO_NAME = "end-to-end-machine-learning-Implementation"
AUTHOR_USER_NAME = "Ramyasreekodati"
SRC_REPO = "wine_quality"
AUTHOR_EMAIL = "kodatiramyasree123@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",  # Added missing comma
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected line
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
