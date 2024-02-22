# Thermal Analysis of a 2D plate


Description:
This Python program simulates the thermal analysis of a 2D plate with a specific heat source using the Finite Difference Method (FDM). The simulation calculates the temperature distribution on the plate over time, considering various parameters such as thermal conductivity, density, specific heat, and heat source intensity.

How it works:

Users input the dimensions of the plate (length and width), the number of nodes in the x and y directions, and the thermal properties of the plate.
The program iterates through a specified number of time steps, calculating the temperature at each node using the Finite Difference Method.
Boundary conditions are applied to mimic real-world scenarios, such as fixed temperatures at the plate edges or the application of a heat source at a specific location.
The final temperature distribution is plotted on a 2D graph using matplotlib, providing a visual representation of the thermal behavior of the plate.
Key Features:

Flexibility: Users can input custom parameters to simulate a wide range of thermal scenarios, making it suitable for diverse engineering applications.
Visualization: The program generates a heatmap of the temperature distribution, aiding in the interpretation and analysis of the simulation results.
Educational Tool: The code serves as a learning resource for understanding thermal analysis concepts and numerical methods like the Finite Difference Method.
Usage:

Clone the repository to your local machine.
Run the program in a Python environment, ensuring all dependencies are installed (numpy and matplotlib).
Follow the prompts to input the plate dimensions, thermal properties, simulation parameters, and heat source intensity.
View the plotted temperature distribution to analyze the thermal behavior of the plate.
