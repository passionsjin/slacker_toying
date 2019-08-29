
LOGCONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
        },

        "info_file_handler": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "default",
            "filename": "log/test_.log"
        },
        "slack_handler": {
            "class": "slacker_log_handler.SlackerLogHandler",
            "level": "WARNING",
            "api_key": "xoxb-707533402582-707555674182-4IzzBXtLwPqNseiUSbu11s8V",
            "channel": "#dev",
            "stack_trace": True,
            "formatter": "default",
        }
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["console", "info_file_handler", "slack_handler"],
    },
    "loggers": {
        "dev": {
            "level": "DEBUG",
            "handlers": ["console", "info_file_handler"],
            "propagate": 0,
            "handlers[1].filename": "log/test_dev.log"
        },
        "prod": {
            "level": "INFO",
            "handlers": ["console", "info_file_handler", "slack_handler"],
            "propagate": 0,
            "channel": "#dev",
            "filename": "log/test_prod.log"
        }
    }
}
