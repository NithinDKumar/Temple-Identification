import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def print_json(data, indent=0):
    for key, value in data.items():
        print(' ' * indent + f"{key}: {value}")
        if isinstance(value, dict):
            print_json(value, indent + 4)

def edit_json(data):
    while True:
        print("\nCurrent JSON data:")
        print_json(data)
        
        path = input("\nEnter the key path to edit (e.g., key1.key2.key3) or 'exit' to save and quit: ")
        if path.lower() == 'exit':
            break
        
        keys = path.split('.')
        temp_data = data
        for key in keys[:-1]:
            if key in temp_data:
                temp_data = temp_data[key]
            else:
                print(f"Key '{key}' not found.")
                break
        else:
            last_key = keys[-1]
            if last_key in temp_data:
                new_value = input(f"Enter the new value for {last_key}: ")
                try:
                    new_value = json.loads(new_value)
                except json.JSONDecodeError:
                    pass
                temp_data[last_key] = new_value
                print(f"Updated {last_key} to {new_value}.")
            else:
                print(f"Key '{last_key}' not found.")
    
    return data

if __name__ == "__main__":
    json_file_path = input("Enter the path to the JSON file: ")
    data = load_json(json_file_path)
    edited_data = edit_json(data)
    save_json(edited_data, json_file_path)
    print("Data has been updated and saved.")
##used this to create a jason file to edit, load , save