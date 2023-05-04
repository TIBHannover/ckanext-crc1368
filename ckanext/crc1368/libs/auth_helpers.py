# encoding: utf-8

import ckan.plugins.toolkit as toolkit
import ckan.model as model
import ckan.logic as logic


class AuthHelpers:

    @staticmethod
    def check_access_show_package(package_id):
        context = {'user': toolkit.g.user, 'auth_user_obj': toolkit.g.userobj}
        data_dict = {'id':package_id}
        try:
            toolkit.check_access('package_show', context, data_dict)
            return True

        except toolkit.NotAuthorized:
            return False
    

    @staticmethod
    def check_access_show_resource(resource_id):
        context = {'user': toolkit.g.user, 'auth_user_obj': toolkit.g.userobj}        
        try:
            toolkit.check_access('resource_show', context, {'id':resource_id})            
            return True
        except toolkit.NotAuthorized:
            return False



    @staticmethod
    def get_mediaWiki_creds():
        credentials_path = toolkit.config.get('ckanext.mediaWiki_credentials_path')        
        try:
            credentials = open(credentials_path, 'r').read()
            credentials = credentials.split('\n')
            username = credentials[0].split('=')[1]
            password = credentials[1].split('=')[1]
            return {"username": username, "password": password}
           
        except:
            return {}
    

    @staticmethod
    def abort_if_not_admin():
        context = {'model': model,
                   'user': toolkit.g.user, 'auth_user_obj': toolkit.g.userobj}
        try:
            logic.check_access('sysadmin', context, {})
        except logic.NotAuthorized:
            toolkit.abort(404, 'Not Found')