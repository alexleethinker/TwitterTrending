# TwitterTrending tech assignment

- Before cloning the project, make sure you have latest Docker Engine and Docker-Compose installed on your machine. The code should be working on Windows, Linux and MacOS environments.
- Then you can clone it and run.
    ```
    git clone https://github.com/alexleethinker/TwitterTrending.git

    cd TwitterTrending

    docker-compose up -d
    ```
- Docker images needed are either being built locally or pulled from cloud.
   
- The following services (only with simple.json data) are now ready:
    - a (pseudo) spark stand-alone cluster
        - open `http://localhost:8080/` to check spark status
    - a single node MongoDB
    - API `GET http://127.0.0.1/:8383/api/trends?source=value&&topic=value`
            - ```source``` in ['sample','twitter-sample']
            - ```topic``` can be any single word
   
- Further, let's load the big dataset (twitter-sample.json) and calculate trends.
    ```
    # data loading 
    docker-compose run --rm --no-deps etl-runner python etl.py --fileName=twitter-sample.json

    # using pyspark to calculate hot topic trends
    docker-compose run --rm --no-deps pyspark-runner python spark_trending.py --fileName=twitter-sample
    ```







- take a set of Twitter data and two user input topic as input and produces a comparison of trend history for last week.
- slope of the frequency of occurrence 



