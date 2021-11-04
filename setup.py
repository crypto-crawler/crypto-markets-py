from setuptools import find_packages, setup


def build_native(spec):
    build = spec.add_external_build(cmd=['cargo', 'build', '--release'],
                                    path='./crypto-markets-ffi')
    spec.add_cffi_module(module_path='crypto_markets._lowlevel',
                         dylib=lambda: build.find_dylib(
                             'crypto_markets_ffi', in_path='target/release'),
                         header_filename=lambda: build.find_header(
                             'crypto_markets.h', in_path='include'),
                         rtld_flags=['NOW', 'NODELETE'])


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='crypto_markets',
    version="0.0.1",
    author="soulmachine",
    description="Fetch trading markets from a cryptocurrency exchange",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soulmachine/crypto-markets-py",
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['milksnake'],
    install_requires=['cffi'],
    milksnake_tasks=[build_native],
    python_requires='>=3.6',
    license='Apache License 2.0',
    license_files=('LICENSE',),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['blockchain', 'cryptocurrency', 'trading'],
)
