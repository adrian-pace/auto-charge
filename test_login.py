import asyncio
from easee_api import get_easee_token_api
from config import settings

async def main():
    print(f"🕵️‍♂️ Testing API login for {settings.easee_email}...")
    try:
        tokens = await get_easee_token_api(settings.easee_email, settings.easee_password)
        print("\n🎉 Success! Got tokens.")
        print(f"🪙  Access Token: {tokens.get('accessToken')}")
        if 'refreshToken' in tokens:
            print()
            print(f"🔄 Refresh Token: {tokens.get('refreshToken')}")
    except Exception as e:
        print(f"💥 Failed with error: {e}")

if __name__ == "__main__":
    asyncio.run(main())

