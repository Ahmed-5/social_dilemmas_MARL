from cleanup import CleanupEnv
# from switch import SwitchEnv
# # from harvest import HarvestEnv

num_agents = 3

sample_actions = {f"agent-{i}":0 for i in range(num_agents)} # 4 is "STAY", 0 is "MOVE_LEFT"
# # print(sample_actions)

env = CleanupEnv(num_agents=num_agents)

# env = SwitchEnv(num_switches=20, num_agents=num_agents)

# # env = HarvestEnv(num_agents=num_agents)

obs = env.reset()
# print(env.agents)
env.setup_agents()
# print(env.agents)
env.render("1.png")
observations,rewards,dones,info = env.step(sample_actions)
print(observations,rewards,dones,info)
env.render("2.png")

# # print(obs)

# from ray.rllib.algorithms.maddpg.maddpg import MADDPGConfig
# from ray import air
# from ray import tune
# config = MADDPGConfig()
# config.training(n_step=tune.grid_search([3, 5]))  
# config.environment(env=env)  
# tune.Tuner(  
#     "MADDPG",
#     run_config=air.RunConfig(stop={"episode_reward_mean":200}),
#     param_space=config.to_dict()
# ).fit()