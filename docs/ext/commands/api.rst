.. currentmodule:: versacord

API Reference
=============

The following section outlines the API of versacord's command extension module.

.. _ext_commands_api_bot:

Bots
----

Bot
~~~

.. attributetable:: versacord.ext.commands.Bot

.. autoclass:: versacord.ext.commands.Bot
    :members:
    :inherited-members:
    :exclude-members: after_invoke, before_invoke, check, check_once, command, event, group, listen

    .. automethod:: Bot.after_invoke()
        :decorator:

    .. automethod:: Bot.before_invoke()
        :decorator:

    .. automethod:: Bot.check()
        :decorator:versacordversacord

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

.. attributetable:: versacordversacord.ext.commands.AutoShardedBot

.. autoclass:: versacordversacord.ext.commands.AutoShardedBot
    :members:

Prefix Helpers
--------------

.. autofunction:: versacordversacord.ext.commands.when_mentioned

.. autofunction:: versacordversacord.ext.commands.when_mentioned_or

.. _ext_commands_api_events:

Event Reference
---------------

These events function similar to :ref:`the regular events <discord-api-events>`, except they
are custom to the command extension module.

.. function:: versacordversacord.ext.commands.on_command_error(ctx, error)

    An error handler that is called when an error is raised
    inside a command either through user input error, check
    failure, or an error in your own code.

    A default one is provided (:meth:`.Bot.on_command_error`).

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`
    :param error: The error that was raised.
    :type error: :class:`.CommandError` derived

.. function:: versacordversacord.ext.commands.on_command(ctx)

    An event that is called when a command is found and is about to be invoked.

    This event is called regardless of whether the command itself succeeds via
    error or completes.

    :param ctx: The invocation context.
    :type ctx: :class:`.Context`

.. function:: versacordversacord.ext.commands.on_command_completion(ctx)

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

.. autofunction:: versacord.ext.commands.command
    :decorator:

.. autofunction:: versacord.ext.commands.group
    :decorator:

Command
~~~~~~~

.. attributetable:: versacord.ext.commands.Command

.. autoclass:: versacord.ext.commands.Command
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

.. attributetable:: versacord.ext.commands.Group

.. autoclass:: versacord.ext.commands.Group
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

.. attributetable:: versacord.ext.commands.GroupMixin

.. autoclass:: versacord.ext.commands.GroupMixin
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

.. attributetable:: versacord.ext.commands.Cog

.. autoclass:: versacord.ext.commands.Cog
    :members:
versacordversacord
CogMeta
~~~~~~~

.. attributetable:: versacord.ext.commands.CogMeta

.. autoclass:: versacord.ext.commands.CogMeta
    :members:

.. _ext_commands_help_command:

Help Commands
-------------

HelpCommand
~~~~~~~~~~~

.. attributetable:: versacordversacord.ext.commands.HelpCommand

.. autoclass:: versacordversacord.ext.commands.HelpCommand
    :members:

DefaultHelpCommand
~~~~~~~~~~~~~~~~~~

.. attributetable:: versacordversacord.ext.commands.DefaultHelpCommand

.. autoclass:: versacordversacord.ext.commands.DefaultHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

MinimalHelpCommand
~~~~~~~~~~~~~~~~~~

.. attributetable:: versacordversacord.ext.commands.MinimalHelpCommand

.. autoclass:: versacordversacord.ext.commands.MinimalHelpCommand
    :members:
    :exclude-members: send_bot_help, send_cog_help, send_group_help, send_command_help, prepare_help_command

Paginator
~~~~~~~~~

.. attributetable:: versacordversacord.ext.commands.Paginator

.. autoclass:: versacordversacord.ext.commands.Paginator
    :members:

Enums
-----

.. class:: BucketType
    :module: versacordversacord.ext.commands

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

.. autofunction:: versacord.ext.commands.check(predicate)
    :decorator:

.. autofunction:: versacord.ext.commands.check_any(*checks)
    :decorator:

.. autofunction:: versacord.ext.commands.has_role(item)
    :decorator:

.. autofunction:: versacord.ext.commands.has_permissions(**perms)
    :decorator:

.. autofunction:: versacord.ext.commands.has_guild_permissions(**perms)
    :decorator:

.. autofunction:: versacord.ext.commands.has_any_role(*items)
    :decorator:

.. autofunction:: versacord.ext.commands.bot_has_role(item)
    :decorator:

.. autofunction:: versacord.ext.commands.bot_has_permissions(**perms)
    :decorator:

.. autofunction:: versacord.ext.commands.bot_has_guild_permissions(**perms)
    :decorator:

.. autofunction:: versacord.ext.commands.bot_has_any_role(*items)
    :decorator:

.. autofunction:: versacord.ext.commands.cooldown(rate, per, type=versacord.ext.commands.BucketType.default)
    :decorator:

.. autofunction:: versacord.ext.commands.dynamic_cooldown(cooldown, type=BucketType.default)
    :decorator:

.. autofunction:: versacord.ext.commands.max_concurrency(number, per=versacord.ext.commands.BucketType.default, *, wait=False)
    :decorator:

.. autofunction:: versacord.ext.commands.before_invoke(coro)
    :decorator:

.. autofunction:: versacord.ext.commands.after_invoke(coro)
    :decorator:

.. autofunction:: versacord.ext.commands.guild_only(,)
    :decorator:

.. autofunction:: versacord.ext.commands.dm_only(,)
    :decorator:

.. autofunction:: versacord.ext.commands.is_owner(,)
    :decorator:

.. autofunction:: versacord.ext.commands.is_nsfw(,)
    :decorator:

.. _ext_commands_api_context:

Cooldown
--------

.. attributetable:: versacord.ext.commands.Cooldown

.. autoclass:: versacord.ext.commands.Cooldown
    :members:

Context
-------

.. attributetable:: versacord.ext.commands.Context

.. autoclass:: versacord.ext.commands.Context
    :members:
    :inherited-members:
    :exclude-members: history, typing

    .. automethod:: versacord.ext.commands.Context.history
        :async-for:

    .. automethod:: versacord.ext.commands.Context.typing
        :async-with:

.. _ext_commands_api_converters:

Converters
----------

.. autoclass:: versacord.ext.commands.Converter
    :members:

.. autoclass:: versacord.ext.commands.ObjectConverter
    :members:

.. autoclass:: versacord.ext.commands.MemberConverter
    :members:

.. autoclass:: versacord.ext.commands.UserConverter
    :members:

.. autoclass:: versacord.ext.commands.MessageConverter
    :members:

.. autoclass:: versacord.ext.commands.PartialMessageConverter
    :members:

.. autoclass:: versacord.ext.commands.GuildChannelConverter
    :members:

.. autoclass:: versacord.ext.commands.TextChannelConverter
    :members:

.. autoclass:: versacord.ext.commands.VoiceChannelConverter
    :members:

.. autoclass:: versacord.ext.commands.StageChannelConverter
    :members:

.. autoclass:: versacord.ext.commands.CategoryChannelConverter
    :members:

.. autoclass:: versacord.ext.commands.InviteConverter
    :members:

.. autoclass:: versacord.ext.commands.GuildConverter
    :members:

.. autoclass:: versacord.ext.commands.RoleConverter
    :members:

.. autoclass:: versacord.ext.commands.GameConverter
    :members:

.. autoclass:: versacord.ext.commands.ColourConverter
    :members:

.. autoclass:: versacord.ext.commands.EmojiConverter
    :members:

.. autoclass:: versacord.ext.commands.PartialEmojiConverter
    :members:

.. autoclass:: versacord.ext.commands.ThreadConverter
    :members:

.. autoclass:: versacord.ext.commands.GuildStickerConverter
    :members:

.. autoclass:: versacord.ext.commands.clean_content
    :members:

.. autoclass:: versacord.ext.commands.Greedy()

.. autofunction:: versacord.ext.commands.run_converters

Flag Converter
~~~~~~~~~~~~~~

.. autoclass:: versacord.ext.commands.FlagConverter
    :members:

.. autoclass:: versacord.ext.commands.Flag()
    :members:

.. autofunction:: versacord.ext.commands.flag

.. _ext_commands_api_errors:

Warnings
--------

.. autoclass:: versacord.ext.commands.MissingMessageContentIntentWarning

Exceptions
----------

.. autoexception:: versacord.ext.commands.CommandError
    :members:

.. autoexception:: versacord.ext.commands.ConversionError
    :members:

.. autoexception:: versacord.ext.commands.MissingRequiredArgument
    :members:

.. autoexception:: versacord.ext.commands.ArgumentParsingError
    :members:

.. autoexception:: versacord.ext.commands.UnexpectedQuoteError
    :members:

.. autoexception:: versacord.ext.commands.InvalidEndOfQuotedStringError
    :members:

.. autoexception:: versacord.ext.commands.ExpectedClosingQuoteError
    :members:

.. autoexception:: versacord.ext.commands.BadArgument
    :members:

.. autoexception:: versacord.ext.commands.BadUnionArgument
    :members:

.. autoexception:: versacord.ext.commands.BadLiteralArgument
    :members:

.. autoexception:: versacord.ext.commands.PrivateMessageOnly
    :members:

.. autoexception:: versacord.ext.commands.NoPrivateMessage
    :members:

.. autoexception:: versacord.ext.commands.CheckFailure
    :members:

.. autoexception:: versacord.ext.commands.CheckAnyFailure
    :members:

.. autoexception:: versacord.ext.commands.CommandNotFound
    :members:

.. autoexception:: versacord.ext.commands.DisabledCommand
    :members:

.. autoexception:: versacord.ext.commands.CommandInvokeError
    :members:

.. autoexception:: versacord.ext.commands.TooManyArguments
    :members:

.. autoexception:: versacord.ext.commands.UserInputError
    :members:

.. autoexception:: versacord.ext.commands.CommandOnCooldown
    :members:

.. autoexception:: versacord.ext.commands.MaxConcurrencyReached
    :members:

.. autoexception:: versacord.ext.commands.NotOwner
    :members:

.. autoexception:: versacord.ext.commands.MessageNotFound
    :members:

.. autoexception:: versacord.ext.commands.MemberNotFound
    :members:
versacord.. autoexception:: versacord.ext.commands.GuildNotFound
    :members:

.. autoexception:: versacord.ext.commands.UserNotFound
    :members:

.. autoexception:: versacord.ext.commands.ChannelNotFound
    :members:

.. autoexception:: versacord.ext.commands.ScheduledEventNotFound
    :members:

.. autoexception:: versacord.ext.commands.ChannelNotReadable
    :members:

.. autoexception:: versacord.ext.commands.ThreadNotFound
    :members:

.. autoexception:: versacord.ext.commands.BadColourArgument
    :members:

.. autoexception:: versacord.ext.commands.RoleNotFound
    :members:

.. autoexception:: versacord.ext.commands.BadInviteArgument
    :members:

.. autoexception:: versacord.ext.commands.EmojiNotFound
    :members:

.. autoexception:: versacord.ext.commands.PartialEmojiConversionFailure
    :members:

.. autoexception:: versacord.ext.commands.GuildStickerNotFound
    :members:

.. autoexception:: versacord.ext.commands.BadBoolArgument
    :members:

.. autoexception:: versacord.ext.commands.MissingPermissions
    :members:

.. autoexception:: versacord.ext.commands.BotMissingPermissions
    :members:

.. autoexception:: versacord.ext.commands.MissingRole
    :members:

.. autoexception:: versacord.ext.commands.BotMissingRole
    :members:

.. autoexception:: versacord.ext.commands.MissingAnyRole
    :members:

.. autoexception:: versacord.ext.commands.BotMissingAnyRole
    :members:

.. autoexception:: versacord.ext.commands.NSFWChannelRequired
    :members:

.. autoexception:: versacord.ext.commands.FlagError
    :members:

.. autoexception:: versacord.ext.commands.BadFlagArgument
    :members:

.. autoexception:: versacord.ext.commands.MissingFlagArgument
    :members:

.. autoexception:: versacord.ext.commands.TooManyFlags
    :members:

.. autoexception:: versacord.ext.commands.MissingRequiredFlag
    :members:

.. autoexception:: versacord.ext.commands.ExtensionError
    :members:

.. autoexception:: versacord.ext.commands.ExtensionAlreadyLoaded
    :members:

.. autoexception:: versacord.ext.commands.ExtensionNotLoaded
    :members:

.. autoexception:: versacord.ext.commands.NoEntryPointError
    :members:

.. autoexception:: versacord.ext.commands.InvalidSetupArguments
    :members:

.. autoexception:: versacord.ext.commands.ExtensionFailed
    :members:

.. autoexception:: versacord.ext.commands.ExtensionNotFound
    :members:

.. autoexception:: versacord.ext.commands.CommandRegistrationError
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
