import sys

from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

from hexagon.cli.args import fill_args
from hexagon.cli.tracer import tracer
from hexagon.cli.printer import log

from typing import Any, Dict, List


def main(
        tool: Dict[str, Any],
        env: Dict[str, Any] = None,
        env_args: Any = None,
        cli_args: List[Any] = None,
):
    """
    All hexagon tools must define a main function

    :param cli_args:
    :param env:
    :param tool:
    :param env_args: the values expected to receive from tool.envs
    :return:
    """

    log.info('Your selected tool is:')
    log.example(tool)

    log.info('Your selected env is:')
    log.example(env)

    log.info('Value in tool.envs[env_name]:')
    log.example(env_args)

    if cli_args:
        log.info('Extra command line arguments:')
        log.example(cli_args)

    # for now this is the way of obtaining other execution arguments (tool name, env name, etc)
    _, _tool_name, _env_name, _my_name = fill_args(sys.argv, 4)

    # tracer.tracing is the way of letting hexagon know you asked the user for a parameter for your tool.
    # this let's hexagon build the "To repeat this command" message correctly
    name = tracer.tracing(_my_name or inquirer.text(
        message="What's your name?",
        validate=EmptyInputValidator("Please enter your name.")
    ).execute())

    log.result(f'Your name is: {name}')
