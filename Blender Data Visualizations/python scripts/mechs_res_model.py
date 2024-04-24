import bpy
import csv
from operator import itemgetter
# STEM support mechanisms and resources

# Define pastel colors (you can add more colors if needed)
pastel_colors = [
    (0.937, 0.635, 0.635, 1.0),  # Light pink
    (0.725, 0.882, 0.725, 1.0),  # Light green
    (0.725, 0.725, 0.882, 1.0),  # Light blue
    (0.882, 0.725, 0.882, 1.0),  # Light purple
    (0.882, 0.882, 0.725, 1.0),  # Light yellow
]

# Open the CSV file for reading
csvfile = open('C:\\Users\\aliso\\Downloads\\STEM_mech_res.csv', 'r')
inFile = csv.reader(csvfile, delimiter=',', quotechar='"')

# Read the CSV data into vertices, including the first column as labels
data = list(inFile)
labels = [r[0] for r in data[1:]]  # Skip the header row for labels
values = [float(r[1]) for r in data[1:]]
vertices = [(i, 0, 0) for i in range(len(values))]

# Create a new mesh
name = "bar_plot"
mesh = bpy.data.meshes.new(name)
obj = bpy.data.objects.new(name, mesh)

# Link the object to the current collection
bpy.context.scene.collection.objects.link(obj)

# Create the mesh data
obj.data.from_pydata(vertices, [], [])

# Set object scale and dimensions
obj.scale = (0.1, 0.1, 1)  # Adjust the scale as needed
obj.dimensions = (len(values), max(values), 1)  # Adjust dimensions based on data

# Create a simple bar plot using cubes
for i, v in enumerate(vertices):
    x, y, z = v
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y - values[i] / 2, z))
    cube = bpy.context.active_object
    cube.scale.x = 0.4  # Adjust the width of the bars as needed
    cube.scale.y = values[i]  # Adjust the height of the bars based on data

    # Set the color of the cubes
    color_index = i % len(pastel_colors)
    cube.active_material = bpy.data.materials.new(name=f"BarMaterial{i}")
    cube.active_material.diffuse_color = pastel_colors[color_index]

    # Create labels for the bars
    bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(x, y - values[i], z + 0.1))
    text = bpy.context.active_object
    text.data.body = f"{labels[i]}: {int(values[i])}" if values[i].is_integer() else f"{labels[i]}: {values[i]}"    
    text.scale = (0.36, 0.36, 0.36)  # Adjust the scale of the labels as needed
    text.rotation_euler.x = 0  # Set X rotation to 0 for horizontal labels
    text.rotation_euler.y = 0
    text.rotation_euler.z = -1.5708 # Rotate labels 90 degrees (1.5708 radians) for alignment with the bars


# Enable smooth shading for the cubes
bpy.ops.object.shade_smooth()
