from isaaclab.app import AppLauncher

app_launcher = AppLauncher({"visualizer": "kit"})
simulation_app = app_launcher.app

from isaaclab.sim import (
    SimulationCfg,
    SimulationContext,
    GroundPlaneCfg,
    DistantLightCfg,
)

import sys
sys.path.append(r"F:\IsaacNavRL")

from source.robot import create_robot


sim_cfg = SimulationCfg()
sim = SimulationContext(sim_cfg)

sim.set_camera_view(
    eye=[3.0, 3.0, 3.0],
    target=[0.0, 0.0, 0.0]
)

# Create ground
ground_cfg = GroundPlaneCfg()
ground_cfg.func("/World/GroundPlane", ground_cfg)

# Create light
light_cfg = DistantLightCfg(intensity=3000.0)
light_cfg.func("/World/Light", light_cfg)

# Create JetBot
robot = create_robot()

sim.reset()

import torch

# Left wheel, right wheel
wheel_velocity = torch.tensor(
    [[10.0, 10.0]],
    device=sim.device
)

print("My JetBot is driving!")

while simulation_app.is_running():

    # Send velocity command to the wheels
    robot.set_joint_velocity_target(wheel_velocity)

    # Send commands into the simulator
    robot.write_data_to_sim()

    # Run one physics step
    sim.step()

    # Update Isaac Lab's robot data
    robot.update(sim.get_physics_dt())

simulation_app.close()