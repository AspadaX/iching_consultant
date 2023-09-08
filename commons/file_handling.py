from datetime import datetime
def save_response_to_file(response, file_name):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_file_name = f"outputs/{current_time}_{file_name}"
    with open(unique_file_name, "w") as f:
        f.write(response)