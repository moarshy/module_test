#!/usr/bin/env python

from module_test.schemas import InputSchema
from module_test.utils import get_logger


logger = get_logger(__name__)


def run(inputs: InputSchema, worker_nodes = None, orchestrator_node = None, flow_run = None, cfg: dict = None):
    logger.info(f"Running with inputs {inputs.prompt}")
    logger.info(f"cfg: {cfg}")

    prompt = inputs.prompt
    modified_prompt = f"{prompt} + second version"

    return modified_prompt


if __name__ == "__main__":
    import module_test
    print(module_test.__version__)
    run(InputSchema(prompt="Hello, world!"))

