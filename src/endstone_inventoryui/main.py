from endstone.plugin import Plugin
from endstone import Logger
from endstone_inventoryui.listener import EventListener


class InventoryUIPlugin(Plugin):
    prefix = "InventoryUI"
    api_version = "0.11"
    load = "POSTWORLD"

    DEBUG_LOG = False

    def on_enable(self) -> None:
        self.register_events(EventListener(self))
        if self.DEBUG_LOG:
            self.logger.set_level(Logger.DEBUG)
