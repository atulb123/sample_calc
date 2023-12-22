import datetime
import json
import logging
import os
import random
import time

import pytest

cli_arg = {}
main_session = None
logger = None



@pytest.fixture(scope="session", autouse=True)
def set_logger_object():
    global logger
    os.makedirs("logging", exist_ok=True)
    logger = logging.getLogger('CALC Logger')
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), "logging", "CALC.log"), mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


@pytest.fixture(scope="session", autouse=True)
def cli_args(request):
    """global parameters initialization"""
    cli_arg["url"] = request.config.getoption("--url")




def pytest_addoption(parser):
    """configuring command liheadlessne arguments"""
    parser.addoption("--url", default="qa", help="pass environment info")



@pytest.fixture(scope="function", autouse=True)
def set_main_session(request):
    logger.info("Setting Session Object")
    yield


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    """pytest report generation utility methods"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
