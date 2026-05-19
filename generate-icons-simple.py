#!/usr/bin/env python3
import os
import struct
import zlib

def create_png(width, height, data, filename):
    # PNG signature
    png = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    png += chunk(b'IHDR', ihdr)
    
    # IDAT chunk
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'  # filter type
        raw_data += data[y * width * 4 : (y + 1) * width * 4]
    compressed = zlib.compress(raw_data, 9)
    png += chunk(b'IDAT', compressed)
    
    # IEND chunk
    png += chunk(b'IEND', b'')
    
    with open(filename, 'wb') as f:
        f.write(png)

def chunk(type, data):
    return struct.pack('>I', len(data)) + type + data + struct.pack('>I', zlib.crc32(type + data) & 0xffffffff)

def draw_logo(size, filename):
    # Create RGBA data
    data = bytearray(size * size * 4)
    padding = int(size * 0.15)
    content_size = size - padding * 2
    border_radius = int(size * 0.2)
    
    for y in range(size):
        for x in range(size):
            idx = (y * size + x) * 4
            
            # Check if inside rounded square
            in_rect = (padding <= x < padding + content_size and 
                       padding <= y < padding + content_size)
            
            if in_rect:
                # Check corners
                cx, cy = x - padding, y - padding
                
                # Check which corner we're in
                in_corner = False
                if cx < border_radius and cy < border_radius:
                    # Top-left
                    dx, dy = cx - border_radius, cy - border_radius
                    if dx * dx + dy * dy > border_radius * border_radius:
                        in_corner = True
                elif cx >= content_size - border_radius and cy < border_radius:
                    # Top-right
                    dx, dy = cx - (content_size - border_radius), cy - border_radius
                    if dx * dx + dy * dy > border_radius * border_radius:
                        in_corner = True
                elif cx < border_radius and cy >= content_size - border_radius:
                    # Bottom-left
                    dx, dy = cx - border_radius, cy - (content_size - border_radius)
                    if dx * dx + dy * dy > border_radius * border_radius:
                        in_corner = True
                elif cx >= content_size - border_radius and cy >= content_size - border_radius:
                    # Bottom-right
                    dx, dy = cx - (content_size - border_radius), cy - (content_size - border_radius)
                    if dx * dx + dy * dy > border_radius * border_radius:
                        in_corner = True
                
                if not in_corner:
                    # Inside the rounded square - dark gray
                    data[idx] = 26   # R
                    data[idx + 1] = 26  # G
                    data[idx + 2] = 26  # B
                    data[idx + 3] = 255 # A
                    
                    # Check if we should draw "GG"
                    # For simplicity, we'll just have the background, the text is hard to do without PIL
                else:
                    # Transparent
                    data[idx] = 0
                    data[idx + 1] = 0
                    data[idx + 2] = 0
                    data[idx + 3] = 0
            else:
                # Transparent
                data[idx] = 0
                data[idx + 1] = 0
                data[idx + 2] = 0
                data[idx + 3] = 0
    
    create_png(size, size, data, filename)
    print(f'Saved {filename}')

if __name__ == '__main__':
    # Generate icons
    draw_logo(180, 'apple-touch-icon.png')
    draw_logo(32, 'favicon-32x32.png')
    draw_logo(16, 'favicon-16x16.png')
    print('All icons generated successfully!')
