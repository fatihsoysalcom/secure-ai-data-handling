import json

def encrypt_data(data, key):
    """Simulates data encryption for privacy."""
    # In a real-world scenario, use a robust encryption library like 'cryptography'
    # This is a placeholder to illustrate the concept of data transformation.
    encrypted_data = []
    for item in data:
        encrypted_item = {}
        for k, v in item.items():
            # Simple XOR-like transformation for demonstration
            transformed_v = ''.join(chr(ord(c) ^ key) for c in str(v))
            encrypted_item[k] = transformed_v
        encrypted_data.append(encrypted_item)
    return encrypted_data

def anonymize_data(data):
    """Simulates data anonymization by masking sensitive fields."""
    # In a real-world scenario, use more sophisticated anonymization techniques.
    anonymized_data = []
    for item in data:
        anonymized_item = item.copy()
        # Masking sensitive fields like 'email' and 'phone'
        if 'email' in anonymized_item:
            anonymized_item['email'] = '***@example.com'
        if 'phone' in anonymized_item:
            anonymized_item['phone'] = 'XXX-XXX-XXXX'
        anonymized_data.append(anonymized_item)
    return anonymized_data

def process_with_ai(processed_data):
    """Simulates sending processed data to an AI model."""
    # This function represents the interaction with the AI model.
    # The data passed here is already secured (encrypted/anonymized).
    print("\n--- Sending processed data to AI model ---")
    print(json.dumps(processed_data, indent=2))
    print("--- AI model processing complete ---")
    # In a real AI scenario, the model would return insights or results.
    return {"insight": "User behavior analysis complete."}

if __name__ == "__main__":
    # Sample sensitive user data
    user_data = [
        {"id": 1, "name": "Alice", "email": "alice@example.com", "phone": "123-456-7890", "preferences": "AI, Tech"},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "phone": "987-654-3210", "preferences": "Data Science, ML"}
    ]

    print("--- Original User Data ---")
    print(json.dumps(user_data, indent=2))

    # Step 1: Anonymize data before any processing
    anonymized_user_data = anonymize_data(user_data)
    print("\n--- Anonymized User Data ---")
    print(json.dumps(anonymized_user_data, indent=2))

    # Step 2: Encrypt data (e.g., for secure transmission or storage before AI processing)
    # Using a simple integer key for demonstration. In practice, use strong cryptographic keys.
    encryption_key = 42
    encrypted_user_data = encrypt_data(anonymized_user_data, encryption_key)
    print("\n--- Encrypted User Data ---")
    print(json.dumps(encrypted_user_data, indent=2))

    # Step 3: Process the secured data with the AI model
    # The AI model receives data that has undergone privacy-preserving steps.
    ai_result = process_with_ai(encrypted_user_data)
    print("\n--- AI Model Result ---")
    print(ai_result)

    # Note: Decryption would be needed to access original data later, using the same key.
    # For this example, we focus on the secure processing pipeline.
