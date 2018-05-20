import tensorflow as tf
from  python_visual_mpc.visual_mpc_core.algorithm.cem_controller_goalimage_sawyer import CEM_controller
import numpy as np

class Imitation_CEM_controller(CEM_controller):
    def __init__(self, ag_params, policyparams, predictor, imitation_policy):
        super().__init__(ag_params, policyparams, predictor)
        self.imitation_policy = imitation_policy

    def sample_actions(self, last_frames, last_states):
        print(last_frames)
        print(last_states)
        print(1 / 0)
