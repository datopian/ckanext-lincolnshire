import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import routes.mapper


class LincolnshirePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'lincolnshire')

    # IRoutes

    def before_map(self, map):
        controller = 'ckanext.lincolnshire.controller:CustomPackageController'
        with routes.mapper.SubMapper(map, controller=controller) as m:
            m.connect('search', '/dataset', action='search',
                      highlight_actions='index search')

        controller = 'ckanext.lincolnshire.controller:CustomGroupController'
        with routes.mapper.SubMapper(map, controller=controller) as m:
            m.connect('group_read', '/group/{id}', action='read',
                      ckan_icon='sitemap')
        return map

    def after_map(self, map):
        return map
