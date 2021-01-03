import os

values = {
    "googleProjectID":os.environ.get("GOOGLE_PROJECT_ID"),
    "dialogFlowSessionID":os.environ.get("DIALOGFLOW_SESSION_ID"),
    "dialogFlowSessionLanguageCode":os.environ.get("DIALOGFLOW_LANGUAGE_CODE")
}