import os
from datetime import datetime


def get_config(**parametrized_config) -> dict:
    """
    :param parametrized_config: kwargs with parametrized arguments for pipelines
    :return: Returns config dictionary for pipelines
    """
    return {
        'files_path': os.path.join(os.getcwd(), f'wallpapers_{datetime.now().isoformat()}'),
        **parametrized_config,
    }
