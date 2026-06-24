import cv2

aruco = cv2.aruco

# Load dictionary
dictionary = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)

# Create detector
detector = aruco.ArucoDetector(dictionary)

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame")
        break

    # Screen center
    height, width, _ = frame.shape
    frame_center_x = width // 2
    frame_center_y = height // 2

    # Blue dot at screen center
    cv2.circle(frame, (frame_center_x, frame_center_y), 5, (255, 0, 0), -1)

    # Detect markers
    corners, ids, rejected = detector.detectMarkers(frame)

    if ids is not None:

        # Draw marker box
        aruco.drawDetectedMarkers(frame, corners, ids)

        # Marker center
        c = corners[0][0]

        center_x = int((c[0][0] + c[2][0]) / 2)
        center_y = int((c[0][1] + c[2][1]) / 2)

        # Red dot at marker center
        cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

        # Green line (error vector)
        cv2.line(
            frame,
            (frame_center_x, frame_center_y),
            (center_x, center_y),
            (0, 255, 0),
            2
        )

        # Calculate error
        error_x = center_x - frame_center_x
        error_y = center_y - frame_center_y

        # Movement commands
        if abs(error_x) < 30 and abs(error_y) < 30:
            command = "LOCK ENGAGED"

        elif error_x > 30:
            command = "MOVE RIGHT"

        elif error_x < -30:
            command = "MOVE LEFT"

        elif error_y > 30:
            command = "MOVE up"

        else:
            command = "MOVE down"

        # Display command
        cv2.putText(
            frame,
            command,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    else:
        cv2.putText(
            frame,
            "TARGET LOST",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    cv2.imshow("ArUco Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()