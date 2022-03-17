from environs import Env

env = Env()
env.read_env()

theme = env.str("vendetta_theme")
db_config = env.dict("connection_vendetta_users_postgres")

host, port = env.str("vendetta_client_host"), env.int("vendetta_port")
