import paho.mqtt.client as mqtt
# import json


def on_message(client, userdata, msg):
    # try:
        payload = msg.payload.decode()
        # terminal_time = payload.get("_terminalTime", None)
        # group_name = payload.get("_groupName", None)
        # status = payload.get("STATUS", None)
        print(payload)

    #     if terminal_time is None or group_name is None:
    #         print(f"Missing required fields in message: {payload}")
    #         return
    #     # print(group_name)
    #     server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     group_name_arr = group_name.split("_")
    #     reg = group_name_arr[0]
    #     plant = group_name_arr[1]
    #     mach = group_name_arr[2]
    #     num = group_name_arr[3]
    #     del payload["_terminalTime"]
    #     del payload["_groupName"]
    #     if "STATUS" in payload:
    #         del payload["STATUS"]
    #     data = json.dumps(payload)
        
    #     # print("Data inserted")
    # except json.JSONDecodeError:
    #     print("Error decoding JSON from message payload.")
    # except Exception as e:
    #     print(f"Error processing message: {e}")


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    topics_mims = [
        "data/c5ea1d1b1c994db5/MIMS/01/+",
        "data/c5ea1d1b1c994db5/MIMS/02/+",
        "data/c5ea1d1b1c994db5/MIMS/03/+",
        "data/c5ea1d1b1c994db5/MIMS/04/+",
        "data/c5ea1d1b1c994db5/MIMS/05/+",
        "data/c5ea1d1b1c994db5/MIMS/06/+",
        "data/c5ea1d1b1c994db5/MIMS/07/+",
        "data/c5ea1d1b1c994db5/MIMS/08/+",
        "data/c5ea1d1b1c994db5/MIMS/09/+",
        "data/c5ea1d1b1c994db5/MIMS/10/+",
        "data/c5ea1d1b1c994db5/MIMS/11/+",
        "data/c5ea1d1b1c994db5/MIMS/12/+",
        "data/c5ea1d1b1c994db5/MIMS/13/+",
        "data/c5ea1d1b1c994db5/MIMS/14/+",
        "data/c5ea1d1b1c994db5/MIMS/15/+",
        "data/c5ea1d1b1c994db5/MIMS/16/+",
        "data/c5ea1d1b1c994db5/MIMS/17/+",
        "data/c5ea1d1b1c994db5/MIMS/18/+",
        "data/c5ea1d1b1c994db5/MIMS/19/+",
        "data/c5ea1d1b1c994db5/MIMS/20/+",
        "data/c5ea1d1b1c994db5/MIMS/21/+",
        "data/c5ea1d1b1c994db5/MIMS/22/+",
        "data/c5ea1d1b1c994db5/MIMS/23/+",
        "data/c5ea1d1b1c994db5/MIMS/24/+",
        "data/c5ea1d1b1c994db5/MIMS/25/+",
        "data/c5ea1d1b1c994db5/MIMS/26/+",
        "data/c5ea1d1b1c994db5/MIMS/27/+",
        "data/c5ea1d1b1c994db5/MIMS/28/+",
        "data/c5ea1d1b1c994db5/MIMS/29/+",
        "data/c5ea1d1b1c994db5/MIMS/30/+",
        "data/c5ea1d1b1c994db5/MIMS/31/+",
        "data/c5ea1d1b1c994db5/MIMS/32/+",
        "data/c5ea1d1b1c994db5/MIMS/33/+",
        "data/c5ea1d1b1c994db5/MIMS/34/+",
        "data/c5ea1d1b1c994db5/MIMS/35/+",
        "data/c5ea1d1b1c994db5/MIMS/36/+",
        "data/c5ea1d1b1c994db5/MIMS/37/+",
    ]
    topics_cmms = [
        "data/c5ea1d1b1c994db5/CMMS/01/+",
        "data/c5ea1d1b1c994db5/CMMS/02/+",
        "data/c5ea1d1b1c994db5/CMMS/03/+",
        "data/c5ea1d1b1c994db5/CMMS/04/+",
        "data/c5ea1d1b1c994db5/CMMS/05/+",
        "data/c5ea1d1b1c994db5/CMMS/06/+",
        "data/c5ea1d1b1c994db5/CMMS/07/+",
        "data/c5ea1d1b1c994db5/CMMS/08/+",
        "data/c5ea1d1b1c994db5/CMMS/09/+",
        "data/c5ea1d1b1c994db5/CMMS/10/+",
        "data/c5ea1d1b1c994db5/CMMS/11/+",
        "data/c5ea1d1b1c994db5/CMMS/12/+",
        "data/c5ea1d1b1c994db5/CMMS/13/+",
        "data/c5ea1d1b1c994db5/CMMS/14/+",
        "data/c5ea1d1b1c994db5/CMMS/15/+",
        "data/c5ea1d1b1c994db5/CMMS/16/+",
        "data/c5ea1d1b1c994db5/CMMS/17/+",
        "data/c5ea1d1b1c994db5/CMMS/18/+",
        "data/c5ea1d1b1c994db5/CMMS/19/+",
        "data/c5ea1d1b1c994db5/CMMS/20/+",
        "data/c5ea1d1b1c994db5/CMMS/21/+",
        "data/c5ea1d1b1c994db5/CMMS/22/+",
        "data/c5ea1d1b1c994db5/CMMS/23/+",
        "data/c5ea1d1b1c994db5/CMMS/24/+",
        "data/c5ea1d1b1c994db5/CMMS/25/+",
        "data/c5ea1d1b1c994db5/CMMS/26/+",
        "data/c5ea1d1b1c994db5/CMMS/27/+",
        "data/c5ea1d1b1c994db5/CMMS/28/+",
        "data/c5ea1d1b1c994db5/CMMS/29/+",
        "data/c5ea1d1b1c994db5/CMMS/30/+",
        "data/c5ea1d1b1c994db5/CMMS/31/+",
        "data/c5ea1d1b1c994db5/CMMS/32/+",
        "data/c5ea1d1b1c994db5/CMMS/33/+",
        "data/c5ea1d1b1c994db5/CMMS/34/+",
        "data/c5ea1d1b1c994db5/CMMS/35/+",
        "data/c5ea1d1b1c994db5/CMMS/36/+",
        "data/c5ea1d1b1c994db5/CMMS/37/+",
        "data/c5ea1d1b1c994db5/CMMS/38/+",
        "data/c5ea1d1b1c994db5/CMMS/39/+",
        "data/c5ea1d1b1c994db5/CMMS/40/+",
        "data/c5ea1d1b1c994db5/CMMS/41/+",
    ]
    topics = topics_mims + topics_cmms
    for topic in topics:
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("118.97.163.52", 1883, 60)
client.loop_forever()
