from flask import Flask, request
import os
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Sample menu
menu = {
    "dosa": 60,
    "idly": 40,
    "burger": 40
}

UPI_ID = "sa7938@okhdfc"

@app.route("/webhook", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    if "menu" in incoming_msg or "order" in incoming_msg:
        menu_text = "\n".join([f"{item.title()} - ₹{price} each" for item, price in menu.items()])
        msg.body(f"Welcome to *Shubham's Kitchen*!\n\nHere's today's menu:\n{menu_text}\n\nTo order, just type what you want like:\n*2 Dosa and 1 Idly*")
    elif any(item in incoming_msg for item in menu):
        # Simple order detection
        total = 0
        order_summary = "Your Order Summary:\n"
        for item in menu:
            if item in incoming_msg:
                words = incoming_msg.split()
                qty = 1
                for i, word in enumerate(words):
                    if word == item:
                        try:
                            qty = int(words[i-1])
                        except:
                            qty = 1
                        break
                cost = menu[item
