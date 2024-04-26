import os
from dotenv import load_dotenv

load_dotenv()


class HighLevelConfig(object):
    CLIENT_ID = os.environ.get("GHL_API_V2_CLIENT_ID", None)
    CLIENT_SECRET = os.environ.get("GHL_API_V2_SECRET_KEY", None)
    API_BASE_URL = "https://services.leadconnectorhq.com"
    AUTH_BASE_URL = "https://marketplace.gohighlevel.com"
    VERSION = "2021-07-28"
    SCOPES = [
        "calendars/events.readonly",
        "contacts.readonly",
        "forms.readonly",
        "invoices.readonly",
        "locations.readonly",
        "opportunities.readonly",
        "surveys.readonly",
        "workflows.readonly",
        "businesses.readonly",
        "users.readonly",
        "companies.readonly",
        "calendars.readonly",
    ]
    REDIRECT_URI = "http://localhost:3000/oauth/callback"
