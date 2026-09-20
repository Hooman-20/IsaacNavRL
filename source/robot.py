import isaaclab.sim as sim_utils

from isaaclab.assets import Articulation, ArticulationCfg
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR


JETBOT_CONFIG = ArticulationCfg(
    prim_path="/World/Robot",

    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_NUCLEUS_DIR}/Robots/NVIDIA/Jetbot/jetbot.usd"
    ),

    actuators={
        "wheel_acts": ImplicitActuatorCfg(
            joint_names_expr=[".*"],
            damping=None,
            stiffness=None,
        )
    },
)


def create_robot():
    """Create and return our JetBot."""

    robot = Articulation(JETBOT_CONFIG)

    return robot