# Class uses for payload customize.


class payload:
    def __init__(self, payloadTemplate, payloadData):
        self.payloadTemplate = payloadTemplate
        self.payloadData = payloadData

    # Because format to upload to rest API is the same json in payloadTemplate
    # Therefore, it the main function to create json before uploading
    def updatePayload(self, payloadBody):
        # All value below still keeping in default by getting current value
        # Just version_number needs to be updated +1 each time.
        self.payloadTemplate["version"]["number"] = (
            self.payloadData["version"]["number"] + 1
        )
        self.payloadTemplate["title"] = self.payloadData["title"]
        self.payloadTemplate["type"] = self.payloadData["type"]
        self.payloadTemplate["status"] = self.payloadData["status"]

        # payloadBody needs to be modified before uploading
        self.payloadTemplate["body"]["storage"]["value"] = f"{payloadBody}"
        return self.payloadTemplate
