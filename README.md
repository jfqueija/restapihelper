# RestApiHelper

The target of this library is provide a simple methods for consume url apis using attributes.

##  __How to Use__

### __Common Class__

We can integrated in our projects, using this import:

```py
from restapihelper.common import Common as cm
```

This library provides us a token refresh method using client credentials based in grantt type. 

__Example Use:__

```py
common = cm(log=lg,calledFrom='AppDummy')
token = common.refreshToken(refreshEndpoint='https://contoso.com/api/token',clientKey='<ClientKey>',
        clientSecret='<ClientSecret>')
```

>   The constructor wait for two parameters.
>   *   Log is required for trace errors in library. It's inherited object logging
>   *   calledFrom it's not required. For construct logger, in extra data, we can report this value for write output for identified the app or tool that use this library

If we have problems when we get token, the result is None. Before to call api, we can validate if the Token is a string or a None value.

### __SecureCall Class__

This method provide a helper for construct api rest calls.

:arrow_up: for use method of secureCall class, it's neccesary provide a bearer token.

For integrated in our projects, we will use this import:

```py
from restapihelper.secureCall import SecureCall as sc
```

####    __Example Use:__


#####   __Get Verb__

```py
apiCall = sc(log=lg,endpointPath='https://contoso.com/apiName/api/1.1',calledFrom='AppDummy')
```

>   Followed same construct reference to common library, we have next parameters:
>   *   Log is required for trace errors in library. It's inherited object logging
>   *   endpointPath is a endpoint url.
>   *   calledFrom it's not required. For construct logger, in extra data, we can report this value for write output for identified the app or tool that use this library

This declaration return an object.

For use the helper, we can followed next example:

```py
response = apiCall.Costumer.get(token=token)
```

>   In the endpoint path, we haven't any enpoint method. In the before example, we declare that the endpoint method is Costumer. If we put the url in browser it's same that this: __https://contoso.com/apiName/api/1.1/Costumer__. The library provide this construction.

Next attribute is the method that we need. In this case, we use get method. It waits for parameter Token.

Inside the library, we establish the communication using authorization based un Bearer.


>   If we need to send paramters to verb, we can use this example:

```py
response = apiCall.Costumer(Name='nameDummy',Surname='surnameDummy').get(token=token)
```

Inside the library, the construct of the final url it's: __https://contoso.com/apiName/api/1.1/Costumer?Name=nameDummy&Surname=surnameDummy__

#####   __Post, Put & Patch Verb__

>   When we need to use a post, put or patch verb, we can follow next examples:

```py
body = {'name':'Jhon','surname':'Doe','address':'Street 2'}
response = apiCall.Costumer.post(token=token,body=json.dumps(body))
```

```py
body = {'name':'Jhon','surname':'Doe','address':'Street 2'}
response = apiCall.Costumer(1).put(token=token,body=json.dumps(body))
```

> Previous example update customer with identifier 1, modifing data request from body dictionary. We use put when change all data of element.
> Url Endpoint construct: __https://contoso.com/apiName/api/1.1/Costumer/1__

```py
body = {'address':'Street 3'}
response = apiCall.Costumer(1).patch(token=token,body=json.dumps(body))
```

> Previous example update customer with identifier 1, modifing partial data request from body dictionary. We use patch when only change partial data of element.
> Url Endpoint construct: __https://contoso.com/apiName/api/1.1/Costumer/1__

#####   __Delete Verb__

Followed next exampl, we can delete a register:

```py
response = apiCall.Costumer(id=3).delete(token=token)
```

> Url output: __https://contoso.com/apiName/api/1.1/Costumer?id=3__

or

```py
response = apiCall.Costumer(3).delete(token=token)
```

> Url output: __https://contoso.com/apiName/api/1.1/Costumer/3__


#####   Notes

>   This Library support next Rest API Verbs:
>   *   Get
>   *   Post
>   *   Put
>   *   Delete
>   *   Patch

### __DirectCall Class__

It's same of __SecureCall Class__ but with one diference. __DirectCall Class__ don't use token. Calls to API it's directly.

This class it's not recommendable use with api's not secured in production enviroment. 

>   Remember, all api's in production enviroment, always they must be securized under one Api Gateway or with local OAuth. You never expose a production api's without secure credentials.

>   Use this class when you need to test API in sandbox or develompment enviroment.