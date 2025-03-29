import numpy as np
import hashlib

class FontIntentEncoderNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style_prompt": ("STRING", {"multiline": False}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("font_embedding",)
    FUNCTION = "encode_font_style"
    CATEGORY = "GlyphSync"

    def encode_font_style(self, style_prompt):
        h = hashlib.sha256(style_prompt.encode()).digest()
        vec = np.frombuffer(h, dtype=np.uint8)[:64].astype(np.float32)
        vec = vec / np.linalg.norm(vec)
        return (vec.reshape(1, -1),)

NODE_CLASS_MAPPINGS = {
    "FontIntentEncoderNode": FontIntentEncoderNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FontIntentEncoderNode": "GlyphSync – Font Intent Encoder"
}
