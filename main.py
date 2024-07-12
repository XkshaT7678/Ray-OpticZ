import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import simpledialog

def draw_mirror(mirror_type='convex', object_distance=10, object_height=2):
    fig, ax = plt.subplots()

    # Draw mirror
    if mirror_type == 'convex':
        center_of_curvature = 10  # center of curvature for convex mirror
        focal_length = center_of_curvature / 2
        focal_point = focal_length
        mirror_label = 'Convex Mirror'
    else:
        center_of_curvature = -10  # center of curvature for concave mirror
        focal_length = center_of_curvature / 2
        focal_point = focal_length
        mirror_label = 'Concave Mirror'

    pole = 0
    mirror_radius = abs(center_of_curvature - pole)

    # Draw mirror (arc)
    if mirror_type == 'convex':
        theta = np.linspace(np.pi / 2, 3 * np.pi / 2, 100)
    else:
        theta = np.linspace(-np.pi / 2, np.pi / 2, 100)

    x = center_of_curvature + mirror_radius * np.cos(theta)
    y = mirror_radius * np.sin(theta)
    ax.plot(x, y, 'b')

    # Draw principal axis
    ax.axhline(0, color='black')

    # Draw center of curvature (C)
    ax.plot(center_of_curvature, 0, 'ro', label='Center of Curvature (C)')

    # Draw focal point (F)
    ax.plot(focal_point, 0, 'go', label='Focal Point (F)')

    # Determine object position (O) and image position (I)
    if mirror_type == 'convex':
        object_position = pole - object_distance
        # Calculate image position using the mirror equation: 1/f = 1/do + 1/di
        image_position = (object_distance * focal_length) / (object_distance + focal_length)
        image_height = object_height * (image_position / object_distance)

        # Draw reflected rays
        # Incident ray (from object)
        ax.plot([object_position, 0], [object_height, 0], 'y--', label='Incident Ray')  # incident ray
        # Reflected ray (to image)
        ax.plot([0, image_position], [0, image_height], 'm--', label='Reflected Ray')  # reflected ray

    else:
        object_position = pole + object_distance
        # Calculate image position using the mirror equation: 1/f = 1/do + 1/di
        image_position = (object_distance * focal_length) / (object_distance - focal_length)
        image_height = object_height * (image_position / object_distance)

        # Draw reflected rays
        # Incident ray (from object)
        ax.plot([object_position, 0], [object_height, 0], 'y--', label='Incident Ray')  # incident ray
        # Reflected ray (to image)
        ax.plot([0, image_position], [0, image_height], 'm--', label='Reflected Ray')  # reflected ray

        # Center ray (through center of curvature)
        ax.plot([object_position, center_of_curvature], [object_height, 0], 'c--', label='Center Ray')  # center ray

    # Draw object (O) and its arrow
    ax.plot(object_position, object_height, 'yo', label='Object (O)')
    ax.annotate('', xy=(object_position, object_height), xytext=(object_position, 0),
                arrowprops=dict(facecolor='yellow', arrowstyle='<|-', linewidth=2))

    # Draw image (I) and its arrow
    ax.plot(image_position, image_height, 'mo', label='Image (I)')
    ax.annotate('', xy=(image_position, image_height), xytext=(image_position, 0),
                arrowprops=dict(facecolor='magenta', arrowstyle='<|-', linewidth=2))

    ax.set_xlim(-30, 30)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal', adjustable='box')
    ax.legend()

    plt.title(f'{mirror_label} - Ray Diagram')
    plt.xlabel('Horizontal Axis')
    plt.ylabel('Vertical Axis')
    plt.show()

def get_object_distance():
    global object_distance
    # Ask for object distance with a custom dialog box
    answer = simpledialog.askstring('Object Distance', 'Enter the object distance:')
    # Convert the answer to a float and handle negative values
    if answer is not None:
        object_distance = float(answer)

def get_object_height():
    global object_height
    # Ask for object height with a custom dialog box
    answer = simpledialog.askstring('Object Height', 'Enter the object height:')
    # Convert the answer to a float
    if answer is not None:
        object_height = float(answer)

def toggle_mirror():
    global mirror_type
    if mirror_type == 'convex':
        mirror_type = 'concave'
    else:
        mirror_type = 'convex'
    draw_mirror(mirror_type, object_distance, object_height)

# Initial prompts for object distance and height
root = tk.Tk()
root.withdraw()  # Hide the root window

get_object_distance()
get_object_height()

mirror_type = 'convex'
draw_mirror(mirror_type, object_distance, object_height)

# Create tkinter window for toggling mirror type
root.deiconify()  # Show the root window

# Add button to toggle mirror type
toggle_button = tk.Button(root, text='Toggle Mirror', command=toggle_mirror)
toggle_button.pack()

root.mainloop()
