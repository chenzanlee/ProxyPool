import platform
from os.path import dirname, abspath, join
from environs import Env
from loguru import logger
from proxypool.utils.parse import parse_redis_connection_string

env = Env()
env.read_env()

# definition of flags
IS_WINDOWS = platform.system().lower() == 'windows'

# definition of dirs
ROOT_DIR = dirname(dirname(abspath(__file__)))
LOG_DIR = join(ROOT_DIR, env.str('LOG_DIR', 'logs'))

# definition of environments
DEV_MODE, TEST_MODE, PROD_MODE = 'dev', 'test', 'prod'
APP_ENV = env.str('APP_ENV', DEV_MODE).lower()
APP_DEBUG = env.bool('APP_DEBUG', True if APP_ENV == DEV_MODE else False)
APP_DEV = IS_DEV = APP_ENV == DEV_MODE
APP_PROD = IS_PROD = APP_ENV == PROD_MODE
APP_TEST = IS_TEST = APP_ENV == TEST_MODE

# redis host
REDIS_HOST = env.str('REDIS_HOST', '127.0.0.1')
# redis port
REDIS_PORT = env.int('REDIS_PORT', 6379)
# redis password, if no password, set it to None
REDIS_PASSWORD = env.str('REDIS_PASSWORD', 'adxf@.qw8yzam$*')
# redis db, if no choice, set it to 0
REDIS_DB = env.int('REDIS_DB', 9)
# redis connection string, like redis://[password]@host:port or rediss://[password]@host:port/0
REDIS_CONNECTION_STRING = env.str('REDIS_CONNECTION_STRING', None)

if REDIS_CONNECTION_STRING:
    REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB = parse_redis_connection_string(REDIS_CONNECTION_STRING)

# redis hash table key name
REDIS_KEY = env.str('REDIS_KEY', 'proxies:zhandaye')

# definition of proxy scores
PROXY_SCORE_MAX = 100
PROXY_SCORE_MIN = 20
PROXY_SCORE_INIT = 50

# definition of proxy number
PROXY_NUMBER_MAX = 50000
PROXY_NUMBER_MIN = 0

# definition of tester cycle, it will test every CYCLE_TESTER second
CYCLE_TESTER = env.int('CYCLE_TESTER', 20)
# definition of getter cycle, it will get proxy every CYCLE_GETTER second
CYCLE_GETTER = env.int('CYCLE_GETTER', 10)
GET_TIMEOUT = env.int('GET_TIMEOUT', 10)

# definition of tester
TEST_URL = env.str('TEST_URL', 'http://www.baidu.com')
TEST_TIMEOUT = env.int('TEST_TIMEOUT', 5)
TEST_BATCH = env.int('TEST_BATCH', 20)
# only save anonymous proxy
TEST_ANONYMOUS = True
# TEST_HEADERS = env.json('TEST_HEADERS', {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
# })
TEST_VALID_STATUS = env.list('TEST_VALID_STATUS', [200, 206, 302, 429])

# definition of api
API_HOST = env.str('API_HOST', '0.0.0.0')
API_PORT = env.int('API_PORT', 5555)
API_THREADED = env.bool('API_THREADED', True)

# flags of enable
ENABLE_TESTER = env.bool('ENABLE_TESTER', True)
ENABLE_GETTER = env.bool('ENABLE_GETTER', True)
ENABLE_SERVER = env.bool('ENABLE_SERVER', True)

# logger.add(env.str('LOG_RUNTIME_FILE', join(LOG_DIR, 'runtime.log')), level='DEBUG', rotation='1 week', retention='20 days')
# logger.add(env.str('LOG_ERROR_FILE', join(LOG_DIR, 'error.log')), level='ERROR', rotation='1 week')
