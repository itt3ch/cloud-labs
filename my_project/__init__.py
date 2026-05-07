"""
2022
apavelchak@gmail.com
Â© Andrii Pavelchak
"""

import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flasgger import Swagger
from flask import Flask, jsonify
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from my_project.auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

db = SQLAlchemy()

todos = {}


def create_simple_entity_paths(entity_path: str, entity_name: str, tag_name: str) -> Dict[str, Any]:
    """
    Create standard CRUD paths for simple entities
    """
    return {
        f"/{entity_path}": {
            "get": {
                "tags": [tag_name],
                "summary": f"Get all {entity_name.lower()}s",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/SimpleEntity"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": [tag_name],
                "summary": f"Create a new {entity_name.lower()}",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SimpleEntityInput"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": f"{entity_name} created successfully",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/SimpleEntity"}
                            }
                        }
                    }
                }
            }
        },
        f"/{entity_path}/{{{entity_name.lower()}_id}}": {
            "get": {
                "tags": [tag_name],
                "summary": f"Get {entity_name.lower()} by ID",
                "parameters": [
                    {
                        "name": f"{entity_name.lower()}_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/SimpleEntity"}
                            }
                        }
                    },
                    "404": {"description": f"{entity_name} not found"}
                }
            },
            "put": {
                "tags": [tag_name],
                "summary": f"Update {entity_name.lower()}",
                "parameters": [
                    {
                        "name": f"{entity_name.lower()}_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SimpleEntityInput"}
                        }
                    }
                },
                "responses": {
                    "200": {"description": f"{entity_name} updated successfully"},
                    "404": {"description": f"{entity_name} not found"}
                }
            },
            "delete": {
                "tags": [tag_name],
                "summary": f"Delete {entity_name.lower()}",
                "parameters": [
                    {
                        "name": f"{entity_name.lower()}_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "204": {"description": f"{entity_name} deleted successfully"},
                    "404": {"description": f"{entity_name} not found"}
                }
            }
        }
    }


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    :return: Flask application object
    """
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)
    register_routes(app)
    init_autodoc_swagger(app)

    @app.route("/")
    def index():
        """Redirect to Swagger documentation"""
        from flask import redirect
        return redirect("/apidocs/")

    return app


def init_autodoc_swagger(app: Flask) -> None:
    """
    Initialize comprehensive Swagger documentation for all API routes
    """
    app.config.setdefault("SWAGGER", {
        "uiversion": 3,
        "title": "Supermarket Display Management API",
        "openapi": "3.0.3",
    })

    swagger_template = {
        "openapi": "3.0.3",
        "info": {
            "title": "Supermarket Display Management API",
            "version": "1.0.0",
            "description": "A comprehensive API for managing supermarket display panels, advertisements, and related entities",
            "contact": {"name": "Andrii Pavelchak", "email": "apavelchak@gmail.com"},
            "license": {"name": "MIT"},
        },
        "servers": [
            {"url": "/", "description": "Local development server"}
        ],
        "components": {
            "schemas": {
                "Brand": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True, "description": "Brand ID"},
                        "name": {"type": "string", "description": "Brand name", "example": "Samsung"}
                    },
                    "required": ["name"]
                },
                "BrandInput": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Brand name", "example": "Samsung"}
                    },
                    "required": ["name"]
                },
                
                "Supermarket": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True, "description": "Supermarket ID"},
                        "name": {"type": "string", "description": "Supermarket name", "example": "Metro Store #1"},
                        "chain_id": {"type": "integer", "description": "Chain ID", "example": 1},
                        "chain": {"$ref": "#/components/schemas/Chain"},
                        "area": {"type": "number", "format": "float", "description": "Area in square meters", "example": 1500.50},
                        "opening_time": {"type": "string", "description": "Opening time (HH:MM:SS)", "example": "08:00:00"},
                        "closing_time": {"type": "string", "description": "Closing time (HH:MM:SS)", "example": "22:00:00"},
                        "average_visitors": {"type": "integer", "description": "Average visitors per day", "example": 500}
                    },
                    "required": ["name"]
                },
                "SupermarketInput": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Supermarket name", "example": "Metro Store #1"},
                        "chain_id": {"type": "integer", "description": "Chain ID", "example": 1},
                        "area": {"type": "number", "format": "float", "description": "Area in square meters", "example": 1500.50},
                        "opening_time": {"type": "string", "description": "Opening time (HH:MM:SS)", "example": "08:00:00"},
                        "closing_time": {"type": "string", "description": "Closing time (HH:MM:SS)", "example": "22:00:00"},
                        "average_visitors": {"type": "integer", "description": "Average visitors per day", "example": 500}
                    },
                    "required": ["name"]
                },
                
                "AdvertisementVideo": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True, "description": "Advertisement Video ID"},
                        "name": {"type": "string", "description": "Video name", "example": "Summer Sale Ad"},
                        "duration": {"type": "string", "description": "Duration (HH:MM:SS)", "example": "00:00:30"},
                        "producer_id": {"type": "integer", "description": "Video producer ID", "example": 1},
                        "brand_id": {"type": "integer", "description": "Brand ID", "example": 1}
                    },
                    "required": ["name", "duration"]
                },
                "AdvertisementVideoInput": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Video name", "example": "Summer Sale Ad"},
                        "duration": {"type": "string", "description": "Duration (HH:MM:SS)", "example": "00:00:30"},
                        "producer_id": {"type": "integer", "description": "Video producer ID", "example": 1},
                        "brand_id": {"type": "integer", "description": "Brand ID", "example": 1}
                    },
                    "required": ["name", "duration"]
                },
                
                "Panel": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True, "description": "Panel ID"},
                        "quantity": {"type": "integer", "description": "Panel quantity", "example": 5},
                        "department_id": {"type": "integer", "description": "Department ID", "example": 1},
                        "manufacturer_id": {"type": "integer", "description": "Manufacturer ID", "example": 1}
                    },
                    "required": ["quantity"]
                },
                "PanelInput": {
                    "type": "object",
                    "properties": {
                        "quantity": {"type": "integer", "description": "Panel quantity", "example": 5},
                        "department_id": {"type": "integer", "description": "Department ID", "example": 1},
                        "manufacturer_id": {"type": "integer", "description": "Manufacturer ID", "example": 1}
                    },
                    "required": ["quantity"]
                },
                
                "TechnicalSpecifications": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True, "description": "Technical Specifications ID"},
                        "panel_id": {"type": "integer", "description": "Panel ID", "example": 1},
                        "resolution_id": {"type": "integer", "description": "Resolution ID", "example": 1},
                        "screen_size_id": {"type": "integer", "description": "Screen size ID", "example": 1},
                        "refresh_rate_id": {"type": "integer", "description": "Refresh rate ID", "example": 1}
                    },
                    "required": ["panel_id", "resolution_id", "screen_size_id", "refresh_rate_id"]
                },
                "TechnicalSpecificationsInput": {
                    "type": "object",
                    "properties": {
                        "panel_id": {"type": "integer", "description": "Panel ID", "example": 1},
                        "resolution_id": {"type": "integer", "description": "Resolution ID", "example": 1},
                        "screen_size_id": {"type": "integer", "description": "Screen size ID", "example": 1},
                        "refresh_rate_id": {"type": "integer", "description": "Refresh rate ID", "example": 1}
                    },
                    "required": ["panel_id", "resolution_id", "screen_size_id", "refresh_rate_id"]
                },
                
                "SupermarketAddress": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True, "description": "Supermarket Address ID"},
                        "address": {"type": "string", "description": "Address", "example": "123 Main Street, City, State"},
                        "supermarket_id": {"type": "integer", "description": "Supermarket ID", "example": 1}
                    },
                    "required": ["address"]
                },
                "SupermarketAddressInput": {
                    "type": "object",
                    "properties": {
                        "address": {"type": "string", "description": "Address", "example": "123 Main Street, City, State"},
                        "supermarket_id": {"type": "integer", "description": "Supermarket ID", "example": 1}
                    },
                    "required": ["address"]
                },
                
                "PanelVideo": {
                    "type": "object",
                    "properties": {
                        "panel_id": {"type": "integer", "description": "Panel ID", "example": 1},
                        "video_id": {"type": "integer", "description": "Video ID", "example": 1}
                    },
                    "required": ["panel_id", "video_id"]
                },
                
                "SimpleEntity": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "readOnly": True, "description": "Entity ID"},
                        "name": {"type": "string", "description": "Entity name"}
                    },
                    "required": ["name"]
                },
                "SimpleEntityInput": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Entity name"}
                    },
                    "required": ["name"]
                },
                
                "Chain": {"$ref": "#/components/schemas/SimpleEntity"},
                "ChainInput": {"$ref": "#/components/schemas/SimpleEntityInput"},
                
                "Error": {
                    "type": "object",
                    "properties": {
                        "error": {"type": "string", "description": "Error message"}
                    }
                }
            },
            
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        },
        
        "paths": {},
        
        "tags": [
            {"name": "Brands", "description": "Brand management operations"},
            {"name": "Supermarkets", "description": "Supermarket management operations"},
            {"name": "Advertisement Videos", "description": "Advertisement video management operations"},
            {"name": "Panels", "description": "Panel management operations"},
            {"name": "Technical Specifications", "description": "Technical specifications management"},
            {"name": "Chains", "description": "Chain management operations"},
            {"name": "Departments", "description": "Department management operations"},
            {"name": "Panel Manufacturers", "description": "Panel manufacturer operations"},
            {"name": "Refresh Rates", "description": "Refresh rate operations"},
            {"name": "Resolutions", "description": "Resolution operations"},
            {"name": "Screen Sizes", "description": "Screen size operations"},
            {"name": "Video Producers", "description": "Video producer operations"},
            {"name": "Supermarket Addresses", "description": "Supermarket address operations"},
            {"name": "Panel Videos", "description": "Panel-video association operations"}
        ]
    }

    paths = swagger_template["paths"]
    
    paths.update({
        "/brand": {
            "get": {
                "tags": ["Brands"],
                "summary": "Get all brands",
                "description": "Retrieve a list of all brands",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/Brand"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Brands"],
                "summary": "Create a new brand",
                "description": "Create a new brand with the provided information",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/BrandInput"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Brand created successfully",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Brand"}
                            }
                        }
                    },
                    "400": {
                        "description": "Validation error",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            }
        },
        "/brand/{brand_id}": {
            "get": {
                "tags": ["Brands"],
                "summary": "Get brand by ID",
                "description": "Retrieve a specific brand by its ID",
                "parameters": [
                    {
                        "name": "brand_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                        "description": "Brand identifier"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Brand"}
                            }
                        }
                    },
                    "404": {
                        "description": "Brand not found",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": ["Brands"],
                "summary": "Update brand",
                "description": "Update a brand with new information",
                "parameters": [
                    {
                        "name": "brand_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                        "description": "Brand identifier"
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/BrandInput"}
                        }
                    }
                },
                "responses": {
                    "200": {"description": "Brand updated successfully"},
                    "404": {"description": "Brand not found"},
                    "400": {"description": "Validation error"}
                }
            },
            "delete": {
                "tags": ["Brands"],
                "summary": "Delete brand",
                "description": "Delete a brand by its ID",
                "parameters": [
                    {
                        "name": "brand_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                        "description": "Brand identifier"
                    }
                ],
                "responses": {
                    "204": {"description": "Brand deleted successfully"},
                    "404": {"description": "Brand not found"}
                }
            }
        },
        
        "/supermarket": {
            "get": {
                "tags": ["Supermarkets"],
                "summary": "Get all supermarkets",
                "description": "Retrieve a list of all supermarkets",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/Supermarket"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Supermarkets"],
                "summary": "Create a new supermarket",
                "description": "Create a new supermarket with the provided information",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SupermarketInput"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Supermarket created successfully",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Supermarket"}
                            }
                        }
                    },
                    "400": {"description": "Validation error"}
                }
            }
        },
        "/supermarket/{supermarket_id}": {
            "get": {
                "tags": ["Supermarkets"],
                "summary": "Get supermarket by ID",
                "parameters": [
                    {
                        "name": "supermarket_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                        "description": "Supermarket identifier"
                    }
                ],#12312sdf
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Supermarket"}
                            }
                        }
                    },
                    "404": {"description": "Supermarket not found"}
                }
            },
            "put": {
                "tags": ["Supermarkets"],
                "summary": "Update supermarket",
                "parameters": [
                    {
                        "name": "supermarket_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SupermarketInput"}
                        }
                    }
                },
                "responses": {
                    "200": {"description": "Supermarket updated successfully"},
                    "404": {"description": "Supermarket not found"}
                }
            },
            "delete": {
                "tags": ["Supermarkets"],
                "summary": "Delete supermarket",
                "parameters": [
                    {
                        "name": "supermarket_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "204": {"description": "Supermarket deleted successfully"},
                    "404": {"description": "Supermarket not found"}
                }
            }
        },
        
        "/advertisement-video": {
            "get": {
                "tags": ["Advertisement Videos"],
                "summary": "Get all advertisement videos",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/AdvertisementVideo"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Advertisement Videos"],
                "summary": "Create a new advertisement video",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/AdvertisementVideoInput"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Advertisement video created successfully",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/AdvertisementVideo"}
                            }
                        }
                    }
                }
            }
        },
        "/advertisement-video/{advertisement_video_id}": {
            "get": {
                "tags": ["Advertisement Videos"],
                "summary": "Get advertisement video by ID",
                "parameters": [
                    {
                        "name": "advertisement_video_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/AdvertisementVideo"}
                            }
                        }
                    },
                    "404": {"description": "Advertisement video not found"}
                }
            },
            "put": {
                "tags": ["Advertisement Videos"],
                "summary": "Update advertisement video",
                "parameters": [
                    {
                        "name": "advertisement_video_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/AdvertisementVideoInput"}
                        }
                    }
                },
                "responses": {
                    "200": {"description": "Advertisement video updated successfully"}
                }
            },
            "delete": {
                "tags": ["Advertisement Videos"],
                "summary": "Delete advertisement video",
                "parameters": [
                    {
                        "name": "advertisement_video_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "204": {"description": "Advertisement video deleted successfully"}
                }
            }
        },
        
        "/panel": {
            "get": {
                "tags": ["Panels"],
                "summary": "Get all panels",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/Panel"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Panels"],
                "summary": "Create a new panel",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/PanelInput"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Panel created successfully",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Panel"}
                            }
                        }
                    }
                }
            }
        },
        "/panel/{panel_id}": {
            "get": {
                "tags": ["Panels"],
                "summary": "Get panel by ID",
                "parameters": [
                    {
                        "name": "panel_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Panel"}
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": ["Panels"],
                "summary": "Update panel",
                "parameters": [
                    {
                        "name": "panel_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/PanelInput"}
                        }
                    }
                },
                "responses": {
                    "200": {"description": "Panel updated successfully"}
                }
            },
            "delete": {
                "tags": ["Panels"],
                "summary": "Delete panel",
                "parameters": [
                    {
                        "name": "panel_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "204": {"description": "Panel deleted successfully"}
                }
            }
        },
        
        "/technical-specifications": {
            "get": {
                "tags": ["Technical Specifications"],
                "summary": "Get all technical specifications",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/TechnicalSpecifications"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Technical Specifications"],
                "summary": "Create new technical specifications",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/TechnicalSpecificationsInput"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Technical specifications created successfully",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/TechnicalSpecifications"}
                            }
                        }
                    }
                }
            }
        },
        "/technical-specifications/{technical_specifications_id}": {
            "get": {
                "tags": ["Technical Specifications"],
                "summary": "Get technical specifications by ID",
                "parameters": [
                    {
                        "name": "technical_specifications_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/TechnicalSpecifications"}
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": ["Technical Specifications"],
                "summary": "Update technical specifications",
                "parameters": [
                    {
                        "name": "technical_specifications_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/TechnicalSpecificationsInput"}
                        }
                    }
                },
                "responses": {
                    "200": {"description": "Technical specifications updated successfully"}
                }
            },
            "delete": {
                "tags": ["Technical Specifications"],
                "summary": "Delete technical specifications",
                "parameters": [
                    {
                        "name": "technical_specifications_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "204": {"description": "Technical specifications deleted successfully"}
                }
            }
        },
        
        "/supermarket-address": {
            "get": {
                "tags": ["Supermarket Addresses"],
                "summary": "Get all supermarket addresses",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/SupermarketAddress"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Supermarket Addresses"],
                "summary": "Create a new supermarket address",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SupermarketAddressInput"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Supermarket address created successfully",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/SupermarketAddress"}
                            }
                        }
                    }
                }
            }
        },
        "/supermarket-address/{supermarket_address_id}": {
            "get": {
                "tags": ["Supermarket Addresses"],
                "summary": "Get supermarket address by ID",
                "parameters": [
                    {
                        "name": "supermarket_address_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/SupermarketAddress"}
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": ["Supermarket Addresses"],
                "summary": "Update supermarket address",
                "parameters": [
                    {
                        "name": "supermarket_address_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SupermarketAddressInput"}
                        }
                    }
                },
                "responses": {
                    "200": {"description": "Supermarket address updated successfully"}
                }
            },
            "delete": {
                "tags": ["Supermarket Addresses"],
                "summary": "Delete supermarket address",
                "parameters": [
                    {
                        "name": "supermarket_address_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "204": {"description": "Supermarket address deleted successfully"}
                }
            }
        },
        
        "/panel-video": {
            "get": {
                "tags": ["Panel Videos"],
                "summary": "Get all panel-video associations",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/PanelVideo"}
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Panel Videos"],
                "summary": "Create a new panel-video association",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/PanelVideo"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Panel-video association created successfully",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/PanelVideo"}
                            }
                        }
                    }
                }
            }
        }
    })
    
    simple_entities = [
        ("chain", "Chain", "Chains"),
        ("department", "Department", "Departments"),
        ("panel-manufacturer", "PanelManufacturer", "Panel Manufacturers"),
        ("refresh-rate", "RefreshRate", "Refresh Rates"),
        ("resolution", "Resolution", "Resolutions"),
        ("screen-size", "ScreenSize", "Screen Sizes"),
        ("video-producer", "VideoProducer", "Video Producers")
    ]
    
    for entity_path, entity_name, tag_name in simple_entities:
        paths.update(create_simple_entity_paths(entity_path, entity_name, tag_name))

    Swagger(app, template=swagger_template)


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes input configuration
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    """
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    pass
