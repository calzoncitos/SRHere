import cv2
import numpy as np
from PIL import Image

def remove_background(input_path: str, output_path: str = None) -> str:
    """
    Remove background from an image using OpenCV.
    
    Args:
        input_path: Path to input image
        output_path: Path for output image (optional)
    """
    try:
        # Read image
        img = cv2.imread(input_path)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Threshold
        _, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
        
        # Create mask
        mask = thresh.copy()
        mask = cv2.GaussianBlur(mask, (5,5), 0)
        
        # Apply mask to original image
        result = cv2.bitwise_and(img, img, mask=mask)
        
        # Convert to RGBA
        b, g, r = cv2.split(result)
        alpha = mask
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)
        
        # Save output
        if output_path is None:
            output_path = input_path.rsplit('.', 1)[0] + '_nobg.png'
            
        cv2.imwrite(output_path, dst)
        print(f"Background removed successfully. Saved to: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

# Example usage
if __name__ == "__main__":
    remove_background("assets/srh_logo.png")
    
    # Process multiple images
    images = [
        "assets/cube.jpeg",
        "assets/srh_rectangle.png"
    ]
    
    for img in images:
        remove_background(img) 