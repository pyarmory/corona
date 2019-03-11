from pyppeteer import chromium_downloader


async def command(arguments):
    return chromium_downloader.download_chromium()
