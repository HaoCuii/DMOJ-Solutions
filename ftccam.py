# Windows + OpenCV via FFmpeg(dshow). Press q to quit.
import os, cv2
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "input_format;dshow"
cap = cv2.VideoCapture("video=Live Streamer CAM 313", cv2.CAP_FFMPEG)
if not cap.isOpened(): raise SystemExit("CAM 313 not found (FFmpeg+dshow)")
while True:
    ok, f = cap.read()
    if not ok: break
    cv2.imshow("Live Streamer CAM 313", f)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release(); cv2.destroyAllWindows()
