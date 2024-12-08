import nodriver as uc
import asyncio

url = 'https://free-proxy-list.net/'
async def scraper(retry_count = 0, max_retries = 5):
    driver = await uc.start()

    page = await driver.get(url)
    
    # count row
    row_count = await page.evaluate('document.querySelectorAll("table.table-striped tbody tr").length')
    print(f"Row count: {row_count}")

    if row_count == 0 or row_count is None:
        print(f"Data not found! Retrying {retry_count + 1}/{max_retries}")
        await page.close()

        if retry_count <= max_retries:
            await asyncio.sleep(2) # 2 seconds sleep before retrying
            return await scraper(retry_count=retry_count+1, max_retries=max_retries)
        else:
            return

    proxies_list = []

    for i in range(row_count):
        proxies = await page.evaluate(f'(document.querySelectorAll("table.table-striped tbody tr")[{i}].querySelector("td")).innerText')
        proxies_list.append(proxies)
    
    print(proxies_list)
       
    await page.close()
    return proxies_list

if __name__ == '__main__':
    try:
        asyncio.run(scraper())
    except Exception as e:
        print(f'An error occured: {e}')
