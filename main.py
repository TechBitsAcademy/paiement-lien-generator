import requests
import uuid

# Remplacez ces valeurs par vos propres informations
AMOUNT = 20000 # Montant du paiement dans la monnaie de votre compte Lygos
SHOP_NAME = "teste oki techbits aca"  # Nom de votre boutique
MESSAGE = "Contactez-nous sur WA pour toutes vos questions"
SUCCESS_URL = "https://facebook.com"  # URL de redirection en cas de succès (Optionnel)
FAILURE_URL = "https://gmail.com"  # URL de redirection en cas d'échec (Optionnel)
ORDER_ID = str(uuid.uuid4())  # Génération automatique d'un ID unique (Optionnel)

url = "https://api.lygosapp.com/v1/gateway"
payload = {
"amount": AMOUNT,
"shop_name": SHOP_NAME,
"message": MESSAGE,
"success_url": SUCCESS_URL,
"failure_url": FAILURE_URL,
"order_id": ORDER_ID
}
headers = {
"api-key": "lygosapp-94f7fdfc-66a8-4aec-af6f-800ce752cad0",
"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
payment_link = response.json().get("link")

print(f"Redirigez vos utilisateurs vers : {payment_link}")