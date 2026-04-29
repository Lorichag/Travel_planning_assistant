import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, subject, content):

    message = Mail(
        from_email='hagardloric@gmail.com',  # ⚠️ email vérifié sur SendGrid
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print("Email sent! Status:", response.status_code)
    except Exception as e:
        print("Error sending email:", e)

def format_travel_email(state):

    return f"""
    <h2>Your Travel Plan ✈️</h2>

    <p><b>Request:</b> {state.get("input")}</p>

    <h3>Plan:</h3>
    <p>{state.get("final")}</p>

    <p>Have a great trip! 🌍</p>
    """