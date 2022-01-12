from environs import Env

env = Env()
env.read_env()

db_config = env.dict("connection_vendetta_users_postgres")