.. image:: https://raw.githubusercontent.com/owera/versa-framework/master/assets/repo-banner.svg
   :alt: Versa Framework

.. image:: https://img.shields.io/discord/881118111967883295?color=blue&label=discord
   :target: https://discord.gg/Fee6Kptq57
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/versa-framework.svg
   :target: https://pypi.org/project/versa-framework/
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/dm/versa-framework?color=informational&label=pypi%20downloads
   :target: https://pypi.org/project/versa-framework/
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/versa-framework.svg
   :target: https://pypi.org/project/versa-framework/
   :alt: PyPI supported Python versions
.. image:: https://img.shields.io/readthedocs/versa-framework
   :target: https://docs.versa.dev/
   :alt: Versa Framework documentation

Versa Framework
--------

A modern, easy-to-use, feature-rich, and async-ready API wrapper for Discord written in Python.


Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``
- Proper rate limit handling
- Optimised in both speed and memory

Installing
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U versa or using .git link repositore

    # Windows
    py -3 -m pip install -U versa or using .git link repositore

Otherwise to get voice support you should run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "versa[voice]"

    # Windows
    py -3 -m pip install -U versa[voice]

To install additional packages for speedup, run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "versa[speed]"

    # Windows
    py -3 -m pip install -U versa[speed]


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/owera/versa-framework/
    $ cd versa
    $ python3 -m pip install -U .[voice]


Optional Packages
~~~~~~~~~~~~~~~~~~

* `PyNaCl <https://pypi.org/project/PyNaCl/>`__ (for voice support)
* `aiodns <https://pypi.org/project/aiodns/>`__, `Brotli <https://pypi.org/project/Brotli/>`__, `cchardet <https://pypi.org/project/cchardet/>`__ (for aiohttp speedup)
* `orjson <https://pypi.org/project/orjson/>`__ (for json speedup)

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. ``apt``, ``dnf``, etc) before running the above commands:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.8-dev`` for Python 3.8)


Quick Example
~~~~~~~~~~~~~

.. code:: py

    from versa.ext import commands


    bot = commands.Bot()

    @bot.slash_command(description="Replies with pong!")
    async def ping(interaction: versa.Interaction):
        await interaction.send("Pong!", ephemeral=True)

    bot.run("token")

You can find more examples in the `examples directory <https://github.com/owera/versa-framework/blob/stable/examples/>`_.

**NOTE:** It is not advised to leave your token directly in your code, as it allows anyone with it to access your bot. If you intend to make your code public you should `store it securely <https://github.com/nextcord/nextcord/blob/stable/examples/secure_token_storage.py/>`_.

Links
------

- `Documentation <https://docs.versa.dev/>`_
- `Official Discord Server <https://discord.gg/Fee6Kptq57>`_
- `Discord API <https://discord.gg/discord-api>`_