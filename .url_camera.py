from flask import Flask, render_template, Response
import cv2

app = Flask('test')

# camera_url = 'http://your-ip-camera-url/stream'
camera_url = 2
# Open the video capture with the IP camera URL
cap = cv2.VideoCapture(camera_url)

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='0.0.0.0', port=5000)
