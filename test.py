from cleanup import CleanupEnv

num_agents = 3

sample_actions = {f"agent-{i}":0 for i in range(num_agents)} # 4 is "STAY", 0 is "MOVE_LEFT"
# print(sample_actions)

env = CleanupEnv(num_agents=num_agents)
obs = env.reset()
# print(env.agents)
env.setup_agents()
# print(env.agents)
env.render("1.png")
env.step(sample_actions)
env.render("2.png")

# print(obs)