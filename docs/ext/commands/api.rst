.. currentmodule:: versa

API Reference
=============

The following section outlines the API of versa's command extension module.

.. _ext_commands_api_bot:

Bots
----

Bot
~~~

.. attributetable:: versa.ext.commands.Bot

.. autoclass:: versa.ext.commands.Bot
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, check, check_once, command, event, group, listen

    .. automethod:: Bot.after_invoke()
        :decorator:

    .. automethod:: Bot.before_invoke()
        :decorator:

    .. automethod:: Bot.check()
        :decorator:versaversa

    .. automethod:: Bot.check_once()
        :decorator:

    .. automethod:: Bot.command(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.event()
        :decorator:

    .. automethod:: Bot.group(*args, **kwargs)
        :decorator:

    .. automethod:: Bot.listen(name=None)
        :decorator:

AutoShardedBot
~~~~~~~~~~~~~~

.. attributetable:: versaversa.ext.commands.AutoShardedBot

.. autoclass:: versaversa.ext.commands.AutoShardedBot
    :members:

Prefix Helpers
--------------

.. autofunction:: versaversa.ext.commands.when_mentioned

.. autofunction:: versaversa.ext.commands.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
---------------

These events function similar to :ref:`the regular events <discord-api-events>`, except they
are custom to the command extension module.

.. function:: versaversa.ext.commands.on_command_error(ctx, error)

    An error handler that is called when an error is raised
    inside a command either through user input error, check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_command_error`).

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: versaversa.ext.commands.on_command(ctx)

    An event that is called when a command is found and is about to be invoked.

    This event is called regardless of whether the command itself succeeds via
    error or completes.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. function:: versaversa.ext.commands.on_command_completion(ctx)

    An event that is called when a command has completed its invocation.

    This event is called only if the command succeeded, i.e. all checks have
    passed and the user input it correctly.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. _ext_commands_api_command:

Commands
--------

Decorators
~~~~~~~~~~

.. autofunction:: versa.ext.commands.command
    :decorator:

.. autofunction:: versa.ext.commands.group
    :decorator:

Command
~~~~~~~

.. attributetable:: versa.ext.commands.Command

.. autoclass:: versa.ext.commands.Command
    :members:
    :special-members: __call__
    :exclude-members: after_invoke, before_invoke, error

    .. automethod:: Command.after_invoke()
        :decorator:

    .. automethod:: Command.before_invoke()
        :decorator:

    .. automethod:: Command.error()
        :decorator:

Group
~~~~~

.. attributetable:: versa.ext.commands.Group

.. autoclass:: versa.ext.commands.Group
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, command, error, group

    .. automethod:: Group.after_invoke()
        :decorator:

    .. automethod:: Group.before_invoke()
        :decorator:

    .. automethod:: Group.command(*args, **kwargs)
        :decorator:

    .. automethod:: Group.error()
        :decorator:

    .. automethod:: Group.group(*args, **kwargs)
        :decorator:

GroupMixin
~~~~~~~~~~

.. attributetable:: versa.ext.commands.GroupMixin

.. autoclass:: versa.ext.commands.GroupMixin
    :members:
    :exclude-members: command, group

    .. automethod:: GroupMixin.command(*args, **kwargs)
        :decorator:

    .. automethod:: GroupMixin.group(*args, **kwargs)
        :decorator:

.. _ext_commands_api_cogs:

Cogs
----

Cog
~~~

.. attributetable:: versa.ext.commands.Cog

.. autoclass:: versa.ext.commands.Cog
    :members:
versaversa
CogMeta
~~~~~~~

.. attributetable:: versa.ext.commands.CogMeta

.. autoclass:: versa.ext.commands.CogMeta
    :members:

.. _ext_commands_help_command:

Help Commands
-------------

HelpCommand
~~~~~~~~~~~

.. attributetable:: versaversa.ext.commands.HelpCommand

.. autoclass:: versaversa.ext.commands.HelpCommand
    :members:

DefaultHelpCommand
~~~~~~~~~~~~~~~~~~

.. attributetable:: versaversa.ext.commands.DefaultHelpCommand

.. autoclass:: versaversa.ext.commands.DefaultHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

MinimalHelpCommand
~~~~~~~~~~~~~~~~~~

.. attributetable:: versaversa.ext.commands.MinimalHelpCommand

.. autoclass:: versaversa.ext.commands.MinimalHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

Paginator
~~~~~~~~~

.. attributetable:: versaversa.ext.commands.Paginator

.. autoclass:: versaversa.ext.commands.Paginator
    :members:

Enums
-----

.. class:: BucketType
    :module: versaversa.ext.commands

    Specifies a type of bucket for, e.g. a cooldown.

    .. attribute:: default

        The default bucket operates on a global basis.
    .. attribute:: user

        The user bucket operates on a per-user basis.
    .. attribute:: guild

        The guild bucket operates on a per-guild basis.
    .. attribute:: channel

        The channel bucket operates on a per-channel basis.
    .. attribute:: member

        The member bucket operates on a per-member basis.
    .. attribute:: category

        The category bucket operates on a per-category basis.
    .. attribute:: role

        The role bucket operates on a per-role basis.

        .. versionadded:: 1.3


.. _ext_commands_api_checks:

Checks
------

.. autofunction:: versa.ext.commands.check(predicate)
    :decorator:

.. autofunction:: versa.ext.commands.check_any(*checks)
    :decorator:

.. autofunction:: versa.ext.commands.has_role(item)
    :decorator:

.. autofunction:: versa.ext.commands.has_permissions(**perms)
    :decorator:

.. autofunction:: versa.ext.commands.has_guild_permissions(**perms)
    :decorator:

.. autofunction:: versa.ext.commands.has_any_role(*items)
    :decorator:

.. autofunction:: versa.ext.commands.bot_has_role(item)
    :decorator:

.. autofunction:: versa.ext.commands.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: versa.ext.commands.bot_has_guild_permissions(**perms)
    :decorator:

.. autofunction:: versa.ext.commands.bot_has_any_role(*items)
    :decorator:

.. autofunction:: versa.ext.commands.cooldown(rate, per, type=versa.ext.commands.BucketType.default)
    :decorator:

.. autofunction:: versa.ext.commands.dynamic_cooldown(cooldown, type=BucketType.default)
    :decorator:

.. autofunction:: versa.ext.commands.max_concurrency(number, per=versa.ext.commands.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: versa.ext.commands.before_invoke(coro)
    :decorator:

.. autofunction:: versa.ext.commands.after_invoke(coro)
    :decorator:

.. autofunction:: versa.ext.commands.guild_only(,)
    :decorator:

.. autofunction:: versa.ext.commands.dm_only(,)
    :decorator:

.. autofunction:: versa.ext.commands.is_owner(,)
    :decorator:

.. autofunction:: versa.ext.commands.is_nsfw(,)
    :decorator:

.. _ext_commands_api_context:

Cooldown
--------

.. attributetable:: versa.ext.commands.Cooldown

.. autoclass:: versa.ext.commands.Cooldown
    :members:

Context
-------

.. attributetable:: versa.ext.commands.Context

.. autoclass:: versa.ext.commands.Context
    :members:
    :inherited-members:
    :exclude-members: history, typing

    .. automethod:: versa.ext.commands.Context.history
        :async-for:

    .. automethod:: versa.ext.commands.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
----------

.. autoclass:: versa.ext.commands.Converter
    :members:

.. autoclass:: versa.ext.commands.ObjectConverter
    :members:

.. autoclass:: versa.ext.commands.MemberConverter
    :members:

.. autoclass:: versa.ext.commands.UserConverter
    :members:

.. autoclass:: versa.ext.commands.MessageConverter
    :members:

.. autoclass:: versa.ext.commands.PartialMessageConverter
    :members:

.. autoclass:: versa.ext.commands.GuildChannelConverter
    :members:

.. autoclass:: versa.ext.commands.TextChannelConverter
    :members:

.. autoclass:: versa.ext.commands.VoiceChannelConverter
    :members:

.. autoclass:: versa.ext.commands.StageChannelConverter
    :members:

.. autoclass:: versa.ext.commands.CategoryChannelConverter
    :members:

.. autoclass:: versa.ext.commands.InviteConverter
    :members:

.. autoclass:: versa.ext.commands.GuildConverter
    :members:

.. autoclass:: versa.ext.commands.RoleConverter
    :members:

.. autoclass:: versa.ext.commands.GameConverter
    :members:

.. autoclass:: versa.ext.commands.ColourConverter
    :members:

.. autoclass:: versa.ext.commands.EmojiConverter
    :members:

.. autoclass:: versa.ext.commands.PartialEmojiConverter
    :members:

.. autoclass:: versa.ext.commands.ThreadConverter
    :members:

.. autoclass:: versa.ext.commands.GuildStickerConverter
    :members:

.. autoclass:: versa.ext.commands.clean_content
    :members:

.. autoclass:: versa.ext.commands.Greedy()

.. autofunction:: versa.ext.commands.run_converters

Flag Converter
~~~~~~~~~~~~~~

.. autoclass:: versa.ext.commands.FlagConverter
    :members:

.. autoclass:: versa.ext.commands.Flag()
    :members:

.. autofunction:: versa.ext.commands.flag

.. _ext_commands_api_errors:

Warnings
--------

.. autoclass:: versa.ext.commands.MissingMessageContentIntentWarning

Exceptions
----------

.. autoexception:: versa.ext.commands.CommandError
    :members:

.. autoexception:: versa.ext.commands.ConversionError
    :members:

.. autoexception:: versa.ext.commands.MissingRequiredArgument
    :members:

.. autoexception:: versa.ext.commands.ArgumentParsingError
    :members:

.. autoexception:: versa.ext.commands.UnexpectedQuoteError
    :members:

.. autoexception:: versa.ext.commands.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: versa.ext.commands.ExpectedClosingQuoteError
    :members:

.. autoexception:: versa.ext.commands.BadArgument
    :members:

.. autoexception:: versa.ext.commands.BadUnionArgument
    :members:

.. autoexception:: versa.ext.commands.BadLiteralArgument
    :members:

.. autoexception:: versa.ext.commands.PrivateMessageOnly
    :members:

.. autoexception:: versa.ext.commands.NoPrivateMessage
    :members:

.. autoexception:: versa.ext.commands.CheckFailure
    :members:

.. autoexception:: versa.ext.commands.CheckAnyFailure
    :members:

.. autoexception:: versa.ext.commands.CommandNotFound
    :members:

.. autoexception:: versa.ext.commands.DisabledCommand
    :members:

.. autoexception:: versa.ext.commands.CommandInvokeError
    :members:

.. autoexception:: versa.ext.commands.TooManyArguments
    :members:

.. autoexception:: versa.ext.commands.UserInputError
    :members:

.. autoexception:: versa.ext.commands.CommandOnCooldown
    :members:

.. autoexception:: versa.ext.commands.MaxConcurrencyReached
    :members:

.. autoexception:: versa.ext.commands.NotOwner
    :members:

.. autoexception:: versa.ext.commands.MessageNotFound
    :members:

.. autoexception:: versa.ext.commands.MemberNotFound
    :members:
versa.. autoexception:: versa.ext.commands.GuildNotFound
    :members:

.. autoexception:: versa.ext.commands.UserNotFound
    :members:

.. autoexception:: versa.ext.commands.ChannelNotFound
    :members:

.. autoexception:: versa.ext.commands.ScheduledEventNotFound
    :members:

.. autoexception:: versa.ext.commands.ChannelNotReadable
    :members:

.. autoexception:: versa.ext.commands.ThreadNotFound
    :members:

.. autoexception:: versa.ext.commands.BadColourArgument
    :members:

.. autoexception:: versa.ext.commands.RoleNotFound
    :members:

.. autoexception:: versa.ext.commands.BadInviteArgument
    :members:

.. autoexception:: versa.ext.commands.EmojiNotFound
    :members:

.. autoexception:: versa.ext.commands.PartialEmojiConversionFailure
    :members:

.. autoexception:: versa.ext.commands.GuildStickerNotFound
    :members:

.. autoexception:: versa.ext.commands.BadBoolArgument
    :members:

.. autoexception:: versa.ext.commands.MissingPermissions
    :members:

.. autoexception:: versa.ext.commands.BotMissingPermissions
    :members:

.. autoexception:: versa.ext.commands.MissingRole
    :members:

.. autoexception:: versa.ext.commands.BotMissingRole
    :members:

.. autoexception:: versa.ext.commands.MissingAnyRole
    :members:

.. autoexception:: versa.ext.commands.BotMissingAnyRole
    :members:

.. autoexception:: versa.ext.commands.NSFWChannelRequired
    :members:

.. autoexception:: versa.ext.commands.FlagError
    :members:

.. autoexception:: versa.ext.commands.BadFlagArgument
    :members:

.. autoexception:: versa.ext.commands.MissingFlagArgument
    :members:

.. autoexception:: versa.ext.commands.TooManyFlags
    :members:

.. autoexception:: versa.ext.commands.MissingRequiredFlag
    :members:

.. autoexception:: versa.ext.commands.ExtensionError
    :members:

.. autoexception:: versa.ext.commands.ExtensionAlreadyLoaded
    :members:

.. autoexception:: versa.ext.commands.ExtensionNotLoaded
    :members:

.. autoexception:: versa.ext.commands.NoEntryPointError
    :members:

.. autoexception:: versa.ext.commands.InvalidSetupArguments
    :members:

.. autoexception:: versa.ext.commands.ExtensionFailed
    :members:

.. autoexception:: versa.ext.commands.ExtensionNotFound
    :members:

.. autoexception:: versa.ext.commands.CommandRegistrationError
    :members:


Exception Hierarchy
~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`~.DiscordException`
        - :exc:`~.commands.CommandError`
            - :exc:`~.commands.ConversionError`
            - :exc:`~.commands.UserInputError`
                - :exc:`~.commands.MissingRequiredArgument`
                - :exc:`~.commands.TooManyArguments`
                - :exc:`~.commands.BadArgument`
                    - :exc:`~.commands.MessageNotFound`
                    - :exc:`~.commands.MemberNotFound`
                    - :exc:`~.commands.GuildNotFound`
                    - :exc:`~.commands.UserNotFound`
                    - :exc:`~.commands.ChannelNotFound`
                    - :exc:`~.commands.ChannelNotReadable`
                    - :exc:`~.commands.BadColourArgument`
                    - :exc:`~.commands.RoleNotFound`
                    - :exc:`~.commands.BadInviteArgument`
                    - :exc:`~.commands.EmojiNotFound`
                    - :exc:`~.commands.GuildStickerNotFound`
                    - :exc:`~.commands.PartialEmojiConversionFailure`
                    - :exc:`~.commands.BadBoolArgument`
                    - :exc:`~.commands.ThreadNotFound`
                    - :exc:`~.commands.ScheduledEventNotFound`
                    - :exc:`~.commands.FlagError`
                        - :exc:`~.commands.BadFlagArgument`
                        - :exc:`~.commands.MissingFlagArgument`
                        - :exc:`~.commands.TooManyFlags`
                        - :exc:`~.commands.MissingRequiredFlag`
                - :exc:`~.commands.BadUnionArgument`
                - :exc:`~.commands.BadLiteralArgument`
                - :exc:`~.commands.ArgumentParsingError`
                    - :exc:`~.commands.UnexpectedQuoteError`
                    - :exc:`~.commands.InvalidEndOfQuotedStringError`
                    - :exc:`~.commands.ExpectedClosingQuoteError`
            - :exc:`~.commands.CommandNotFound`
            - :exc:`~.commands.CheckFailure`
                - :exc:`~.commands.CheckAnyFailure`
                - :exc:`~.commands.PrivateMessageOnly`
                - :exc:`~.commands.NoPrivateMessage`
                - :exc:`~.commands.NotOwner`
                - :exc:`~.commands.MissingPermissions`
                - :exc:`~.commands.BotMissingPermissions`
                - :exc:`~.commands.MissingRole`
                - :exc:`~.commands.BotMissingRole`
                - :exc:`~.commands.MissingAnyRole`
                - :exc:`~.commands.BotMissingAnyRole`
                - :exc:`~.commands.NSFWChannelRequired`
            - :exc:`~.commands.DisabledCommand`
            - :exc:`~.commands.CommandInvokeError`
            - :exc:`~.commands.CommandOnCooldown`
            - :exc:`~.commands.MaxConcurrencyReached`
        - :exc:`~.commands.ExtensionError`
            - :exc:`~.commands.ExtensionAlreadyLoaded`
            - :exc:`~.commands.ExtensionNotLoaded`
            - :exc:`~.commands.NoEntryPointError`
            - :exc:`~.commands.InvalidSetupArguments`
            - :exc:`~.commands.ExtensionFailed`
            - :exc:`~.commands.ExtensionNotFound`
    - :exc:`~.ClientException`
        - :exc:`~.commands.CommandRegistrationError`
