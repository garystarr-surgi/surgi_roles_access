from setuptools import setup, find_packages

setup(
    name='surgi_roles_access',
    version='0.0.1',
    description='Control Connection Shortcuts per Role',
    author='SurgiShop',
    author_email='gary.starr@surgishop.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe']
)
