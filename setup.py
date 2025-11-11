from setuptools import find_packages, setup

setup(
    name='custom_nav_control',
    version='1.0',
    description='NetBox plugin to hide IPAM menu for non-superusers',
    author='Your Name',
    author_email='you@example.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
