import easyocr
import numpy as np

class OCRValidatorNode:
    reader = easyocr.Reader(['en'], gpu=False)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "expected_text": ("STRING", {"multiline": True}),
                "similarity_threshold": ("FLOAT", {"default": 0.8, "min": 0.0, "max": 1.0}),
            }
        }

    RETURN_TYPES = ("STRING", "FLOAT")
    RETURN_NAMES = ("ocr_result", "similarity_score")
    FUNCTION = "validate"
    CATEGORY = "GlyphSync"

    def validate(self, image, expected_text, similarity_threshold):
        img = np.array(image).astype(np.uint8)
        results = self.reader.readtext(img)
        found_texts = " ".join([r[1] for r in results])
        matched_words = set(found_texts.lower().split()) & set(expected_text.lower().split())
        score = len(matched_words) / max(1, len(expected_text.split()))
        status = "PASS" if score >= similarity_threshold else "FAIL"
        return (f"{status}: {found_texts}", round(score, 3))

NODE_CLASS_MAPPINGS = {
    "OCRValidatorNode": OCRValidatorNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OCRValidatorNode": "GlyphSync – OCR Validator"
}
