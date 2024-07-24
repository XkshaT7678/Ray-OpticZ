# PHYMULATOR - 2024
# OUR TOPIC - RAY OPTICS
# Coded by Akshat Kumar
# D.A.V PUBLIC SCHOOL SECTOR 7 Rohini Delhi
#--------------------------------------Code starts Here--------------------------------------#
import matplotlib.pyplot as plt  #Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
import numpy as np #NumPy (Numerical Python) is a powerful library for numerical computing in Python.
import tkinter as tk #Tkinter (Tk interface) is a standard GUI (Graphical User Interface) library for Python.
from tkinter import simpledialog

def draw_mirror(mirror_type='convex', object_distance=10, object_height=2):
    fig, ax = plt.subplots()

    # Draw mirror
    if mirror_type == 'convex':
        center_of_curvature = 10  # center of curvature for convex mirror
        focus = center_of_curvature / 2
        mirror_label = ''
    else:
        center_of_curvature = -10  # center of curvature for concave mirror
        focus = center_of_curvature / 2
        mirror_label = ''
### Explanation for Swapping Mirror Labels:

# The mirrors were mislabeled in our simulation: "concave" acted as convex and "convex" as concave. We've corrected this to accurately reflect real-world optics, ensuring clear and accurate learning.

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

    # Draw focus (F)
    ax.plot(focus, 0, 'go', label='Focus (F)')

    # Determine object position (O) and image position (I)
    if mirror_type == 'convex':
        object_position = pole - object_distance
        if object_distance == focus:
            image_position = float('inf')
            image_height = float('inf')
        else:
            image_position = (object_distance * focus) / (object_distance + focus)
            image_height = object_height * (image_position / object_distance)

        # Draw reflected rays
        # Incident ray (from object)
        ax.annotate('', xy=(0, 0), xytext=(object_position, object_height), arrowprops=dict(facecolor='yellow', arrowstyle='->', linestyle='--', label='Incident Ray'))
        # Reflected ray (to image)
        if image_position == float('inf'):
            ax.annotate('', xy=(30, 30 * (image_height / image_position)), xytext=(0, 0), arrowprops=dict(facecolor='magenta', arrowstyle='->', linestyle='--', label='Reflected Ray'))
        else:
            ax.annotate('', xy=(image_position, image_height), xytext=(0, 0), arrowprops=dict(facecolor='magenta', arrowstyle='->', linestyle='--', label='Reflected Ray'))

    else:
        object_position = pole + object_distance
        if object_distance == focus:
            image_position = float('inf')
            image_height = float('inf')
        else:
            image_position = (object_distance * focus) / (object_distance - focus)
            image_height = object_height * (image_position / object_distance)

        # Draw reflected rays
        # Incident ray (from object)
        ax.annotate('', xy=(0, 0), xytext=(object_position, object_height), arrowprops=dict(facecolor='yellow', arrowstyle='->', linestyle='--', label='Incident Ray'))
        # Reflected ray (to image)
        if image_position == float('inf'):
            ax.annotate('', xy=(-30, -30 * (image_height / image_position)), xytext=(0, 0), arrowprops=dict(facecolor='magenta', arrowstyle='->', linestyle='--', label='Reflected Ray'))
        else:
            ax.annotate('', xy=(image_position, image_height), xytext=(0, 0), arrowprops=dict(facecolor='magenta', arrowstyle='->', linestyle='--', label='Reflected Ray'))

    # Draw object (O) and its arrow
    ax.plot(object_position, object_height, 'yo', label='Object (O)')
    ax.annotate('', xy=(object_position, object_height), xytext=(object_position, 0),
                arrowprops=dict(facecolor='yellow', arrowstyle='-|>', linewidth=2))

    # Draw image (I) and its arrow
    if image_position != float('inf'):
        ax.plot(image_position, image_height, 'mo', label='Image (I)')
        ax.annotate('', xy=(image_position, image_height), xytext=(image_position, 0),
                    arrowprops=dict(facecolor='magenta', arrowstyle='-|>', linewidth=2))

    ax.set_xlim(-30, 30)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal', adjustable='box')
    ax.legend()

    plt.suptitle(' PHYMULATOR - 2024')
    plt.title(f'{mirror_label}Ray Diagram')
    plt.xlabel('Horizontal Axis (x)')
    plt.ylabel('Vertical Axis (y)')
    plt.show()

def get_object_distance():
    global object_distance
    # Ask for object distance with a custom dialog box
    answer = simpledialog.askstring('Object Distance', 'Enter the Object Distance, (-ve for concave +ve for convex)')
    if answer is not None:
        object_distance = float(answer)

def get_object_height():
    global object_height
    # Ask for object height with a custom dialog box
    answer = simpledialog.askstring('Object Height', '               Enter the Object Height                   ')
    # Convert the answer to a float
    if answer is not None:
        object_height = float(answer)

def swap_mirror():
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

# Create tkinter window for swapping mirror type
root.deiconify()  # Show the root window

# Add button to swap mirror type
# swap_button = tk.Button(root, text='CHANGE MIRROR', command=swap_mirror)
# swap_button.pack()

root.mainloop()
#--------------------------------------Code ends Here--------------------------------------#
