# GlyphSync – Semantic Text-to-Layout Node Suite for ComfyUI 🖋️🎨

**GlyphSync** is a modular custom node pack for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that lets you generate images with **accurately rendered, semantically aligned text** — from prompt to layout to pixel-perfect output.

It brings structured design logic to text generation by turning natural language prompts into:
- 🧠 Layout blueprints (position, anchor, style)
- 🖼️ Spatial control masks for ControlNet
- 🖋️ Font embeddings from stylistic cues
- 🔍 OCR validation of text accuracy

---

## ✨ Features

✅ Prompt-to-layout parsing  
✅ Layout-to-mask rendering  
✅ Font intent encoding (vector)  
✅ Mask refinement (blur, dilation, invert)  
✅ OCR-based text verification  
✅ SDXL/Flux/ControlNet compatible  
✅ Plug-and-play in ComfyUI  

---

## 📦 Installation

### 🔌 As a ComfyUI Custom Node Pack
```bash
# Inside ComfyUI/custom_nodes/
git clone https://github.com/WIZZZZZZZZZYYYY/glyphsync-comfyui.git

Or manually copy the folder into:

ComfyUI/custom_nodes/glyphsync_nodes/

Then restart ComfyUI. Nodes will appear under the category: GlyphSync

⸻

📦 Pip install (for packaging or development)

pip install git+https://github.com/WIZZZZZZZZZYYYY/glyphsync-comfyui.git



⸻

🧩 Included Nodes

Node	Purpose
PromptToLayoutNode	Converts prompt into structured layout + preview
LayoutToMaskNode	Turns layout JSON into binary spatial mask
FontIntentEncoderNode	Embeds font style intent into a latent vector
MaskRefinementNode	Refines masks with blur/dilate/invert tools
OCRValidatorNode	Uses OCR to check if image text matches prompt



⸻

🧠 Example Prompt Flow

“Create a poster that says ‘Swim Before the Wave Hits’ in a bold futuristic font.”

This will:
	1.	Parse the layout (centered, large text)
	2.	Generate a spatial mask
	3.	Embed font style as a latent vector
	4.	Guide image generation via ControlNet + SDXL
	5.	Check output for text accuracy via OCR

⸻

🖼 Demo Workflow

Import glyphsync_demo_workflow.json into ComfyUI to test the full pipeline.

⸻

📄 Requirements
	•	Pillow
	•	numpy
	•	easyocr

Install via:

pip install -r requirements.txt



⸻

💡 Use Cases
	•	Poster generation
	•	Magazine covers
	•	Title-safe meme design
	•	Branded visuals
	•	UI/UX layout prototyping

⸻

📃 License

MIT – use it, remix it, make it yours.

⸻

Built with ❤️ by Zyr  – contributions welcome!
