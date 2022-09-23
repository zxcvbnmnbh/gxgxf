import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "9198094"))
API_HASH = getenv("API_HASH", "5873984ba5ad6873afcb9b19df393dc9")
BOT_TOKEN = getenv("BOT_TOKEN", "5689290467:AAHGiki9FHMRnuoJUBNR06X8hHCs4VdmYQg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AgC96s0xVp8vLcSHUKMtG4C4W6ftveOO76d2pwjlOL71S5feAfY7xyGXvVEe5OaTJjmADUNqDenkL-ufFSND46kbt-XO_OeWJ5Y26es0lumk6P2X0KvF5IAr6_BZuo4eH6arfM0JsmS_1QO23aSaczlOSq-G-omqqN8O8_W7WBnv1v_m_5sIWcNnnW3zTqu0IWVHTy8QG7afUVE_KGxz7xMKRhrEKIDCA_Phc3DEEBvb74Ofcv4mpAbKZfq6wJjkvyW0KCht9MoJfeRmd5d3Q2nZemhEJ__uJ0vwwnsaURiltSInJk8OMjDcAVUgQnDl1b0tDCegsDuNtUU1EqEDdJn2AAAAAT9EPpQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
