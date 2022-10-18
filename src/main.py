from core.config import *
from core.API_interaction import api_interaction
from core.payload import payload
from core.valueBody import valueBody

if __name__ == "__main__":
    # Init class API
    API_interact = api_interaction()

    # Get current content without ValueBody
    PayloadData = API_interact.get()

    # Get current content and valueBody without Version_number
    getValueBody = API_interact.get(custom_URL)
    payloadBody = getValueBody["body"]["storage"]["value"]

    # Init class payload
    Payload = payload(payloadTemplate, PayloadData)

    # Update Value Body
    for run_time in range(from_table, to_table + 1):
        # Get variables from config.py
        # try except uses when user input to_table larger than they have
        try:
            column = getVars[f"table_{run_time}"]["first_column"]
            header = getVars[f"table_{run_time}"]["header"]
            replaceStr = getVars[f"table_{run_time}"]["replace_with"]
        except KeyError:
            print(f"There are no table_{run_time} => STOP")
            break

        # Init class valueBody
        valueBody_handle = valueBody(payloadBody, run_time)
        findStr = valueBody_handle.findString(column, header)
        newPayloadBody = valueBody_handle.replaceString(replaceStr)
        # Format payloadBody to html type
        newPayloadBody.prettify(formatter="html")
        # Update new HTML content
        payloadBody = newPayloadBody

    # Update payload template
    PayloadUpdated = Payload.updatePayload(newPayloadBody)
    print(PayloadUpdated)
    submitPayload = API_interact.update(PayloadUpdated)
    print(submitPayload)
