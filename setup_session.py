"""
Setup script for Lookonchain Telegram Bot
Run this ONCE locally to create session file
"""

import os
from telethon import TelegramClient
import asyncio

print("=" * 60)
print("Lookonchain Bot - First Time Setup")
print("=" * 60)
print()
print("This script will create a Telegram session file.")
print("You'll need to enter your phone number and verification code.")
print()

# Get credentials
api_id_input = input("Enter TELEGRAM_API_ID (from my.telegram.org): ").strip()
api_hash_input = input("Enter TELEGRAM_API_HASH (from my.telegram.org): ").strip()

try:
    api_id = int(api_id_input)
except ValueError:
    print("ERROR: API_ID must be a number!")
    exit(1)

if not api_hash_input:
    print("ERROR: API_HASH cannot be empty!")
    exit(1)

print()
print("Creating Telegram client...")

client = TelegramClient('lookonchain_session', api_id, api_hash_input)

async def main():
    print()
    print("=" * 60)
    print("TELEGRAM AUTHORIZATION")
    print("=" * 60)
    print()
    print("You will be asked to enter:")
    print("1. Your phone number (international format: +1234567890)")
    print("2. Verification code sent to Telegram")
    print("3. 2FA password (if enabled)")
    print()
    
    await client.start()
    
    print()
    print("=" * 60)
    print("✅ SUCCESS! Session created!")
    print("=" * 60)
    print()
    print("Files created:")
    print("  - lookonchain_session.session")
    print("  - lookonchain_session.session-journal (temporary)")
    print()
    print("=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print()
    print("1. COMMIT session file to Git:")
    print("   git add lookonchain_session.session")
    print("   git commit -m 'Add Telegram session file'")
    print("   git push")
    print()
    print("2. Add secrets to GitHub:")
    print("   - TELEGRAM_API_ID")
    print("   - TELEGRAM_API_HASH")
    print("   - OPENAI_API_KEY")
    print("   - TELEGRAM_BOT_TOKEN")
    print("   - TELEGRAM_CHAT_ID")
    print()
    print("3. Run workflow in GitHub Actions")
    print()
    print("=" * 60)
    print("⚠️  SECURITY NOTE:")
    print("=" * 60)
    print()
    print("The session file gives FULL ACCESS to your Telegram account.")
    print("Keep your repository PRIVATE!")
    print()
    print("To revoke access:")
    print("1. Go to Telegram Settings → Privacy & Security → Active Sessions")
    print("2. Terminate the 'lookonchain_session' session")
    print()
    
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
