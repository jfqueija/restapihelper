#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import requests
from requests.auth import HTTPBasicAuth
import json
import urllib

class Common(object):
    """
        Common class contains common functions or methods.
    """
    
    def __init__(self,log,calledFrom=None):
        """
            Class constructor
            :param log, logger class send by principal call. It's required.
            :param calledFrom: string. Name of app that call library.
        """
        self.__log = log
        self.__inheritedFrom = calledFrom

    def refreshToken(self,refreshEndpoint:str, clientKey:str, clientSecret:str,*args, **kwargs):
        """
            Public function used for refresh token using client credentials
            :param refreshEndpoint, refresh url
            :param clientKey, client key
            :param clientSecret, client secret
            :result access_token or None.
        """   
        try:            
            response = requests.post(url=refreshEndpoint,data=self.__doGrantType(), verify=True, allow_redirects=False, auth=(clientKey, clientSecret),*args, **kwargs)
            if response.status_code == 200:
                self.__log.debug(msg='Finished Execution.',extra=self.doExtraLogger(appName='RestApiHelper',methodName='refreshToken',
                        className='Common',inheritedFrom=self.__inheritedFrom,kwargs={'StatusCode':response.status_code}))
                token = json.loads(response.text)
                result = token['access_token']
            else:
                self.__log.error(msg="Failed execution",extra=self.doExtraLogger(appName='RestApiHelper',methodName='refreshToken',
                        className='Common',inheritedFrom=self.__inheritedFrom,kwargs={'StatusCode':response.status_code,'ErrorCall':response.text}))
                result = None
        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.doExtraLogger(appName='RestApiHelper',methodName='refreshToken',
                    className='Common',inheritedFrom=self.__inheritedFrom))
            result = None
        return result

    def doHeadersBearer(self,token:str):
        """
            Public method used for construct header based in bearer authorization.
            :param token str
        """
        result = None
        try:            
            result = {'Content-type': 'application/json', 'Authorization': 'Bearer %s' %  token}
        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.doExtraLogger(appName='RestApiHelper',methodName='doHeadersBearer',
                    className='Common',inheritedFrom=self.__inheritedFrom))
        return result
    
    def buildUrl(self,endpointPath,endpointMethods,arguments):
        """
            Public method used build final url.
            :param endpointPath: str. Endpoint path. Sample: https://contoso.com/api/v1
            :param endpointMethods: str. Endpoint methods. Sample: customer/
            :param arguments: list. List of arguments used in verbs get or delete
        """
        result = None
        try:            
            uri = [endpointPath]
            for m in endpointMethods:
                uri.append(str(m))
            result = "/".join(uri)
            if arguments:      
                result = result + "?" + urllib.parse.urlencode(arguments)
        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.doExtraLogger(appName='RestApiHelper',methodName='buildUrl',
                    className='Common',inheritedFrom=self.__inheritedFrom))
        return result

    def doExtraLogger(self,appName:str,methodName:str,className:str,inheritedFrom:str,*args, **kwargs):
        """
            Public method used for construct dictionary with extra information send to logger.
            :param appName: string
            :param methodName: string
            :param className: string
            :param inheritedFrom: string
            :param args: extra data
            :param kwargs: extra dictionary
        """
        extra = dict()
        extra["AppName"] = appName
        extra["Class"] = className
        extra["Method"] = methodName
        extra["inheritedFrom"] = inheritedFrom
        if kwargs:
            extra.update(kwargs['kwargs'])
        return extra

    def __doGrantType(self):
        """
            Private method used for declare grant type.            
        """
        result = None
        try:            
            result = {'grant_type': 'client_credentials'}
        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.doExtraLogger(appName='RestApiHelper',methodName='__doGrantType',
                    className='Common',inheritedFrom=self.__inheritedFrom))
        return result