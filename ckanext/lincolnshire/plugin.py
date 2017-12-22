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
        with routes.mapper.SubMapper(map, controller='group') as m:
                m.connect('group_index', '/group', action='index',
                          highlight_actions='index search')
                m.connect('group_list', '/group/list', action='list')
                m.connect('group_new', '/group/new', action='new')
                m.connect('group_action', '/group/{action}/{id}',
                          requirements=dict(action='|'.join([
                              'edit',
                              'delete',
                              'member_new',
                              'member_delete',
                              'history',
                              'followers',
                              'follow',
                              'unfollow',
                              'admins',
                              'activity',
                          ])))
                m.connect('group_about', '/group/about/{id}', action='about',
                          ckan_icon='info-sign'),
                m.connect('group_edit', '/group/edit/{id}', action='edit',
                          ckan_icon='edit')
                m.connect('group_members', '/group/members/{id}', action='members',
                          ckan_icon='group'),
                m.connect('group_activity', '/group/activity/{id}/{offset}',
                          action='activity', ckan_icon='time'),
                m.connect('group_read', '/group/{id}', action='read',
                          ckan_icon='sitemap')
        return map


    def after_map(self, map):
        return map
