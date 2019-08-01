## Response To The Technical Questions

* How long I spent on the coding test
    I spent about 7 non consecutive working days for both frontend and backend. If I   had more time, I would have added authentication to enable each users have their categories and favorite things

* Useful feature included in Django Restframework 3.9
    One of the useful feature included in DRT 3.9 is the automatic schema generation for openapi documenetation. The code snippet bellow is an example of an openapi configuration which can be seen in the urls.py file of this project. An example schema is found in the `openapi-schema.yml` file in the root directory of this project.
    ```
    ./manage.py generateschema > openapi-schema.yml
    ```
    ```bash
      path('openapi', get_schema_view(
      title="favorte things",
      description="API for all things …"
    ), name='openapi-schema'),
    ```
    
* Performance issue on production
    One good approach to track down performance issue on production is to turn on health monitoring in the cloud (Cloud watch in the case of AWS). From here, where a lot of time is spent can be seen. It could be from third party api, Excessive Web Service Invocation, slow sql statement, querying two many data etc.

    Same issue can also be reproduced on the staging or local environment by using load testing frameworks like Locust

    One case I have done this was a slow performance in the production environment due to many users querying the database(serching and filtering at time). We had to implement database indexing(search engine) using Django Haystack solr.
