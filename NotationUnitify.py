import inspect

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

asistant_id = "5788e9b9-7a2d-40de-9061-6fd5f9cb5f1b"
api_key = "nRfXCvsSGezvDNsRFgfJHDvA4BMOrHcJLN4jsE9sfOMo"
url = "https://api.us-south.assistant.watson.cloud.ibm.com/instances/50c7e745-79bd-45ab-b445-11b1a7ef1c87/v2/assistants/5788e9b9-7a2d-40de-9061-6fd5f9cb5f1b/sessions"
latest_version = "2020-04-01"

authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version=latest_version,
    authenticator=authenticator
)

assistant.set_service_url(url)

print(inspect.getmembers(assistant))

session_id = assistant.create_session(assistant_id=asistant_id).get_result()

print(json.dumps(session_id, indent=2))

assistant.delete_session(assistant_id, session_id["session_id"]).get_result()
