# Convert Carto3D Mesh to STL and WRL

This repository hosts a Python tool is designed for converting Carto3D mesh files into STL and WRL formats, suitable for 3D printing and colour map visualization. The tool focuses on processing 3D mesh data, efficiently filtering out sectors, and preparing the data for further use.


![Example VRML](/images/snapshotWRL.png)
![Example STL](/images/snapshotSTL.png)


## Features

- **Parsing Carto3D Mesh Files**: Extracts essential mesh data for conversion.
- **Sector Exclusion**: Filters out triangles marked with specific `GroupID`s.
- **VRML and STL Generation**: Creates VRML (.wrl) files for visualization and STL files for 3D printing, excluding the specified sectors.
- **Timestamped Outputs**: Names the output files with timestamps to facilitate organization.


## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system. This tool does not require external Python libraries outside of the Python Standard Library.

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/diogopmartins/Convert-Carto3D-mesh-to-STL-and-WRL.git
cd Convert-Carto3D-mesh-to-STL-and-WRL
