from setuptools import setup

with open ('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

repo_name = 'book-recomendation'
author = 'gxbriellops'
src_repo = 'src'
list_of_requirements = ['streamlit','numpy']

setup(
    name=repo_name,
    version='0.0.1',
    author=author,
    description='Book recomendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{author}/{repo_name}',
    author_email='qkXg7@example.com',
    packages=src_repo,
    install_requires=list_of_requirements
)