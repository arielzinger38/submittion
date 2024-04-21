from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis
redis_host = "localhost"
redis_port = 6379
redis_db = 0
queue_name = "image_queue"
redis_conn = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

@app.route("/")
def process_queue():
    # Pop image ID from the queue
    image_id = redis_conn.blpop(queue_name)[1].decode('utf-8')
    print(f"Processing image with ID: {image_id}")

    # Fetch and analyze image (placeholder)
    analyze_image(image_id)
    return "Image processed successfully"

def analyze_image(image_id):
    # Placeholder for image analysis logic
    # Here you would fetch the image, analyze it, and print results
    print(f"Image size: 1024KB")
    print("Contains: Dog")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
