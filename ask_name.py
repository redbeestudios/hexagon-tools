import sys

from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

from hexagon.cli.args import fill_args
from hexagon.cli.tracer import tracer
from hexagon.cli.printer import log


def main(env_values):
    """
    All hexagon tools must define a main function

    :param env_values: the values expected to receive from tool.envs
    :return:
    """

    log.info('Value in tool.envs[env_name]:')
    log.example(env_values)

    # for now this is the way of obtaining other execution arguments (tool name, env name, etc)
    _, _tool_name, _env_name, _my_name = fill_args(sys.argv, 4)

    # tracer.tracing is the way of letting hexagon know you asked the user for a parameter for your tool.
    # this let's hexagon build the "To repeat this command" message correctly
    name = tracer.tracing(_my_name or inquirer.text(
        message="What's your name?",
        validate=EmptyInputValidator("Please enter your name.")
    ).execute())

    log.result('Your name is:', name)
