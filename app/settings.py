from os import environ
from dotenv import load_dotenv

load_dotenv('.env')

SESSION_CONFIGS = [
    dict(
        name='mini_ultimatum',
        display_name="Play the mini ultimatum game",
        app_sequence=['mini_ultimatum', 'exit_survey'],
        num_demo_participants=3,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'KSH'
USE_POINTS = False

ROOMS = [
    dict(name='mini_ultimatum', 
         display_name='Mini Ultimatum Game Room',
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
OTREE_ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

OTREE_AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')
OTREE_PRODUCTION = int(environ.get('OTREE_PRODUCTION', 0))
OTREE_REST_KEY = environ.get('OTREE_REST_KEY')
DATABASE_URL = environ.get('DATABASE_URL')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '6569938605431'

INSTALLED_APPS = ['otree']
