# MAIN - LOGGER v0.1.0 r1.0
# -----------------------------------------------------------------------------

from main.ota_updater import OTAUpdater 
from main.logger import MainLogger


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/mastercba/logger')
    ota_updater.download_and_install_update_if_available('TORRIMORA', 'santino989')

def start():
    from main import ota_updater
    from main.logger import MainLogger

    loggerPRJ = MainLogger()
#    process()
#    ota_updater = OTAUpdater('https://github.com/mastercba/logger')
#    ota_updater.download_and_install_update_if_available('TORRIMORA', 'santino989')
#    ota_updater.using_network('TORRIMORA', 'santino989')
#    ota_updater.check_for_update_to_install_during_next_reboot()    

def boot():
    download_and_install_update_if_available()
    start()
    

boot()
# -----------------------------------------------------------------------------
