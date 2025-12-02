import json
import boto3
import time

s3 = boto3.client("s3")
sns = boto3.client("sns")

BUCKET = "agriculture"
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:SmartAgriAlerts"

def lambda_handler(event, context):

    # Extract sensor data
    message = event["Records"][0]["Sns"]["Message"]
    data = json.loads(message)

    temp = float(data["temperature"])
    soil = int(data["soil"])
    light = int(data["light"])

    # Motor logic
    motor_status = "OFF"
    if soil > 3000:     # Very dry
        motor_status = "ON"

    payload = {
        "temperature": temp,
        "soil": soil,
        "light": light,
        "motor_status": motor_status,
        "timestamp": int(time.time())
    }

    # Upload to S3
    s3.put_object(
        Bucket=BUCKET,
        Key="latest.json",
        Body=json.dumps(payload),
        ContentType="application/json"
    )

    # Trigger SNS alert
    if soil > 3000:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="🚨 SmartAgri Alert!",
            Message=f"Soil too dry! Moisture: {soil} → Motor ON 🚜"
        )

    return {"status": "success", "data": payload}

