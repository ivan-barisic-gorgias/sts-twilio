"""
Deepgram Voice Agent configuration including prompt and function definitions.
"""

# System prompt for the AI agent
AGENT_PROMPT = """You are a helpful customer service AI assistant for an e-commerce company.

IMPORTANT: Before providing ANY order information or customer details, you MUST verify the caller's identity by asking them to provide ONE of the following:
- Their email address
- Their order number
- Their shipping address

Once you have collected this verification information, use the appropriate function to retrieve their data.

Only after successfully verifying their identity should you share order details, shipping information, or other personal data.

You can also help customers check product availability using the check_inventory function.

Be conversational, friendly, and helpful. If a customer asks about their order without providing verification details first, politely ask them to verify their identity before proceeding."""

# Function definitions for the agent
FUNCTION_DEFINITIONS = [
    {
        "name": "get_customer_by_email",
        "description": "Retrieve customer information by their email address. Use this to verify customer identity when they provide their email. Format the email in the correct format (e.g. first.last@example.com).",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The customer's email address"
                }
            },
            "required": ["email"]
        }
    },
    {
        "name": "get_customer_by_phone",
        "description": "Retrieve customer information by their phone number. Use this to verify customer identity when they provide their phone number.",
        "parameters": {
            "type": "object",
            "properties": {
                "phone": {
                    "type": "string",
                    "description": "The customer's phone number"
                }
            },
            "required": ["phone"]
        }
    },
    {
        "name": "get_order",
        "description": "Retrieve order information by order ID. Use this after verifying customer identity to look up their order details.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The unique order identifier"
                }
            },
            "required": ["order_id"]
        }
    },
    {
        "name": "check_inventory",
        "description": "Check if a product is in stock and get its availability. Use this when customers ask about product availability.",
        "parameters": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "The name of the product to check"
                }
            },
            "required": ["product_name"]
        }
    }
]

# Audio settings
AUDIO_SETTINGS = {
    "input": {
        "encoding": "mulaw",
        "sample_rate": 8000,
    },
    "output": {
        "encoding": "mulaw",
        "sample_rate": 8000,
        "container": "none",
    },
}

# Agent settings
AGENT_SETTINGS = {
    "language": "en",
    "listen": {
        "provider": {
            "type": "deepgram",
            "model": "nova-3",
            "keyterms": ["hello", "goodbye", "order", "email"]
        }
    },
    "think": {
        "provider": {
            "type": "open_ai",
            "model": "gpt-4.1-nano",
            "temperature": 0.5,
        },
        "functions": FUNCTION_DEFINITIONS,
        "prompt": AGENT_PROMPT
    },
    "speak": {
        "provider": {
            "type": "deepgram",
            "model": "aura-2-thalia-en"
        }
    },
    "greeting": "Hello! Thank you for calling. How can I help you today?"
}
