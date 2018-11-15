# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ploneconf.migration.testing import PLONECONF_MIGRATION_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf.migration is properly installed."""

    layer = PLONECONF_MIGRATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf.migration is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneconf.migration'))

    def test_browserlayer(self):
        """Test that IPloneconfMigrationLayer is registered."""
        from ploneconf.migration.interfaces import (
            IPloneconfMigrationLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneconfMigrationLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONECONF_MIGRATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['ploneconf.migration'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ploneconf.migration is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneconf.migration'))

    def test_browserlayer_removed(self):
        """Test that IPloneconfMigrationLayer is removed."""
        from ploneconf.migration.interfaces import \
            IPloneconfMigrationLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneconfMigrationLayer,
            utils.registered_layers())
