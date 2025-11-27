
"""
Problemstellung:
Wenn zwei inkompatible Schnittstellen zusammenarbeiten müssen, kann das Adapter-Muster verwendet werden, 
um eine Brücke zwischen ihnen zu schlagen. 
Hier ist ein einfaches Beispiel, das zeigt, wie ein E-Mail-Dienst an eine einheitliche Schnittstelle angepasst werden kann.
Der Adapter übersetzt deine interne Schnittstelle in die des externen Systems.

Bsp. Einsatzszenario:
Du hast verschiedene E-Mail-Dienste (z.B. SMTP, SendGrid, etc.), die unterschiedliche Schnittstellen haben.
Du möchtest jedoch eine einheitliche Schnittstelle in deinem Code verwenden, um E-Mails zu senden.
"""

# ===== Einheitliche Schnittstelle für einen E-Mail-Dienst =====
class EmailService:
    def send_email(self, to, subject, body):
        raise NotImplementedError()
    
# ===== Drittanbieter-E-Mail-Dienst =====
class ThirdPartyMailer:
    def send(self, payload: dict):
        print("Sende über externes System:", payload)

# ===== Adapter, der die Drittanbieter-Schnittstelle anpasst =====
"""
Der Adapter übernimmt die Umbennung und Umstrukturierung der Daten, sodass sie mit der einheitlichen Schnittstelle kompatibel sind.
- Umbenennung der Parameter
- Anpassung des Datenformats (Dictionary)
- Aufruf der Drittanbieter-API
"""
class ThirdPartyMailerAdapter(EmailService):
    def __init__(self, client: ThirdPartyMailer):
        self.client = client

    def send_email(self, to, subject, body):
        payload = {
            "recipient": to,
            "title": subject,
            "content": body
        }
        self.client.send(payload)

# ===== Client Code =====
if __name__ == "__main__":
    third_party_mailer = ThirdPartyMailer()
    email_service = ThirdPartyMailerAdapter(third_party_mailer)

    email_service.send_email(
        to="test@example.com",
        subject="Hallo",
        body="Das ist eine Testmail."
    )