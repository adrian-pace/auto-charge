import logging
from fastapi import FastAPI, HTTPException
from easee_api import get_easee_token_api, start_charging, stop_charging
from config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/start-charge/")
async def start_charge_endpoint():
    try:
        tokens = await get_easee_token_api(settings.easee_email, settings.easee_password)
        accessToken = tokens.get("accessToken")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    try:
        await start_charging(accessToken, settings.easee_charger_id)
        return {"message": "Charging started successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/stop-charge/")
async def stop_charge_endpoint():
    try:
        tokens = await get_easee_token_api(settings.easee_email, settings.easee_password)
        accessToken = tokens.get("accessToken")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    try:
        await stop_charging(accessToken, settings.easee_charger_id)
        return {"message": "Charging stopped successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
