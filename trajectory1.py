import carla
import matplotlib.pyplot as plt

# Connect to the CARLA simulator
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
world = client.get_world()

# Create a dictionary to store trajectory data for each actor
trajectories = {}

# Loop for 10 seconds and record data every 0.1 seconds
for i in range(0,1000,4):
    time = world.get_snapshot().timestamp.elapsed_seconds

    # Loop through all actors and record data for each vehicle actor
    for actor in world.get_actors():
        if 'vehicle' in actor.type_id:
            actor_id = actor.id
            location = actor.get_location()
            x = location.x
            y = location.y
            z = location.z

            # Update the trajectory data for the actor
            if actor_id in trajectories:
                trajectories[actor_id]['x'].append(x)
                trajectories[actor_id]['y'].append(y)
            else:
                trajectories[actor_id] = {'x': [x], 'y': [y]}

    # Wait for 0.1 seconds
    world.wait_for_tick()

# Plot the trajectory for each actor
for actor_id, data in trajectories.items():
    plt.plot(data['x'], data['y'], label=f'Actor {actor_id}')

plt.title('Trajectory of Actors in CARLA Simulator')
plt.xlabel('X position (m)')
plt.ylabel('Y position (m)')
plt.legend()
plt.show()