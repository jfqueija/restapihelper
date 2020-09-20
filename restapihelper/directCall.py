#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import requests
import json

from restapihelper.common import Common as cm

class DirectCall(object):
    """
        This class contains functions or methods used for call to Http verbs. In this class, the methods don't use token or credentials.
    """
    def __init__(self,log,endpointPath,endpointMethods=None,arguments={},calledFrom=None):
        """
            Class constructor
            :param log, logger class send by principal call. It's required.
            :param endpointPath: str. Endpoint path. Sample: https://contoso.com/api/v1/
            :param endpointMethods: str. Endpoint methods. Sample: customer/
            :param calledFrom: string. Name of app that call library.
            :param arguments: list. List of arguments used in verbs get or delete
        """
        self.__log = log        
        self.__path = endpointPath
        self.__args = arguments
        self.__cm = cm(log=log)
        self.__inheritedFrom = calledFrom
        if endpointMethods is None:
            self.__methods = ()
        else:
            self.__methods = endpointMethods
    
    def __call__(self, *args, **kwargs):
        try:
            if args or kwargs:
                arguments = dict()
                if kwargs:
                    arguments = self.__args.copy()
                    arguments.update(kwargs)
                return DirectCall(log = self.__log,endpointPath=self.__path, endpointMethods=self.__methods + args, arguments=arguments,calledFrom=self.__inheritedFrom)
        except Exception:
            pass
        return self
    
    def __str__(self):
        return str(dict(endpointPath=self.__path, endpointMethods=self.__methods, arguments=self.__args))

    def __getattr__(self,attribute):
        """
            Private method used for get attribute from class and create final endpoint.
        """
        result = None
        try:            
            result = DirectCall(log = self.__log,endpointPath=self.__path, endpointMethods=self.__methods + (attribute,),arguments=self.__args,calledFrom=self.__inheritedFrom)
        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='__getattr__',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom))
        return result

    def get(self, params=None, *args, **kwargs):
        """
            Public method for invoke secure get verb.  
            :param params: list. List of params. Using attributes, we haven't use this parameter. It's one option when we don't use attributes.
        """
        result = None
        try:                
            result = requests.get(url=self.__cm.buildUrl(endpointPath=self.__path,endpointMethods=self.__methods,arguments=self.__args),
                        params=params, *args, **kwargs)
            self.__log.debug(msg='Finished Execution.',extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='get',
                        className='DirectCall',inheritedFrom=self.__inheritedFrom,kwargs={'StatusCode':result.status_code}))
        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='get',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom))
        return result

    def post(self, body,*args, **kwargs):
        """
            Public method for invoke secure post verb. 
            :param body: json with body. It's required. Use json.dumps(body) when you invoke this method. It's needed import library json in your project.
        """
        result = None
        try:     
            if body:           
                result = requests.post(url=self.__cm.buildUrl(endpointPath=self.__path,endpointMethods=self.__methods,arguments=self.__args),
                            data=body, *args, **kwargs)
                self.__log.debug(msg='Finished Execution.',extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='post',
                        className='DirectCall',inheritedFrom=self.__inheritedFrom,kwargs={'StatusCode':result.status_code}))
            else:
                self.__log.error(msg="Body is required.",extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='post',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom)) 

        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='post',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom))
        return result
    
    def put(self, body,*args, **kwargs):
        """
            Public method for invoke secure put verb.  
            :param body: json with body. It's required. Use json.dumps(body) when you invoke this method. It's needed import library json in your project.
        """
        result = None
        try:     
            if body:           
                result = requests.put(url=self.__cm.buildUrl(endpointPath=self.__path,endpointMethods=self.__methods,arguments=self.__args),
                            data=body, *args, **kwargs)
                self.__log.debug(msg='Finished Execution.',extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='put',
                        className='DirectCall',inheritedFrom=self.__inheritedFrom,kwargs={'StatusCode':result.status_code}))
            else:
                self.__log.error(msg="Body is required.",extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='put',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom)) 

        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='put',
                    className='SecureCall',inheritedFrom=self.__inheritedFrom))
        return result
    
    def delete(self, params,*args, **kwargs):
        """
            Public method for invoke secure delete verb.  
            :param params: list. List of params. Using attributes, we haven't use this parameter. It's one option when we don't use attributes.
        """
        result = None
        try:   
            if params:             
                result = requests.delete(url=self.__cm.buildUrl(endpointPath=self.__path,endpointMethods=self.__methods,arguments=self.__args),
                            params=params, *args, **kwargs)
                self.__log.debug(msg='Finished Execution.',extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='delete',
                        className='DirectCall',inheritedFrom=self.__inheritedFrom,kwargs={'StatusCode':result.status_code}))
            else:
                self.__log.error(msg="Params is required.",extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='delete',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom)) 
        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='delete',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom))
        return result

    def patch(self, body,*args, **kwargs):
        """
            Public method for invoke secure patch verb. 
            :param token: str. Valid token for use call    
            :param body: json with body. It's required. Use json.dumps(body) when you invoke this method. It's needed import library json in your project.
        """
        result = None
        try:     
            if body:           
                result = requests.patch(url=self.__cm.buildUrl(endpointPath=self.__path,endpointMethods=self.__methods,arguments=self.__args),
                            data=body,*args, **kwargs)
                self.__log.debug(msg='Finished Execution.',extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='patch',
                        className='DirectCall',inheritedFrom=self.__inheritedFrom,kwargs={'StatusCode':result.status_code}))
            else:
                self.__log.error(msg="Body is required.",extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='patch',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom)) 

        except Exception as ex:
            self.__log.exception(msg="%s"%str(ex),extra=self.__cm.doExtraLogger(appName='RestApiHelper',methodName='patch',
                    className='DirectCall',inheritedFrom=self.__inheritedFrom))
        return result