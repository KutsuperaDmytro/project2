from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0',
    description='A tool for cleaning folders',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean_folder:main']},
)