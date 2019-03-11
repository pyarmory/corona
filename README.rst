Corona
======

Corona is essentially a basic webpage screenshot utility that
uses headless Chromium via pyppeteer.

Running
-------

.. code-block:: shell


    # Download a version of Chromium to use
    corona setup

    # Take a snapshot
    corona snap https://google.com google.png


Extension
---------
The application allows for a couple of extension points via a python
script that follows this format:

.. code-block:: python


    async def pre_snapshot(page):
        # Do something awesome just before the
        # snapshot here

    async def post_snapshot(page):
        # Do something even more awesome after
        # the snapshot has been taken
