import streamlit as st
import cv2
from PIL import Image

def main():
    # Set page title and description
    st.title("Webcam Image Capture")
    st.write("Click the button below to capture an image from your webcam.")

    # Add a button to capture image
    if st.button("Capture Image"):
        # Open webcam
        video_capture = cv2.VideoCapture(0)

        # Check if webcam opened successfully
        if not video_capture.isOpened():
            st.error("Error: Failed to open webcam.")
            return

        # Read frame from webcam
        ret, frame = video_capture.read()

        # Release webcam
        video_capture.release()

        # Convert frame to PIL Image
        pil_image = Image.fromarray(frame)

        # Display captured image
        st.image(pil_image, caption='Captured Image', use_column_width=True)

if __name__ == "__main__":
    main()
