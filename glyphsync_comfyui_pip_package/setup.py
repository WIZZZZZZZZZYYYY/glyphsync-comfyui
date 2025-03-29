
from setuptools import setup, find_packages

setup(
    name="glyphsync-comfyui",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "Pillow",
        "easyocr"
    ],
    description="A ComfyUI custom node suite for prompt-to-layout text generation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="you@example.com",
    url="https://github.com/your-org/glyphsync-comfyui",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
