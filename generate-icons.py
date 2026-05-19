#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def draw_logo(size, filename):
    # Create a new image with transparent background
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    padding = int(size * 0.15)
    content_size = size - padding * 2
    border_radius = int(size * 0.2)
    
    # Draw rounded square background
    draw.rounded_rectangle(
        [padding, padding, padding + content_size, padding + content_size],
        radius=border_radius,
        fill=(26, 26, 26, 255)  # #1a1a1a
    )
    
    # Draw "GG" text
    try:
        # Try to use a bold font
        font_size = int(size * 0.35)
        try:
            font = ImageFont.truetype('Arial Bold.ttf', font_size)
        except:
            try:
                font = ImageFont.truetype('Arial.ttf', font_size)
            except:
                # Fallback to default font
                font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    text = 'GG'
    
    # Calculate text position
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) / 2
    y = (size - text_height) / 2 - bbox[1]
    
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    
    # Save the image
    img.save(filename, 'PNG')
    print(f'Saved {filename}')

if __name__ == '__main__':
    # Generate icons
    draw_logo(180, 'apple-touch-icon.png')
    draw_logo(32, 'favicon-32x32.png')
    draw_logo(16, 'favicon-16x16.png')
    print('All icons generated successfully!')
