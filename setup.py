import os
import setuptools
import sys

setuptools.setup(
  setup_requires=['pbr'],
  python_requires="~=3.6", # >= 3.6 < 4.0
  include_package_data=True,
  extras_require={
    "deflate": [ "deflate" ],
  },
  entry_points={
    "console_scripts": [
      "cloudfiles=cloudfiles_cli:main"
    ],
  },
  pbr=True
)

