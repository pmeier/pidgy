"""__init__.py"""

"""pidgy literate computing frame"""

LOADED = False


def load_ipython_extension(shell):
    from . import tangle, weave

    shell.user_ns.setdefault("shell", shell)
    tangle.load_ipython_extension(shell)
    weave.load_ipython_extension(shell)


def unload_ipython_extension(shell):
    from . import tangle, weave

    tangle.unload_ipython_extension(shell)
    weave.unload_ipython_extension(shell)
