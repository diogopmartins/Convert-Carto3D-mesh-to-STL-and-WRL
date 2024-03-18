import os
import datetime

def parse_mesh(mesh_file_path):
    vertices = []
    triangles = []
    group_ids = []
    with open(mesh_file_path, 'r') as file:
        current_section = ""
        for line in file:
            line = line.strip()
            if line.startswith('['):
                current_section = line
                continue

            if '[VerticesSection]' in current_section and '=' in line:
                parts = line.split('=')[1].strip().split()
                vertex = tuple(map(float, parts[:3]))
                vertices.append(vertex)

            elif '[TrianglesSection]' in current_section and '=' in line:
                parts = line.split('=')[1].strip().split()
                triangle = tuple(map(int, parts[:3]))
                group_id = float(parts[-1])
                triangles.append(triangle)
                group_ids.append(group_id)

    return vertices, triangles, group_ids


def calculate_gradient_color(i, num_triangles):
    colors = [(0, 0, 1), (0, 1, 0), (1, 1, 0), (1, 0.5, 0), (1, 0, 0)]
    t = i / max(1, num_triangles - 1) * (len(colors) - 1)
    index = int(t)
    t -= index
    if index >= len(colors) - 1:
        return colors[-1]
    return tuple((1 - t) * a + t * b for a, b in zip(colors[index], colors[index + 1]))


def generate_vrml_with_multi_gradient(vertices, triangles, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write("#VRML V2.0 utf8\n")
        file.write("Group {\n")
        file.write(" children [\n")

        num_triangles = len(triangles)
        for i, tri in enumerate(triangles):
            color = calculate_gradient_color(i, num_triangles)

            file.write("  Shape {\n")
            file.write("   appearance Appearance {\n")
            file.write("    material Material {\n")
            file.write(f"     diffuseColor {color[0]} {color[1]} {color[2]}\n")
            file.write("    }\n")
            file.write("   }\n")
            file.write("   geometry IndexedFaceSet {\n")
            file.write("    coord Coordinate {\n")
            file.write("     point [\n")
            for idx in tri:
                file.write(f"      {vertices[idx][0]} {vertices[idx][1]} {vertices[idx][2]},\n")
            file.write("     ]\n")
            file.write("    }\n")
            file.write("    coordIndex [0, 1, 2, -1]\n")
            file.write("   }\n")
            file.write("  }\n")

        file.write(" ]\n")
        file.write("}\n")



def generate_stl_for_positive_group_ids(vertices, triangles, group_ids, output_stl_path):
    with open(output_stl_path, 'w') as stl_file:
        stl_file.write("solid mesh\n")
        for tri, gid in zip(triangles, group_ids):
            if gid >= 0:
                stl_file.write("facet normal 0 0 0\n outer loop\n")
                for idx in tri:
                    stl_file.write(f"vertex {vertices[idx][0]} {vertices[idx][1]} {vertices[idx][2]}\n")
                stl_file.write("endloop\nendfacet\n")
        stl_file.write("endsolid mesh\n")


def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    mesh_file_path = os.path.join(script_dir, '1-LA.mesh') 
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Output paths with timestamp
    output_stl_path = os.path.join(script_dir, f'object_STL_{timestamp}.stl')
    output_vrml_path = os.path.join(script_dir, f'object_VRML_color_{timestamp}.wrl')

    vertices, triangles, group_ids = parse_mesh(mesh_file_path)
    generate_stl_for_positive_group_ids(vertices, triangles, group_ids, output_stl_path)
    generate_vrml_with_multi_gradient(vertices, triangles, output_vrml_path)

    print(f"STL file generated: {output_stl_path}")
    print(f"VRML file generated: {output_vrml_path}")
    print("COMPLETED - DM 2024")


if __name__ == "__main__":
    main()
