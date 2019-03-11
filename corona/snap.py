import collections
import os
import importlib

import pyppeteer


async def command(arguments):
    if not pyppeteer.chromium_downloader.check_chromium():
        print('Browser has not been setup. Please run "corona setup"')

    pyscript = await load_ext_pyscript(arguments)

    browser = await pyppeteer.launch(headless=True)
    page = await browser.newPage()

    if arguments.auth_username and arguments.auth_password:
        await page.authenticate({
            'username': arguments.auth_username,
            'password': arguments.auth_password
        })

    await page.goto(arguments.url)
    await page.setViewport({
        'width': arguments.viewport_width,
        'height': arguments.viewport_height,
    })

    if pyscript and pyscript.pre_snapshot:
        await pyscript.pre_snapshot(page)

    await page.screenshot(path=arguments.filename)

    if pyscript and pyscript.post_snapshot:
        await pyscript.post_snapshot(page)

    await browser.close()


async def load_ext_pyscript(arguments):
    if not arguments.pyscript or not os.path.exists(arguments.pyscript):
        return

    loader = importlib.machinery.SourceFileLoader('pyscript', arguments.pyscript)
    module = loader.load_module()

    PyScript = collections.namedtuple('PyScript', ['pre_snapshot', 'post_snapshot'])

    return PyScript(
        pre_snapshot=getattr(module, 'pre_snapshot', None),
        post_snapshot=getattr(module, 'post_snapshot', None),
    )
