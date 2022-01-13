from environs import Env

env = Env()
env.read_env()

theme = env.str("vendetta_theme")

