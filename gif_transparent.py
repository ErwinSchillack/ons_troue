from PIL import Image

def make_gif_background_transparent(input_gif_path, output_gif_path, background_color=(255, 255, 255)):
    """
    Converts the specified background color of a GIF to transparent and saves the new GIF.
    
    :param input_gif_path: Path to the input GIF file.
    :param output_gif_path: Path where the output GIF with transparent background should be saved.
    :param background_color: A tuple specifying the background color to make transparent. Default is white.
    """
    # Open the input GIF
    with Image.open(input_gif_path) as img:
        # Create a list to hold the frames of the new GIF
        frames = []

        # Iterate through each frame of the GIF
        print( img.n_frames)
        for frame in range(0, img.n_frames):
            img.seek(frame)
            # Convert the image to RGBA if not already
            rgba_frame = img.convert("RGBA")
            
            # Create a new image with transparent background
            transparent_frame = Image.new("RGBA", rgba_frame.size, (0, 0, 0, 0))
            
            # Paste the current frame onto the transparent image, omitting the specified background color
            transparent_frame.paste(rgba_frame, mask=rgba_frame)
            
            # Replace all pixels that match the background color with transparency
            datas = transparent_frame.getdata()
            newData = []
            for item in datas:
                # Change all pixels that match background_color to transparent
                if item[0] == background_color[0] and item[1] == background_color[1] and item[2] == background_color[2]:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            
            transparent_frame.putdata(newData)
            frames.append(transparent_frame)

        # Save the frames as a new GIF
        frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], loop=0, transparency=0)

# Example usage
make_gif_background_transparent(r'C:\Users\Volker\wedding-website\img\logo-lg.gif', 'output_transparent.gif', background_color=(255, 255, 255, 255))
