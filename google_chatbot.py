import requests
import json
import warnings

warnings.filterwarnings(action="ignore")


def send_google_chat_notification(webhook_url: str, message: str):
    """
    You send a simple text message to a Google Chat space.
    """
    if not webhook_url or "https://chat.googleapis.com" not in webhook_url:
        print("❌ The Google Chat webhook URL is invalid. Please check the URL.")
        return

    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    message_data = {"text": message}

    try:
        response = requests.post(
            url=webhook_url,
            headers=message_headers,
            data=json.dumps(message_data),
            timeout=10,
        )
        response.raise_for_status()
        print("✅ Google Chat message sent successfully!")

    except requests.exceptions.RequestException as e:
        print(f"❌ Google Chat message send failed error: {e}")


if __name__ == "__main__":
    webhook_url = """https://chat.googleapis.com/v1/spaces/AAQA1Tn7uwU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=qGw7kWIBIv5wL5t_51Ug3ccSgPDFHvv4gF7JnPjTz68"""

    message = "Say YES!!!"

    send_google_chat_notification(webhook_url, message)
