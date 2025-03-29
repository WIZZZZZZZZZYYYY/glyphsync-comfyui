import json
from typing import Any, Dict
from PIL import Image, ImageDraw, ImageFont
import numpy as np

class PromptToLayoutNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "IMAGE")
    RETURN_NAMES = ("layout_json", "layout_preview")
    FUNCTION = "process_prompt"
    CATEGORY = "GlyphSync"

    def process_prompt(self, prompt: str):
        layout = {
            "text_blocks": [
                {
                    "text": prompt.strip().strip('"'),
                    "position": [0.25, 0.4],
                    "font": "bold_neon",
                    "size": "large",
                    "anchor": "center"
                }
            ]
        }
        layout_json = json.dumps(layout, indent=2)
        image = self.render_layout_preview(layout)
        return (layout_json, image)

    def render_layout_preview(self, layout: Dict[str, Any]) -> Image.Image:
        W, H = 512, 512
        img = Image.new("RGB", (W, H), (20, 20, 20))
        draw = ImageDraw.Draw(img)
        for block in layout.get("text_blocks", []):
            text = block["text"]
            x = int(block["position"][0] * W)
            y = int(block["position"][1] * H)
            try:
                font = ImageFont.truetype("arial.ttf", 28)
            except:
                font = ImageFont.load_default()
            draw.text((x, y), text, font=font, fill=(255, 255, 255), anchor="mm")
        return np.array(img)

NODE_CLASS_MAPPINGS = {
    "PromptToLayoutNode": PromptToLayoutNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptToLayoutNode": "GlyphSync – Prompt to Layout"
}
