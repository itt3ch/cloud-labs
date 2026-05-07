"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each of your specific entities
    from .orders.BrandBlueprint import brand_bp
    from .orders.AdvertisementVideoBlueprint import advertisement_video_bp
    from .orders.ChainBlueprint import chain_bp
    from .orders.DepartmentBlueprint import department_bp
    from .orders.PanelBlueprint import panel_bp
    from .orders.PanelManufacturerBlueprint import panel_manufacturer_bp
    from .orders.PanelVideoBlueprint import panel_video_bp
    from .orders.RefreshRateBlueprint import refresh_rate_bp
    from .orders.ResolutionBlueprint import resolution_bp
    from .orders.SreenSizeBlueprint import screen_size_bp
    from .orders.SupermarketAddressBlueprint import supermarket_address_bp
    from .orders.SupermarketBlueprint import supermarket_bp
    from .orders.TechnicalSpecificationsBlueprint import technical_specifications_bp
    from .orders.VideoProducerBlueprint import video_producer_bp

    # Register each blueprint with the app
    app.register_blueprint(brand_bp)
    app.register_blueprint(advertisement_video_bp)
    app.register_blueprint(chain_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(panel_bp)
    app.register_blueprint(panel_manufacturer_bp)
    app.register_blueprint(panel_video_bp)
    app.register_blueprint(refresh_rate_bp)
    app.register_blueprint(resolution_bp)
    app.register_blueprint(screen_size_bp)
    app.register_blueprint(supermarket_address_bp)
    app.register_blueprint(supermarket_bp)
    app.register_blueprint(technical_specifications_bp)
    app.register_blueprint(video_producer_bp)
