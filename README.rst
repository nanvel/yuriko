yuriko
======

Encrypted notes.

Setup
-----

.. code-block:: bash

    pip install yuriko

Set environment variable `YURIKO_DB_PATH` to path to where the database will be located
(it can be created with `init` if not exist).

One way is to use `~/.bash_profile`:

.. code-block:: bash

    vim ~/.bash_profile
    // add `export YURIKO_DB_PATH=/some/path`
    source ~/.bash_profile

Also there is `YURIKO_PASSWORD_SUFFIX` environment variable.
AES key = `(password entered + YURIKO_PASSWORD_SUFFIX)[:16]`, so password to enter can be a bit shorter.

Usage
-----

.. code-block:: bash

    yuriko init
    yuriko search <q prefix>
    yuriko open <key>
    yuriko del <key>