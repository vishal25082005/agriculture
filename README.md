# 🌱 Edge–Cloud Smart Agriculture Infrastructure

A cloud-native IoT solution that integrates **ESP32**, **AWS IoT Core**, **AWS Lambda**, **Amazon EC2**, **Amazon DynamoDB**, **Amazon S3**, and **MQTT** to enable real-time environmental monitoring and intelligent irrigation. The system combines edge computing with cloud processing to provide a scalable, secure, and reliable smart agriculture platform capable of operating even during network outages.

---

## 📖 Overview

The Edge–Cloud Smart Agriculture Infrastructure is designed to automate agricultural monitoring and irrigation using IoT and AWS cloud technologies. Environmental data is collected through ESP32-connected sensors and securely transmitted to AWS IoT Core using MQTT. AWS Lambda processes incoming sensor data, which is stored in Amazon DynamoDB for real-time analytics and Amazon S3 for long-term storage. A Dockerized Flask dashboard hosted on Amazon EC2 provides live monitoring, while Amazon SNS sends instant notifications whenever abnormal environmental conditions are detected.

To ensure uninterrupted operation, the ESP32 performs local irrigation control by activating the relay whenever soil moisture falls below a predefined threshold, allowing the system to continue functioning even during temporary cloud or network failures.

---

## ✨ Features

- 🌱 Real-time soil moisture monitoring
- 🌡️ Temperature and humidity monitoring using DHT11
- ☀️ Ambient light monitoring using LDR sensor
- 💧 Automatic irrigation using relay-controlled water pump
- ☁️ Hybrid Edge–Cloud architecture
- 📡 Secure MQTT communication with AWS IoT Core
- ⚡ Serverless event processing using AWS Lambda
- 📊 Live monitoring dashboard hosted on Amazon EC2
- 🗄️ Real-time sensor data storage using Amazon DynamoDB
- 📁 Long-term storage using Amazon S3
- 🔔 Instant alerts using Amazon SNS
- 🐳 Dockerized Flask application deployment
- 🔒 Secure cloud infrastructure using AWS IAM
- 🌐 Continuous operation during internet outages

---

# 🏗️ System Architecture

<p align="center">
  <img src="architecture/architecture.png" alt="Edge Cloud Smart Agriculture Architecture" width="900">
</p>

---

## 🔄 Project Workflow

1. ESP32 collects temperature, humidity, soil moisture, and light intensity from connected sensors.
2. Sensor readings are securely transmitted to **AWS IoT Core** using the **MQTT protocol**.
3. The **AWS IoT Core Rules Engine** routes incoming messages to **AWS Lambda**.
4. AWS Lambda validates and processes sensor data.
5. Processed sensor readings are stored in **Amazon DynamoDB** for real-time access.
6. Historical reports and supporting files are archived in **Amazon S3**.
7. A **Dockerized Flask dashboard** hosted on **Amazon EC2** retrieves sensor data and displays live environmental conditions.
8. **Amazon SNS** sends email notifications whenever abnormal conditions are detected.
9. During network interruptions, the **ESP32 autonomously controls irrigation**, ensuring uninterrupted operation.

---

# ☁️ AWS Services Used

| Service | Purpose |
|----------|---------|
| AWS IoT Core | Secure MQTT communication with ESP32 |
| AWS Lambda | Serverless sensor data processing |
| Amazon DynamoDB | Real-time sensor data storage |
| Amazon S3 | Long-term storage of reports and files |
| Amazon EC2 | Hosting Flask monitoring dashboard |
| Amazon SNS | Email notifications and alerts |
| AWS IAM | Identity and access management |

---

# 🛠️ Technology Stack

### Cloud
- AWS IoT Core
- Amazon EC2
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Amazon SNS
- AWS IAM

### IoT & Hardware
- ESP32
- MQTT
- DHT11 Sensor
- Soil Moisture Sensor
- LDR Sensor
- Relay Module
- Water Pump

### Backend
- Python
- Flask

### DevOps
- Docker
- Git
- Linux

---

# 🔌 Hardware Components

- ESP32 Development Board
- DHT11 Temperature & Humidity Sensor
- Soil Moisture Sensor
- LDR Sensor
- Relay Module
- Water Pump
- Breadboard
- Jumper Wires
- Wi-Fi Network

---

# 📂 Repository Structure

```
Edge-Cloud-Smart-Agriculture/
│
├── architecture/
│   └── architecture.png
│
├── esp32/
│   ├── smart_agriculture.ino
│   └── mqtt_config.h
│
├── lambda/
│   └── lambda_function.py
│
├── flask_app/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── requirements.txt
│
├── docker/
│   └── Dockerfile
│
├── screenshots/
│   ├── hardware_setup.png
│   ├── dashboard.png
│   ├── dynamodb_table.png
│   ├── aws_console.png
│   └── sns_email.png
│
├── README.md
└── requirements.txt
```

---

# 📸 Screenshots

## Hardware Setup

> Add an image of your ESP32 hardware setup.

---

## AWS Architecture

> Add the architecture diagram.

---

## Flask Dashboard

> Add your dashboard screenshot.

---

## DynamoDB Table

> Add a screenshot of stored sensor data.

---

## Amazon SNS Alert

> Add a screenshot of the email notification.

---

# 🚀 Future Enhancements

- 📱 Mobile application for farmers
- 🤖 AI-based irrigation prediction
- 🌦️ Weather API integration
- 🌾 Crop health prediction
- 🌍 Multi-farm monitoring
- 📈 AWS CloudWatch analytics
- 🔄 OTA firmware updates
- 📊 Historical trend visualization

---

# 📚 Skills Demonstrated

- Internet of Things (IoT)
- Edge Computing
- Cloud Computing
- AWS IoT Core
- AWS Lambda
- Amazon EC2
- Amazon DynamoDB
- Amazon S3
- Amazon SNS
- MQTT Protocol
- Flask
- Docker
- Python
- ESP32
- Embedded Systems
- Cloud-Native Application Development

---

# 👨‍💻 Author

**Vishal M**

Cloud & IoT Engineer

B.Tech – Electronics & Communication Engineering

📧 **Email:** vishal.md2508@gmail.com

💼 **LinkedIn:** https://linkedin.com/in/YOUR-LINKEDIN

💻 **GitHub:** https://github.com/YOUR-GITHUB

---

## ⭐ If you found this project interesting, consider giving it a Star!
