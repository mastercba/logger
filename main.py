# MAIN - LOGGER v0.1.2 r1.2
# -----------------------------------------------------------------------------

from main.ota_updater import OTAUpdater 
from main.logger import MainLogger


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/mastercba/logger')
    ota_updater.download_and_install_update_if_available('TORRIMORA', 'santino989')

def start():
    from main import ota_updater
    from main.logger import MainLogger

    ota_updater = OTAUpdater('https://github.com/mastercba/logger')
#    ota_updater.download_and_install_update_if_available('TORRIMORA', 'santino989')
    ota_updater.using_network('TORRIMORA', 'santino989')
    ota_updater.check_for_update_to_install_during_next_reboot()    
    loggerPRJ = MainLogger()

def boot():
    download_and_install_update_if_available()
    start()
    

boot()
# -----------------------------------------------------------------------------
