"""
Violation:
Use '.exception' over '.error' inside except blocks
"""

import logging
import sys

logger = logging.getLogger(__name__)


def bad():
    try:
        a = 1
    except Exception:
        logging.error("Context message here")

        if True:
            logging.error("Context message here")


def bad():
    try:
        a = 1
    except Exception:
        logger.error("Context message here")

        if True:
            logger.error("Context message here")


def bad():
    try:
        a = 1
    except Exception:
        log.error("Context message here")

        if True:
            log.error("Context message here")


def bad():
    try:
        a = 1
    except Exception:
        self.logger.error("Context message here")

        if True:
            self.logger.error("Context message here")


def good():
    try:
        a = 1
    except Exception:
        logger.exception("Context message here")


def good():
    try:
        a = 1
    except Exception:
        foo.exception("Context message here")


def fine():
    try:
        a = 1
    except Exception:
        logger.error("Context message here", exc_info=True)


def fine():
    try:
        a = 1
    except Exception:
        logger.error("Context message here", exc_info=sys.exc_info())


from logging import error, exception


def bad():
    try:
        a = 1
    except Exception:
        error("Context message here")

        if True:
            error("Context message here")


def good():
    try:
        a = 1
    except Exception:
        exception("Context message here")


def fine():
    try:
        a = 1
    except Exception:
        error("Context message here", exc_info=True)


def fine():
    try:
        a = 1
    except Exception:
        error("Context message here", exc_info=sys.exc_info())


def nested():
    try:
        a = 1
    except Exception:
        try:
            b = 2
        except Exception:
            error("Context message here")
