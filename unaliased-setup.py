import re

from setuptools import Extension, setup

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = ""
with open("versacord/__init__.py") as f:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if match is None or match.group(1) is None:
        raise RuntimeError("version is not set")

    version = match.group(1)

if version.endswith(("a", "b", "rc")):
    # append version identifier based on commit count
    try:
        import subprocess

        p = subprocess.Popen(
            ["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = p.communicate()
        if out:
            version += out.decode("utf-8").strip()
        p = subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = p.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except Exception:
        pass

readme = ""
with open("README.rst") as f:
    readme = f.read()

extras_require = {
    "voice": ["PyNaCl>=1.3.0,<1.5"],
    "docs": [
        "sphinx==4.0.2",
        "sphinxcontrib_trio==1.1.2",
        "sphinxcontrib-websupport",
    ],
    "speed": ["orjson>=3.5.4", "aiodns>=1.1", "Brotli", "cchardet"],
}

packages = [
    "versacord",
    "versacord.types",
    "versacord.ui",
    "versacord.ui.select",
    "versacord.webhook",
    "versacord.ext.application_checks",
    "versacord.ext.commands",
    "versacord.ext.slash_utils",
    "versacord.ext.tasks",
]

setup(
    name="versacord-unaliased",
    author="versacord Developers & Rapptz",
    url="https://github.com/owera/versa-framework",
    project_urls={
        "Documentation": "https://versacord.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/owera/versa-framework/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description="A easyly to use  Python framework forked from Discord API | Versacord Framework (without the discord alias)",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
