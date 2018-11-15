from plone import api


def run_pre_migration(context):
    """ Use this for any steps that need to be done before the migration

        Example for disabling a subscriber:
        
        for subscriber:
        <subscriber
            for="plone.app.contenttypes.interfaces.IDocument
               zope.lifecycleevent.interfaces.IObjectModifiedEvent"
            handler=".events.subscriber_name"
            />
        
        from zope.component import getGlobalSiteManager
        gsm = getGlobalSiteManager()
        gsm.unregisterHandler(
            subscriber_name, (IDocument, IObjectModifiedEvent))
    """


def run_migration(context):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runAllImportStepsFromProfile(
        'profile-ploneconf.migration.import:import_content')


def run_post_migration(context):
    """ Use this for any steps that need to be done after the migration
        To go with the pre_migration example,
        you can re-register a subscriber:
        gsm.registerHandler(subscriber_name, (IDocument, IObjectModifiedEvent)
    """