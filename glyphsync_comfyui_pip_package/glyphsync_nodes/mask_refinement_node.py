import numpy as np
from PIL import Image, ImageFilter, ImageOps

class MaskRefinementNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask_image": ("IMAGE",),
                "blur_radius": ("INT", {"default": 2, "min": 0, "max": 20}),
                "invert": ("BOOLEAN", {"default": False}),
                "dilate": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("refined_mask",)
    FUNCTION = "refine_mask"
    CATEGORY = "GlyphSync"

    def refine_mask(self, mask_image, blur_radius, invert, dilate):
        mask = Image.fromarray(mask_image.squeeze().astype(np.uint8)).convert("L")
        if blur_radius > 0:
            mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
        if invert:
            mask = ImageOps.invert(mask)
        if dilate:
            mask = mask.filter(ImageFilter.MaxFilter(3))
        return (np.array(mask),)

NODE_CLASS_MAPPINGS = {
    "MaskRefinementNode": MaskRefinementNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MaskRefinementNode": "GlyphSync – Mask Refinement"
}
