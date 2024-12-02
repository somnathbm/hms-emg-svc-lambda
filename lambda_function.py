from utils.helper import create_new_emg_admission

def lambda_handler(event, context):
    queue_data = event[0]
    if not queue_data["messageId"] or not queue_data["body"]:
        raise Exception("corrupted event")
    msg_body: map = queue_data["body"]
    process_message(msg_body)

def process_message(message: map):
    try:
        print(f"Processed message {message}")
        # TODO: Do interesting work based on the new message
        return create_new_emg_admission(message["patient_id"])
    except Exception as err:
        print("An error occurred")
        raise err
