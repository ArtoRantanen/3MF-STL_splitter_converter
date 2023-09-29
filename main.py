import trimesh
import os

def sanitize_name(name):
    """Sanitize names for use as filenames or directories."""
    return "".join([c if c.isalnum() else "_" for c in name])

def split_and_save_as_stl(mesh, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Decompose the mesh into individual components
    mesh_components = mesh.split()

    # Iterate over each component and save it as a separate STL
    for i, component in enumerate(mesh_components):
        output_path = os.path.join(output_dir, f"component_{i}.stl")
        component.export(output_path, file_type="stl")

def process_mesh_or_scene(obj, output_dir):
    if isinstance(obj, trimesh.Scene):
        for name, mesh in obj.geometry.items():
            sanitized_name = sanitize_name(name)
            split_and_save_as_stl(mesh, os.path.join(output_dir, sanitized_name))
    else:  # Assuming a Mesh object
        split_and_save_as_stl(obj, output_dir)

def convert_3mf_to_stl_and_split(input_path, output_dir):
    # Load the 3MF file
    loaded_objs = trimesh.load(input_path, file_type="3mf")

    # If the loaded object is not a list (i.e., a single Mesh or Scene), make it a list for consistency
    if not isinstance(loaded_objs, list):
        loaded_objs = [loaded_objs]

    # Iterate over each object, convert to STL and split
    for i, obj in enumerate(loaded_objs):
        process_mesh_or_scene(obj, os.path.join(output_dir, f"model_{i}"))

if __name__ == "__main__":
    input_file_path = "2023_09_15.3mf"  # Replace with the path to your 3MF file
    output_directory = "output"  # Replace with the path to the directory where you want to save the STL files

    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    convert_3mf_to_stl_and_split(input_file_path, output_directory)
    print(f"Models have been saved to {output_directory}")

