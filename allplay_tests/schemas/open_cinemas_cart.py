click_cinema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "category_id": {
          "type": "integer"
        },
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "budget": {
          "type": "string"
        },
        "slogan": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "quality": {
          "type": "string"
        },
        "is_3d": {
          "type": "boolean"
        },
        "is_serial": {
          "type": "boolean"
        },
        "is_cartoon": {
          "type": "boolean"
        },
        "file_count": {
          "type": "integer"
        },
        "trailers_count": {
          "type": "integer"
        },
        "rating_allplay": {
          "type": "number"
        },
        "rating_count_allplay": {
          "type": "integer"
        },
        "rating_imdb": {
          "type": "number"
        },
        "rating_count_imdb": {
          "type": "integer"
        },
        "age": {
          "type": "integer"
        },
        "is_free": {
          "type": "boolean"
        },
        "est_price": {
          "type": "integer"
        },
        "tvod_price": {
          "type": "integer"
        },
        "langs": {
          "type": "null"
        },
        "in_cinema_till": {
          "type": "null"
        },
        "published_at": {
          "type": "string"
        },
        "available_at": {
          "type": "null"
        },
        "comments_count": {
          "type": "integer"
        },
        "title_orig": {
          "type": "string"
        },
        "url": {
          "type": "string"
        },
        "slug": {
          "type": "string"
        },
        "rating_kp": {
          "type": "number"
        },
        "rating_count_kp": {
          "type": "integer"
        },
        "is_new": {
          "type": "boolean"
        },
        "featured": {
          "type": "null"
        },
        "required_services": {
          "type": "array",
          "items": [
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            },
            {
              "type": "integer"
            }
          ]
        },
        "tvod_days": {
          "type": "integer"
        },
        "score": {
          "type": "number"
        },
        "localized_description": {
          "type": "string"
        },
        "poster": {
          "type": "object",
          "properties": {
            "url_100x100": {
              "type": "string"
            },
            "url_340x450": {
              "type": "string"
            },
            "url_680x900": {
              "type": "string"
            }
          },
          "required": [
            "url_100x100",
            "url_340x450",
            "url_680x900"
          ]
        },
        "genres": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "localized_name": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "localized_name"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "localized_name": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "localized_name"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "localized_name": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "localized_name"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "localized_name": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "localized_name"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "localized_name": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "localized_name"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "localized_name": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "localized_name"
              ]
            }
          ]
        },
        "countries": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "localized_name": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "localized_name"
              ]
            }
          ]
        },
        "actors": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "object",
                  "properties": {
                    "url_100x100": {
                      "type": "string"
                    },
                    "url_200x300": {
                      "type": "string"
                    },
                    "url_200x200": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "url_100x100",
                    "url_200x300",
                    "url_200x200"
                  ]
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "object",
                  "properties": {
                    "url_100x100": {
                      "type": "string"
                    },
                    "url_200x300": {
                      "type": "string"
                    },
                    "url_200x200": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "url_100x100",
                    "url_200x300",
                    "url_200x200"
                  ]
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "object",
                  "properties": {
                    "url_100x100": {
                      "type": "string"
                    },
                    "url_200x300": {
                      "type": "string"
                    },
                    "url_200x200": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "url_100x100",
                    "url_200x300",
                    "url_200x200"
                  ]
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "null"
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "object",
                  "properties": {
                    "url_100x100": {
                      "type": "string"
                    },
                    "url_200x300": {
                      "type": "string"
                    },
                    "url_200x200": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "url_100x100",
                    "url_200x300",
                    "url_200x200"
                  ]
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "null"
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "object",
                  "properties": {
                    "url_100x100": {
                      "type": "string"
                    },
                    "url_200x300": {
                      "type": "string"
                    },
                    "url_200x200": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "url_100x100",
                    "url_200x300",
                    "url_200x200"
                  ]
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "null"
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "null"
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num",
                    "description"
                  ]
                },
                "poster": {
                  "type": "null"
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            }
          ]
        },
        "directors": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num"
                  ]
                },
                "poster": {
                  "type": "object",
                  "properties": {
                    "url_100x100": {
                      "type": "string"
                    },
                    "url_200x300": {
                      "type": "string"
                    },
                    "url_200x200": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "url_100x100",
                    "url_200x300",
                    "url_200x200"
                  ]
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "used_count": {
                  "type": "integer"
                },
                "localized_name": {
                  "type": "string"
                },
                "pivot": {
                  "type": "object",
                  "properties": {
                    "movie_id": {
                      "type": "integer"
                    },
                    "person_id": {
                      "type": "integer"
                    },
                    "num": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "movie_id",
                    "person_id",
                    "num"
                  ]
                },
                "poster": {
                  "type": "null"
                }
              },
              "required": [
                "id",
                "name",
                "used_count",
                "localized_name",
                "pivot",
                "poster"
              ]
            }
          ]
        },
        "published_bg": {
          "type": "null"
        }
      },
      "required": [
        "id",
        "category_id",
        "title",
        "description",
        "budget",
        "slogan",
        "year",
        "quality",
        "is_3d",
        "is_serial",
        "is_cartoon",
        "file_count",
        "trailers_count",
        "rating_allplay",
        "rating_count_allplay",
        "rating_imdb",
        "rating_count_imdb",
        "age",
        "is_free",
        "est_price",
        "tvod_price",
        "langs",
        "in_cinema_till",
        "published_at",
        "available_at",
        "comments_count",
        "title_orig",
        "url",
        "slug",
        "rating_kp",
        "rating_count_kp",
        "is_new",
        "featured",
        "required_services",
        "tvod_days",
        "score",
        "localized_description",
        "poster",
        "genres",
        "countries",
        "actors",
        "directors",
        "published_bg"
      ]
    },
    "meta": {
      "type": "object",
      "properties": {
        "t_ms": {
          "type": "number"
        }
      },
      "required": [
        "t_ms"
      ]
    }
  },
  "required": [
    "data",
    "meta"
  ]
}