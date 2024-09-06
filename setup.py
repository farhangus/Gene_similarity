from setuptools import setup, find_packages

setup(
    name="gene_similarity",  # The name of your package
    version="0.1.0",  # Initial version
    description="A package for visualizing gene similarity",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/farhangus/Gene_similarity",  # Your GitHub repo URL
    author="Farhang",  # Your name
    author_email="youremail@example.com",
    license="MIT",  # License type
    packages=find_packages(where="src"),  # Look for packages in the 'src' folder
    package_dir={"": "src"},
    install_requires=[
        "seaborn",
        "matplotlib",
        "pandas",
        "click",
        "numpy",
        "scipy",
        "networkx"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'gene-similarity=gene_similarity.cli:entry_point',
        ],
    },
    python_requires='>=3.6',
)

