from core.readJson import readJson

# File config for this project
# Get value from json file (./setup/vars.json)
getValueJson = readJson()
varsFile = "./setup/vars.json"
getVars = getValueJson.getJson(varsFile)
APIkey = getVars["API_key"]
confluenceURL = getVars["confluence_URL"]
pageID = getVars["page_ID"]
from_table = getVars["from_table"]
to_table = getVars["to_table"]

# headers for API_interact
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {APIkey}",
}
url = f"{confluenceURL}/rest/api/content/{pageID}"

# custom_URL uses for getting only valueBody.
custom_URL = f"{url}?expand=body.storage"

# get value in json payload template
payloadPath = "./src/payloadTemplate/payload.json"
payloadTemplate = getValueJson.getJson(payloadPath)
