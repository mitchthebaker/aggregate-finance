templates = {
  "swagger": "2.0",
  "paths": {
    "/": {
      "get": {
        "summary": "Root endpoint",
        "response": {
          "200": {
            "description": "An object displaying the hostname and port"
          }
        }
      }
    },
    "/plaid/access-token/{institution_id}": {
      "post": {
        "summary": "Retrieve a new access token from the Plaid API",
        "description": "This endpoint retrieves a new access token for the specified institution and initial products.",
        "parameters": [
          {
            "name": "institution_id",
            "in": "path",
            "description": "The ID of the institution the Item will be associated with.",
            "required": True,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "The products to initially pull for the Item. May be any products that the specified institution_id supports.",
          "required": True,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "initial_products": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                },
                "required": ["initial_products"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "JSON payload with access_token, item_id, and request_id.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "access_token": {
                      "type": "string",
                      "description": "Access token for the Item."
                    },
                    "item_id": {
                      "type": "string",
                      "description": "The ID of the Item."
                    },
                    "request_id": {
                      "type": "string",
                      "description": "The unique request ID for debugging purposes."
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "initial_products is required and must be a non-empty list.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "description": "Description of the error."
                    }
                  }
                },
                "example": {
                  "error": "initial_products is required and must be a non-empty list."
                }
              }
            }
          }
        },
        "tags": ["Plaid"]
      }
    },
    "/plaid/transactions-sync": {
      "get": {
        "summary": "Retrieve transactions for an institution",
        "description": "Retrieve transactions corresponding to an access token for a specific institution ID.",
        "responses": {
          "200": {
            "description": "JSON payload with added, modified, removed, and accounts.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "added": {
                      "type": "array",
                      "items": {
                        "type": "object"
                      },
                      "description": "List of added transactions."
                    },
                    "modified": {
                      "type": "array",
                      "items": {
                        "type": "object"
                      },
                      "description": "List of modified transactions."
                    },
                    "removed": {
                      "type": "array",
                      "items": {
                        "type": "object"
                      },
                      "description": "List of removed transactions."
                    },
                    "accounts": {
                      "type": "array",
                      "items": {
                        "type": "object"
                      },
                      "description": "Details of associated accounts."
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Missing Plaid access token.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "description": "Description of the error."
                    }
                  }
                },
                "example": {
                  "error": "Plaid access token is required."
                }
              }
            }
          },
          "500": {
            "description": "Error adding into transactions collection.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "description": "Details of the server error."
                    }
                  }
                },
                "example": {
                  "error": "Failed to insert transactions into the database."
                }
              }
            }
          }
        },
        "tags": ["Plaid"]
      }
    },
    "/db/collections": {
      "get": {
        "tags": ["Database"],
        "summary": "Fetch all collections",
        "description": "Fetch a list of all collections in the MongoDB database.",
        "responses": {
          "200": {
            "description": "Successfully retrieved the list of collections.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "description": "Name of a collection in the database."
                  }
                },
                "example": [
                  "users",
                  "transactions",
                  "accounts"
                ]
              }
            }
          },
          "500": {
            "description": "Internal Server Error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "description": "Details of the server error."
                    }
                  }
                },
                "example": {
                  "error": "Failed to fetch collections from the database."
                }
              }
            }
          }
        }
      }
    },
    "/db/collections/{collection_name}": {
      "get": {
        "tags": ["Database"],
        "summary": "Fetch all documents from a collection",
        "description": "Fetch all documents from a MongoDB collection.",
        "parameters": [
          {
            "in": "path",
            "name": "collection_name",
            "required": True,
            "description": "The name of the MongoDB collection to query.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved all documents.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "description": "A single document from the collection."
                  }
                },
                "example": [
                  {
                    "_id": "64a6b7c1e25b3456abcd1234",
                    "field1": "value1",
                    "field2": "value2"
                  },
                  {
                    "_id": "64a6b7c1e25b3456abcd5678",
                    "field1": "value3",
                    "field2": "value4"
                  }
                ]
              }
            }
          },
          "500": {
            "description": "Server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "description": "Details of the server error."
                    }
                  }
                },
                "example": {
                  "error": "Failed to retrieve documents from the collection."
                }
              }
            }
          }
        }
      }
    },
    "/google-api/spreadsheet/{spreadsheet_id}": {
      "get": {
        "tags": ["Google API"],
        "summary": "Get a Google spreadsheet by ID",
        "description": "Get a Google spreadsheet by ID",
        "parameters": [
          {
            "in": "path",
            "name": "spreadsheet_id",
            "required": True,
            "description": "The spreadsheet ID (can be found in url)",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved all documents.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "description": "A single document from the collection."
                  }
                },
                "example": [
                  {
                    "_id": "64a6b7c1e25b3456abcd1234",
                    "field1": "value1",
                    "field2": "value2"
                  },
                ]
              }
            }
          },
          "500": {
            "description": "Server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "description": "Details of the server error."
                    }
                  }
                },
                "example": {
                  "error": "Failed to retrieve documents from the collection."
                }
              }
            }
          }
        }
      }
    }
  }
}
