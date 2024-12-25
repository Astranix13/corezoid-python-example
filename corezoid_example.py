import json

def handle(params):
    # Перевіряємо, чи є параметри
    if not params:
        return {"error": "No parameters provided."}
    
    # Ваш код для обробки параметрів
    result = {key: f"Processed {value}" for key, value in params.items()}
    
    return result

if __name__ == "__main__":
    # Пример обробки запиту
    request_body = '{"jsonrpc": "2.0", "method": "handle", "id": "1", "params": {"key1": "value1", "key2": "value2"}}'
    
    # Парсимо запит
    request_data = json.loads(request_body)
    
    # Викликаємо метод
    if request_data["method"] == "handle":
        response = handle(request_data["params"])
        
        # Формуємо відповідь
        response_body = json.dumps({
            "jsonrpc": "2.0",
            "id": request_data["id"],
            "result": response
        })
        
        print(response_body)
