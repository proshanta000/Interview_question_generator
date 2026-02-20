import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Interview_question_generator"
AUTHOR_USER_NAME = "proshanta000"
# This must match the folder name inside 'src'
SRC_REPO = "Interview_question_generator" 
AUTHOR_EMAIL = "proshanta.mithu5@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for PDF-based Interview Question & Answer generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    # This part is crucial for the modular structure:
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)