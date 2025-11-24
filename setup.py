from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="surgi_roles_access",
    version="0.0.1",
    description="Role-based dashboard and access customizations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="SurgiShop",
    packages=find_packages(),
    install_requires=[
        "frappe"
    ],
    zip_safe=False,
    include_package_data=True,
)
