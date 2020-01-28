import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'testi18n',
    packages = setuptools.find_packages(),
    version = '1.0.0',
    license = 'MIT',
    author = 'Francesco Piantini',
    author_email = 'francesco.piantini@gmail.com',
    description = 'Python I18N demo',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    python_requires='>=3.6',
)

