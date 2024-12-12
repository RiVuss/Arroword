#!/usr/bin/env python
# coding: utf-8

# In[162]:


from PIL import Image, ImageDraw, ImageFont
from IPython.display import display

def draw_arroword(grid, answer_color="#deebff", clue_color="white", save_as_file=False):
    # Visualization parameters
    CELL_SIZE = 100

    GRID_ROWS = len(grid)  # Dynamically calculate rows
    GRID_COLS = len(grid[0])  # Dynamically calculate columns
    IMG_WIDTH = GRID_COLS * CELL_SIZE
    IMG_HEIGHT = GRID_ROWS * CELL_SIZE

    # Create the image and drawing context
    img = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 16)
        answer_font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
        answer_font = ImageFont.load_default()

    # Helper function to wrap and scale text
    def wrap_text_and_scale(text, width, height, draw, font):
        while True:
            lines = []
            current_line = ""
            for w in text.split():
                test_line = w if not current_line else current_line + " " + w
                bbox = draw.textbbox((0, 0), test_line, font=font)
                w_width = bbox[2] - bbox[0]
                if w_width <= width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = w
            if current_line:
                lines.append(current_line)

            total_height = sum(draw.textbbox((0, 0), line, font=font)[3] for line in lines)
            if total_height <= height or font.size <= 8:
                return lines, font
            else:
                font = ImageFont.truetype("arial.ttf", font.size - 2)

    # Function to draw cell borders
    def draw_cell_border(r, c):
        x0 = c * CELL_SIZE
        y0 = r * CELL_SIZE
        x1 = x0 + CELL_SIZE
        y1 = y0 + CELL_SIZE
        draw.rectangle([x0, y0, x1, y1], outline="black", width=2)

    # Function to draw arrows
    def draw_arrow_for_clue(r, c, direction):
        """
        Draws arrows as black triangles positioned outside the cell border and pointing in the specified direction.
        For compound directions, draw a line from the border of the clue to the middle of the neighboring cell,
        and then place the arrowhead.
        """
        x0 = c * CELL_SIZE
        y0 = r * CELL_SIZE
        cx = x0 + CELL_SIZE / 2
        cy = y0 + CELL_SIZE / 2
        triangle_size = 12
        triangle_offset = 12

        if direction == "right":
            points = [
                (cx + CELL_SIZE / 2 + triangle_offset, cy),
                (cx + CELL_SIZE / 2 + triangle_offset - triangle_size, cy - triangle_size / 2),
                (cx + CELL_SIZE / 2 + triangle_offset - triangle_size, cy + triangle_size / 2)
            ]
        elif direction == "down":
            points = [
                (cx, cy + CELL_SIZE / 2 + triangle_offset),
                (cx - triangle_size / 2, cy + CELL_SIZE / 2 + triangle_offset - triangle_size),
                (cx + triangle_size / 2, cy + CELL_SIZE / 2 + triangle_offset - triangle_size)
            ]
        elif direction == "down right":
            line_start_x = x0 + CELL_SIZE / 8
            line_start_y = y0 + CELL_SIZE
            line_end_x = x0 + CELL_SIZE / 8
            line_end_y = y0 + CELL_SIZE + CELL_SIZE / 2
            draw.line([(line_start_x, line_start_y), (line_end_x, line_end_y)], fill="black", width=2)
            points = [
                (line_end_x  + triangle_offset , line_end_y),
                (line_end_x  + triangle_offset  - triangle_size, line_end_y - triangle_size / 2),
                (line_end_x  + triangle_offset  - triangle_size, line_end_y + triangle_size / 2)
            ]
        elif direction == "up right":
            line_start_x = x0 + CELL_SIZE / 8
            line_start_y = y0 
            line_end_x = x0 + CELL_SIZE / 8
            line_end_y = y0 - CELL_SIZE / 2
            draw.line([(line_start_x, line_start_y), (line_end_x, line_end_y)], fill="black", width=2)
            points = [
                (line_end_x  + triangle_offset - 1, line_end_y),
                (line_end_x  + triangle_offset - 1 - triangle_size, line_end_y - triangle_size / 2),
                (line_end_x  + triangle_offset - 1 - triangle_size, line_end_y + triangle_size / 2)
            ]
        elif direction == "right down":
            line_start_x = x0 + CELL_SIZE
            line_start_y = y0 + CELL_SIZE / 8
            line_end_x = x0 + CELL_SIZE + CELL_SIZE / 2
            line_end_y = y0 + CELL_SIZE / 8
            draw.line([(line_start_x, line_start_y), (line_end_x, line_end_y)], fill="black", width=2)
            points = [
                (line_end_x, line_end_y  + triangle_offset),
                (line_end_x - triangle_size / 2, line_end_y  + triangle_offset - triangle_size),
                (line_end_x + triangle_size / 2, line_end_y  + triangle_offset - triangle_size)
            ]
        elif direction == "left down":
            line_start_x = x0  
            line_start_y = y0 + CELL_SIZE / 8
            line_end_x = x0 - CELL_SIZE / 2 
            line_end_y = y0 + CELL_SIZE / 8

            draw.line([(line_start_x, line_start_y), (line_end_x, line_end_y)], fill="black", width=2)
            points = [
                (line_end_x, line_end_y  + triangle_offset -1),  #-1 to adjust for with location border
                (line_end_x - triangle_size / 2, line_end_y  + triangle_offset - triangle_size - 1), #-1 to adjust for with location
                (line_end_x + triangle_size / 2, line_end_y  + triangle_offset - triangle_size - 1)
            ]
        elif direction == "down left":
            line_start_x = x0 + CELL_SIZE / 8
            line_start_y = y0 + CELL_SIZE - CELL_SIZE / 8
            line_end_x = x0 - CELL_SIZE / 2
            line_end_y = y0 + CELL_SIZE + CELL_SIZE / 2
            draw.line([(line_start_x, line_start_y), (line_end_x, line_end_y)], fill="black", width=2)
            points = [
                (line_end_x, line_end_y),
                (line_end_x + triangle_size, line_end_y - triangle_size / 2),
                (line_end_x + triangle_size / 2, line_end_y - triangle_size)
            ]
        else:
            return

        draw.polygon(points, fill="black")


    # Draw the grid (background fills first)
    for r in range(GRID_ROWS):
        for c in range(GRID_COLS):
            x0 = c * CELL_SIZE
            y0 = r * CELL_SIZE
            x1 = x0 + CELL_SIZE
            y1 = y0 + CELL_SIZE
            cell = grid[r][c]

            if cell["type"] == "clue":
                draw.rectangle([x0, y0, x1, y1], fill=clue_color)
            elif cell["type"] == "answer":
                draw.rectangle([x0, y0, x1, y1], fill=answer_color)

    # Draw arrows and content
    for r in range(GRID_ROWS):
        for c in range(GRID_COLS):
            x0 = c * CELL_SIZE
            y0 = r * CELL_SIZE
            cell = grid[r][c]

            if cell["type"] == "clue":
                margin = 10
                max_width = CELL_SIZE - 2 * margin
                max_height = CELL_SIZE - 2 * margin
                lines, scaled_font = wrap_text_and_scale(cell["clue_text"], max_width, max_height, draw, font)

                total_height = sum(draw.textbbox((0, 0), line, font=scaled_font)[3] for line in lines)
                current_y = y0 + (CELL_SIZE - total_height) / 2

                for line in lines:
                    bbox = draw.textbbox((0, 0), line, font=scaled_font)
                    line_width = bbox[2] - bbox[0]
                    current_x = x0 + (CELL_SIZE - line_width) / 2
                    draw.text((current_x, current_y), line, font=scaled_font, fill="black")
                    current_y += bbox[3]

                draw_arrow_for_clue(r, c, cell["direction"])
            elif cell["type"] == "answer":
                letter = cell["letter"]
                bbox = draw.textbbox((0, 0), letter, font=answer_font)
                w = bbox[2] - bbox[0]
                h = bbox[3] - bbox[1]
                draw.text((x0 + (CELL_SIZE - w) / 2, y0 + (CELL_SIZE - h) / 2), letter, font=answer_font, fill="black")

            draw_cell_border(r, c)

    # Save the image if requested
    if save_as_file:
        img.save("arrowword_example.png")
        print("Arrowword example saved as arrowword_example.png")

    # Return the image
    return img

