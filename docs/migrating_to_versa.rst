.. currentmodule:: versacord

.. _migrating_versacord:

Migrating to versacord
=====================

Due to the `original discord.py repository <https://github.com/Rapptz/discord.py>`_ becoming read-only, we decided
that it would be necessary to fork it and keep on developing further. We also wanted to change the name and voted on
versacord in order to properly register it at pypi.

Porting from discord.py
-----------------------

In order to port a bot using discord.py to versacord, follow these steps:

1. Uninstall discord.py:

    .. code:: sh

        # Linux/macOS
        python3 -m pip uninstall discord.py

        # Windows
        py -3 -m pip uninstall discord.py

2. Install versacord:

    .. code:: sh

        # Linux/macOS
        python3 -m pip install -U versacord or using .git link repositore

        # Windows
        py -3 -m pip install -U versacord or using .git link repositore

3. Update the following import statements:

    * ``import discord`` -> ``import versacord``
    * ``from discord.ext`` -> ``from versacord.ext``

4. For all places in your code that used ``discord`` (embeds, colors, etc), change them to use ``versacord``.

    Note: Steps 3 and 4 are not entirely necessary and your code should still work, but is highly recommended.

    For more information on migrations, view the rest of the migration documentation:

.. toctree::
    :maxdepth: 1

    migrating
    migrating_2
