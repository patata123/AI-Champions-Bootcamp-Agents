# Install with pip install firecrawl-py
import asyncio
from firecrawl import AsyncFirecrawlApp
from dotenv import load_dotenv
load_dotenv('.env')

async def main():
    app = AsyncFirecrawlApp()
    response = await app.scrape_url(
        url='https://www.mycareersfuture.gov.sg/search?search=auditor',		
        formats= [ 'markdown' ],
        only_main_content= True,
        parse_pdf= True,
    )
    print(response)

asyncio.run(main())