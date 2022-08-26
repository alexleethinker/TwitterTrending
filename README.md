# TwitterTrending tech assignment

Before cloning the project, make sure you have latest Docker Engine and Docker-Compose installed on your machine. The code should be working on Windows, Linux and MacOS environments.

- Then you can clone it and run. Docker images needed are either being built locally or pulled from cloud.
    ```
    git clone https://github.com/alexleethinker/TwitterTrending.git

    cd TwitterTrending

    docker-compose up -d
    ```



- The following services (only with simple.json data) are now ready:
    - a single node MongoDB

    - a (pseudo) spark stand-alone cluster
        - open `http://localhost:8080/` to check spark status

    - API `GET http://127.0.0.1/:8383/api/trends?source=value&&topic=value`
        - ```source``` should be either ```sample``` or ```twitter-sample```
        - ```topic``` can be any single word
   



- Further, let's load the big dataset ```twitter-sample.json``` and calculate trends.
    ```
    # data loading 
    docker-compose run --rm --no-deps etl-runner python etl.py --fileName=twitter-sample.json

    # using pyspark to calculate hot topic trends
    docker-compose run --rm --no-deps pyspark-runner python spark_trending.py --fileName=twitter-sample
    ```


