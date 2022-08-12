from dino_runner.utils.constants import CLOUD, CLOUD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Could(PowerUp):
    def __init__(self):
        self.image = CLOUD
        self.type = CLOUD_TYPE
        super().__init__(self.image, self.type)