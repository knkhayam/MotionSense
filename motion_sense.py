import cv2
import numpy as np
import time

# === CONFIG ===
MOTION_THRESHOLD = 20       # Flow strength threshold
MIN_AREA = 500              # Minimum area in pixels
TRIGGER_PERCENT = 20         # Motion % threshold to trigger alert
ALPHA = 0.6
BETA = 0.4

cap = cv2.VideoCapture('data/vid.mp4')
ret, prev = cap.read()
prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (5, 5), 0)

prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    total_pixels = h * w

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray,
                                        None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    motion_mask = np.uint8(cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX))

    motion_mask[motion_mask < MOTION_THRESHOLD] = 0
    motion_area = cv2.countNonZero(motion_mask)

    if motion_area < MIN_AREA:
        motion_mask[:] = 0

    # Check if motion exceeds percentage threshold
    motion_percent = (motion_area / total_pixels) * 100
    is_triggered = motion_percent >= TRIGGER_PERCENT

    heatmap = cv2.applyColorMap(motion_mask, cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(frame, ALPHA, heatmap, BETA, 0)

    # === Display FPS ===
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(overlay, f"FPS: {fps:.1f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # === Show "Trigger" if motion exceeds threshold ===
    if is_triggered:
        cv2.putText(overlay, "Trigger: " + str(round(motion_percent,2)) + "%", (w - 230, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        # Any Task to do here
        print("Trigger: " + str(round(motion_percent,2)) + "%")

    else:
        cv2.putText(overlay, str(round(motion_percent,2)) + "%", (w - 150, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    cv2.imshow("Motion Detection with Trigger", overlay)

    prev_gray = gray.copy()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()