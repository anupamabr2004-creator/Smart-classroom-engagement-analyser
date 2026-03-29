import cv2
from detector import AttentionDetector
from scorer import calculate_class_attention
from logger import log_attention

def main():
    detector = AttentionDetector()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        scores = detector.detect_attention(frame)

        y = 30
        for idx, (score, status) in enumerate(scores):
            cv2.putText(
                frame,
                f"Student {idx+1}: {status} ({score})",
                (10, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
            y += 30

        class_score = calculate_class_attention(scores)
        log_attention(class_score)
        cv2.putText(
            frame,
            f"Class Attention: {class_score:.2f}",
            (10, 450),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

        cv2.imshow("Smart Classroom Analyzer", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()