import logging
from typing import Dict

import httpx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_easee_token_api(email: str, password: str) -> Dict:
    """Authenticate using the official Easee Developer API."""
    auth_url = "https://api.easee.com/api/accounts/login"
    
    async with httpx.AsyncClient() as client:
        logger.info("Initiating API login flow...")
        payload = {
            "userName": email,
            "password": password
        }
        
        response = await client.post(auth_url, json=payload)
        
        if response.status_code != 200:
            logger.error("API login failed: %s", response.text)
            response.raise_for_status()
            
        logger.info("API Tokens successfully acquired.")
        return response.json()

async def start_charging(access_token: str, charger_id: str):
    """Send the start charging command to the Easee API."""
    url = f"https://api.easee.com/api/chargers/{charger_id}/commands/start_charging"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        logger.info("Sending start_charging command to charger %s...", charger_id)
        # Some command endpoints in Easee API just require a POST with empty body
        response = await client.post(url, headers=headers)
        
        if response.status_code not in (200, 202):
            logger.error("Failed to start charging: %s", response.text)
            response.raise_for_status()
            
        logger.info("Successfully sent start charging command!")
        return response.json() if response.text else {}

async def stop_charging(access_token: str, charger_id: str):
    """Send the stop charging command to the Easee API."""
    url = f"https://api.easee.com/api/chargers/{charger_id}/commands/stop_charging"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        logger.info("Sending stop_charging command to charger %s...", charger_id)
        # Some command endpoints in Easee API just require a POST with empty body
        response = await client.post(url, headers=headers)
        
        if response.status_code not in (200, 202):
            logger.error("Failed to stop charging: %s", response.text)
            response.raise_for_status()
            
        logger.info("Successfully sent stop charging command!")
        return response.json() if response.text else {}