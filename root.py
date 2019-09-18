# -*- coding: utf-8 -*-
"""This module contains an empty application container.
It is defined here to avoid circular imports
"""
from mindmeld import Application
from ewsrestgatewayclient.ebo import EBO
from chuck_core import se_handler

se_office_manager = EBO()
se_token = se_office_manager.token.get_token("Admin", "P@ssword")
se_auth = se_office_manager.root.retrieve(custom_headers={'Authorization':'Bearer ' + se_token.access_token})

app = Application(__name__)

__all__ = ['app', 'se_office_manager', 'se_token', 'se_auth', 'se_handler']
