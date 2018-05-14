import os
import python_visual_mpc
current_dir = '/'.join(str.split(__file__, '/')[:-1])
bench_dir = '/'.join(str.split(__file__, '/')[:-2])

from python_visual_mpc.visual_mpc_core.algorithm.cem_controller import CEM_controller

ROOT_DIR = os.path.abspath(python_visual_mpc.__file__)
ROOT_DIR = '/'.join(str.split(ROOT_DIR, '/')[:-2])

from python_visual_mpc.visual_mpc_core.agent.agent_mjc import AgentMuJoCo
import numpy as np

agent = {
    'type': AgentMuJoCo,
    'T': 40,
    'substeps':50,
    'make_final_gif':'', ########################3
    'adim':3,
    'sdim':6,
    'filename': ROOT_DIR + '/mjc_models/cartgripper_updown_whitefingers.xml',
    'filename_nomarkers': ROOT_DIR + '/mjc_models/cartgripper_updown_whitefingers.xml',
    'gen_xml':1,   #generate xml every nth trajecotry
    'num_objects': 2,
    'viewer_image_height' : 480,
    'viewer_image_width' : 640,
    'image_height':48,
    'image_width':64,
    'additional_viewer':'',
    'data_save_dir':current_dir + '/data/train',
    'posmode':"",
    'targetpos_clip':[[-0.45, -0.45, -0.08], [0.45, 0.45, 0.15]],
    'discrete_adim':[2],
    'not_use_images':"",
    'sample_objectpos':'',
    'object_object_mindist':0.35,
    'const_dist':0.2,
    'randomize_ballinitpos':'',
    # 'dist_ok_thresh':0.1,
    'first_last_noarm':''
}

policy = {
    'verbose':'',
    'type' : CEM_controller,
    'current_dir':current_dir,
    'nactions': 5,
    'repeat': 3,
    'initial_std': 0.08,        # std dev. in xy
    'initial_std_lift': 2.5,
    'iterations': 2,
    'action_cost_factor': 0,
    'rew_all_steps':"",
    'finalweight':10,
    'no_action_bound':"",
    'num_samples': 100,
    'replan_interval':10,
}

config = {
    'current_dir':current_dir,
    'save_data': True,
    'start_index':0,
    'end_index': 59999,
    'traj_per_file':5,
    'agent':agent,
    'policy':policy,
}
