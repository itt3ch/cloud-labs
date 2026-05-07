"""
2024
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Orders DB imports for DAOs corresponding to each entity
from .orders.VideoProducerDao import VideoProducerDAO
from .orders.BrandDao import BrandDAO
from .orders.AdvertisementVideoDao import AdvertisementVideoDAO
from .orders.ChainDao import ChainDAO
from .orders.SupermarketDao import SupermarketDAO
from .orders.DepartmentDao import DepartmentDAO
from .orders.SupermarketAddressDao import SupermarketAddressDAO
from .orders.PanelManufacturerDao import PanelManufacturerDAO
from .orders.PanelDao import PanelDAO
from .orders.PanelVideoDao import PanelVideoDAO
from .orders.ResolutionDao import ResolutionDAO
from .orders.ScreenSizeDao import ScreenSizeDAO
from .orders.RefreshRateDao import RefreshRateDAO
from .orders.TechnicalSpecificationsDao import TechnicalSpecificationsDAO

# Initialize DAOs for each entity
videoProducerDao = VideoProducerDAO()
brandDao = BrandDAO()
advertisementVideoDao = AdvertisementVideoDAO()
chainDao = ChainDAO()
supermarketDao = SupermarketDAO()
departmentDao = DepartmentDAO()
supermarketAddressDao = SupermarketAddressDAO()
panelManufacturerDao = PanelManufacturerDAO()
panelDao = PanelDAO()
panelVideoDao = PanelVideoDAO()
resolutionDao = ResolutionDAO()
screenSizeDao = ScreenSizeDAO()
refreshRateDao = RefreshRateDAO()
technicalSpecificationsDao = TechnicalSpecificationsDAO()
