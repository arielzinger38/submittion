from flask import Flask, request, jsonify
import os
import time
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_db = os.getenv('REDIS_DB', 0)
queue_name = os.getenv('QUEUE_NAME', 'image_queue')

# Connect to Redis
redis_conn = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the image locally
    file_path = os.path.join('./uploads', file.filename)
    file.save(file_path)

    # Push the image ID to the queue
    image_id = str(int(time.time()))
    redis_conn.rpush(queue_name, image_id)

    return jsonify({'message': 'File uploaded successfully', 'image_id': image_id})

if __name__ == '__main__':
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')
    app.run(host='0.0.0.0', port=5000)
