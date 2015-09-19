import tornado.options
import logging
import os
import sys

CONFIG_LOCAL = "settings_local.py"  # can be optionally created, is ignored in VCS
CONFIG_DEFAULT = "settings.py"  # default config file, used if no command line arg is provided, and config_local.py does
                              # not exists

logger = logging.getLogger(__file__)


def parse_config_file(config_file):
    #parse default options
    path = os.path.dirname(__file__)
    config_path = os.path.join(path, CONFIG_DEFAULT)
    logger.info("parsing options from default config file: %s", config_path)
    tornado.options.parse_config_file(config_path)

    if config_file:
        #parse specified config file that overwrites default settings
        logger.info("parsing options from config file: %s", config_file)
        tornado.options.parse_config_file(config_file)
        return
    try:
        #config file was not specified try to load local config
        config_path = os.path.join(path, CONFIG_LOCAL)
        logger.info("parsing options from config file: %s", config_path)
        tornado.options.parse_config_file(config_path)
    except IOError:
        logger.warning("""
cannot find local config file: %s, create one basing on config_local_example.py
starting with default options""", config_path)


def configure(config_path=None, already_loaded=[]):
    """loads default and user defined config options, subsequent calls are ignored"""
    if already_loaded and not config_path:
        return
    if not already_loaded:
        already_loaded.append(True)

        tornado.options.define("config", help="config file", type=str)
        tornado.options.define("port", help="server port", default=8000, type=int)
        tornado.options.define("address", help="server address", default="0.0.0.0", type=str)
        tornado.options.define("default_scenes", help="list of auto-loaded scenes", multiple=True)

        #configure logging
        logging.basicConfig(
            format="%(levelname)s:%(name)s: %(message)s",
            level=logging.INFO,
        )

        #setup django settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alvi.config.django_settings")

    if not config_path:
        tornado.options.parse_command_line()
        config_path = tornado.options.options.config
    parse_config_file(config_path)
