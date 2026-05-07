"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import services using HelloWorld naming convention
from .orders.BrandService import BrandService
from .orders.TechnicalSpecificationsService import TechnicalSpecificationsService
from .orders.RefreshRateService import RefreshRateService
from .orders.ScreenSizeService import ScreenSizeService
from .orders.ResolutionService import ResolutionService
from .orders.PanelVideoService import PanelVideoService
from .orders.PanelService import PanelService
from .orders.PanelManufacturerService import PanelManufacturerService
from .orders.SupermarketAddressService import SupermarketAddressService
from .orders.DepartmentService import DepartmentService
from .orders.SupermarketService import SupermarketService
from .orders.ChainService import ChainService
from .orders.AdvertisementVideoService import AdvertisementVideoService
from .orders.VideoProducerService import VideoProducerService

# Initialize service instances with HelloWorld naming style
brandService = BrandService()
technicalSpecificationsService = TechnicalSpecificationsService()
refreshRateService = RefreshRateService()
screenSizeService = ScreenSizeService()
resolutionService = ResolutionService()
panelVideoService = PanelVideoService()
panelService = PanelService()
panelManufacturerService = PanelManufacturerService()
supermarketAddressService = SupermarketAddressService()
departmentService = DepartmentService()
supermarketService = SupermarketService()
chainService = ChainService()
advertisementVideoService = AdvertisementVideoService()
videoProducerService = VideoProducerService()
