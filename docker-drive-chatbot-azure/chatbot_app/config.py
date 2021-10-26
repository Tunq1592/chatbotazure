#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "5a989b4c-904d-43f0-8490-123017614709")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "sKz7Q~Dey8gzXlGxJHB6v1s5DKq2xPyk4uZ06")
