from flask import Flask, render_template, jsonify
import boto3
import json

app = Flask(__name__)
s3 = boto3.client("s3")
BUCKET = "agriculture"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/latest")
def latest():
    obj = s3.get_object(Bucket=BUCKET, Key="latest.json")
    data = json.loads(obj["Body"].read().decode("utf-8"))
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

