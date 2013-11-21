'''
This is example configuration for Stratum server.
Please rename it to config.py and fill correct values.

This is already setup with sane values for solomining.
You NEED to set the parameters in BASIC SETTINGS
'''

# ******************** BASIC SETTINGS ***************
# These are the MUST BE SET parameters!

CENTRAL_WALLET = 'set_valid_addresss_in_config!'	# local BITCOIN address where money goes

BITCOIN_TRUSTED_HOST = 'localhost'
BITCOIN_TRUSTED_PORT = 8332
BITCOIN_TRUSTED_USER = 'user'
BITCOIN_TRUSTED_PASSWORD = 'somepassword'

# ******************** BASIC SETTINGS ***************
# Backup BITCOINd connections (consider having at least 1 backup)
# You can have up to 99

#BITCOIN_TRUSTED_HOST_1 = 'localhost'
#BITCOIN_TRUSTED_PORT_1 = 8332
#BITCOIN_TRUSTED_USER_1 = 'user'
#BITCOIN_TRUSTED_PASSWORD_1 = 'somepassword'

#BITCOIN_TRUSTED_HOST_2 = 'localhost'
#BITCOIN_TRUSTED_PORT_2 = 8332
#BITCOIN_TRUSTED_USER_2 = 'user'
#BITCOIN_TRUSTED_PASSWORD_2 = 'somepassword'

# ******************** GENERAL SETTINGS ***************

# Enable some verbose debug (logging requests and responses).
DEBUG = False

# Destination for application logs, files rotated once per day.
LOGDIR = 'log/'

# Main application log file.
LOGFILE = "stratum.log"		# eg. 'stratum.log'

# Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGLEVEL = 'INFO'

# Logging Rotation can be enabled with the following settings
# It if not enabled here, you can set up logrotate to rotate the files. 
# For built in log rotation set LOG_ROTATION = True and configrue the variables
LOG_ROTATION = True
LOG_SIZE = 10485760 # Rotate every 10M
LOG_RETENTION = 10 # Keep 10 Logs
# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 300

# Disable the example service
ENABLE_EXAMPLE_SERVICE = False

# ******************** TRANSPORTS *********************

# Hostname or external IP to expose
HOSTNAME = 'localhost'

# Port used for Socket transport. Use 'None' for disabling the transport.
LISTEN_SOCKET_TRANSPORT = 3333
# Port used for HTTP Poll transport. Use 'None' for disabling the transport
LISTEN_HTTP_TRANSPORT = None
# Port used for HTTPS Poll transport
LISTEN_HTTPS_TRANSPORT = None
# Port used for WebSocket transport, 'None' for disabling WS
LISTEN_WS_TRANSPORT = None
# Port used for secure WebSocket, 'None' for disabling WSS
LISTEN_WSS_TRANSPORT = None


# Salt used when hashing passwords
PASSWORD_SALT = 'some_crazy_string'

# ******************** Database  *********************

# MySQL
DB_MYSQL_HOST = 'localhost'
DB_MYSQL_DBNAME = 'pooldb'
DB_MYSQL_USER = 'pooldb'
DB_MYSQL_PASS = '**empty**'

# ******************** Adv. DB Settings *********************
#  Don't change these unless you know what you are doing

DB_LOADER_CHECKTIME = 15	# How often we check to see if we should run the loader
DB_LOADER_REC_MIN = 1		# Min Records before the bulk loader fires
DB_LOADER_REC_MAX = 50		# Max Records the bulk loader will commit at a time

DB_LOADER_FORCE_TIME = 300      # How often the cache should be flushed into the DB regardless of size.

DB_STATS_AVG_TIME = 300		# When using the DATABASE_EXTEND option, average speed over X sec
				#	Note: this is also how often it updates
DB_USERCACHE_TIME = 600		# How long the usercache is good for before we refresh

# ******************** Pool Settings *********************

# User Auth Options
USERS_AUTOADD = False		# Automatically add users to db when they connect.
                            # This basically disables User Auth for the pool.
USERS_CHECK_PASSWORD = False	# Check the workers password? (Many pools don't)

# Transaction Settings
COINBASE_EXTRAS = '/stratumPool/'			# Extra Descriptive String to incorporate in solved blocks
ALLOW_NONLOCAL_WALLET = False				# Allow valid, but NON-Local wallet's

# BITCOINd communication polling settings (In Seconds)
PREVHASH_REFRESH_INTERVAL = 5 	# How often to check for new Blocks
				#	If using the blocknotify script (recommended) set = to MERKLE_REFRESH_INTERVAL
				#	(No reason to poll if we're getting pushed notifications)
MERKLE_REFRESH_INTERVAL = 60	# How often check memorypool
				#	This effectively resets the template and incorporates new transactions.
				#	This should be "slow"

INSTANCE_ID = 31		# Used for extranonce and needs to be 0-31

# ******************** Pool Difficulty Settings *********************
#  Again, Don't change unless you know what this is for.

# Pool Target (Base Difficulty)
POOL_TARGET = 16			# Pool-wide difficulty target int >= 1

# Variable Difficulty Enable
VARIABLE_DIFF = False		# Master variable difficulty enable

# Variable diff tuning variables
#VARDIFF will start at the POOL_TARGET. It can go as low as the VDIFF_MIN and as high as min(VDIFF_MAX or Liteconin's difficulty)
USE_BITCOIN_DIFF = False   # Set the maximum difficulty to the BITCOIN difficulty. 
DIFF_UPDATE_FREQUENCY = 86400 # Update the BITCOIN difficulty once a day for the VARDIFF maximum
VDIFF_MIN_TARGET = 15		#  Minimum Target difficulty 
VDIFF_MAX_TARGET = 1000		# Maximum Target difficulty 
VDIFF_TARGET_TIME = 30		# Target time per share (i.e. try to get 1 share per this many seconds)
VDIFF_RETARGET_TIME = 120		# Check to see if we should retarget this often
VDIFF_VARIANCE_PERCENT = 20	# Allow average time to very this % from target without retarget
#### Advanced Option #####
# For backwards compatibility, we send the scrypt hash to the solutions column in the shares table
# For block confirmation, we have an option to send the block hash in
# Please make sure your front end is compatible with the block hash in the solutions table.
SOLUTION_BLOCK_HASH = False # If enabled, send the block hash. If false send the scrypt hash in the shares table

# ******************** E-Mail Notification Settings *********************

NOTIFY_EMAIL_TO = ''		# Where to send Start/Found block notifications
NOTIFY_EMAIL_TO_DEADMINER = ''	# Where to send dead miner notifications
NOTIFY_EMAIL_FROM = 'root@localhost'	# Sender address
NOTIFY_EMAIL_SERVER = 'localhost'	# E-Mail Sender
NOTIFY_EMAIL_USERNAME = ''		# E-Mail server SMTP Logon
NOTIFY_EMAIL_PASSWORD = ''
NOTIFY_EMAIL_USETLS = True


# ******************** Admin settings *********************

# Use scripts/generateAdminHash.sh <password> to generate the hash
# for calculating SHA256 of your preferred password
ADMIN_PASSWORD_SHA256 = 'password hash' # SHA256 of the password

