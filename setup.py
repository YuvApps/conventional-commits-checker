from setuptools import setup, find_packages

setup(
    name='conventional-commits-checker',  # This is the name of your package
    version='0.1.0',  # Initial version
    packages=find_packages(),
    description='A tool for validating Conventional Commit messages',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YuvApps/conventional-commits-checker',  # Replace with your repository URL
    author='Yuval Aharoni',
    author_email='yuvalaharoni585@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'packaging>=20.0',  # Specify the minimum version of the packaging library
    ],
)