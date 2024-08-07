#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
"""

from __future__ import unicode_literals

import io
from os import path

try:
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements

from setuptools import find_packages, setup


def get_requirements(requirements_file):
    """Use pip to parse requirements file."""
    requirements = []
    if path.isfile(requirements_file):
        for req in parse_requirements(requirements_file, session="hack"):
            try:
                if req.markers:
                    requirements.append("%s;%s" % (req.req, req.markers))
                else:
                    requirements.append("%s" % req.req)
            except AttributeError:
                requirements.append(req.requirement)
    return requirements


if __name__ == "__main__":
    HERE = path.abspath(path.dirname(__file__))
    INSTALL_REQUIRES = get_requirements(path.join(HERE, "requirements.txt"))

    with io.open(path.join(HERE, "README.rst"), encoding="utf-8") as readme:
        LONG_DESCRIPTION = readme.read()

    setup(
        name="kalabash-rspamd",
        description="The rspamd frontend of Kalabash",
        long_description=LONG_DESCRIPTION,
        license="MIT",
        url="https://alphamonak.com/",
        author="Alphamonak Solutions",
        author_email="amonak@alphamonak.com",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Framework :: Django :: 1.11",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Topic :: Communications :: Email",
            "Topic :: Internet :: WWW/HTTP",
        ],
        keywords="email rspamd dkim",
        packages=find_packages(exclude=["docs", "test_project"]),
        include_package_data=True,
        zip_safe=False,
        install_requires=INSTALL_REQUIRES,
        use_scm_version=True,
        setup_requires=["setuptools_scm"],
    )
