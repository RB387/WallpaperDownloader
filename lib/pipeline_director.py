from dataclasses import dataclass
import logging
import asyncio
from abc import ABC, abstractmethod
from typing import Tuple, Any, Dict, List
from lib.storage import AbstractStorage


@dataclass
class AbstractPipelineStep(ABC):
    """
    Abstract class for Pipeline step
    Must implement `get_workers_tasks` method
    that should return list of AsyncIO tasks

    Instances of this class are used in PipelineDirector

    Properties:
        :config: Dictionary with configuration for this step
        :storage: Any AbstractStorage instance
    """

    config: Dict[str, Any]
    storage: AbstractStorage

    @abstractmethod
    async def get_workers_tasks(self) -> List[asyncio.Task]:
        raise NotImplementedError


@dataclass
class AbstractPipelineDirector(ABC):
    """
    Abstract class of Pipeline Director
    that executes Pipelines steps
    Must implement private `_get_pipeline_steps` method
    that should return tuple of Pipeline steps

    Use `start_pipeline` to execute all pipelines

    Properties:
        :config: Dictionary with configuration for pipelines
    """

    config: Dict[str, Any]

    async def start_pipeline(self):
        """
        Public method to run all pipelines from _get_pipeline_steps
        :return: None
        """
        for pipeline_step in self.get_pipeline_steps():
            logging.info(f"Starting {pipeline_step.__class__.__name__}")

            tasks = await pipeline_step.get_workers_tasks()
            logging.info(f"Workers count: {len(tasks)}")
            await asyncio.gather(*tasks)

            logging.info(f"Finished {pipeline_step.__class__.__name__}")

    @abstractmethod
    def get_pipeline_steps(self) -> Tuple[AbstractPipelineStep]:
        raise NotImplementedError
