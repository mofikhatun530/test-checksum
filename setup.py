from setuptools import setup, find_packages


setup(
    name='web3_checksum',
    version='1.0',
    license='MIT',
    author="Slava Ukraini",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mofikhatun530/test-checksum',
    keywords='web3 checksum',
    install_requires=[
          'requests', 'web3',
      ],

)
