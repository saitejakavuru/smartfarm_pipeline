import setuptools

# Read the long description from the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "smartfarm_pipeline"
AUTHOR_USER_NAME = "saitejakavuru"
SRC_REPO = "smartfarm_pipeline"
AUTHOR_EMAIL = "workbox.teja@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for smartfarm app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected option
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.8',  # Optionally specify the minimum Python version required
)
