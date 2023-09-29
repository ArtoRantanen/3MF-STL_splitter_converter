import trimesh
import os

def split_stl(input_path, output_dir):
    # Load the STL file
    loaded_mesh = trimesh.load_mesh(input_path)

    # Decompose the STL into individual components
    mesh_components = loaded_mesh.split()

    # Iterate over each component and save it as a separate STL
    for i, mesh in enumerate(mesh_components):
        output_path = os.path.join(output_dir, f"component_{i}.stl")
        mesh.export(output_path)

if __name__ == "__main__":
    input_file_path = "2023_09_15.stl"  # Replace with the path to your STL file
    output_directory = "output"  # Replace with the path to the directory where you want to save the separated STL files

    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    split_stl(input_file_path, output_directory)
    print(f"Components have been saved to {output_directory}")