import json
from PIL import Image, ImageDraw
import numpy as np

class LayoutToMaskNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "layout_json": ("STRING", {"multiline": True}),
                "canvas_width": ("INT", {"default": 512, "min": 256, "max": 2048}),
                "canvas_height": ("INT", {"default": 512, "min": 256, "max": 2048}),
                "block_size": ("INT", {"default": 64, "min": 10, "max": 512}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("layout_mask",)
    FUNCTION = "generate_mask"
    CATEGORY = "GlyphSync"

    def generate_mask(self, layout_json, canvas_width, canvas_height, block_size):
        mask = Image.new("L", (canvas_width, canvas_height), 0)
        draw = ImageDraw.Draw(mask)
        layout = json.loads(layout_json)
        for block in layout.get("text_blocks", []):
            x = int(block["position"][0] * canvas_width)
            y = int(block["position"][1] * canvas_height)
            left = x - block_size // 2
            top = y - block_size // 2
            right = x + block_size // 2
            bottom = y + block_size // 2
            draw.rectangle([left, top, right, bottom], fill=255)
        return (np.array(mask),)

NODE_CLASS_MAPPINGS = {
    "LayoutToMaskNode": LayoutToMaskNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LayoutToMaskNode": "GlyphSync – Layout to Mask"
}
