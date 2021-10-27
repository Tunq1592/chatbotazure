#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "444217b8-a823-493e-8ee2-afd07ccc796d")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "5T57Q~dl8p7hnRfx~jokpGzi.b_QoaIg-LOZs")
