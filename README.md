# Plot Vehicle Actor Trajectory in Carla Simulator

This code assumes that you have already set up a CARLA simulator environment and have launched the simulator with multiple vehicle actors controlled by different players. 

The code connects to the simulator using the CARLA Python API, loops through all actors in the world, and records the x and y coordinate data for each vehicle actor every 0.1 seconds for 10 seconds.

The trajectory data is stored in a dictionary for each actor, and then a plot is created of the trajectory for each actor using the matplotlib library. 

The resulting plot shows the trajectory of each vehicle actor in the CARLA simulator. See Example Plot Below; Shows the trajectory to collision of two different actors, each having its unique ID.


![Trajectory 1](https://user-images.githubusercontent.com/59507941/233200841-2dc47695-1c4f-4591-ae16-7d1350f6f554.PNG)
