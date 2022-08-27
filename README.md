# TwitterTrending tech assignment

A cloud hosted api service as example: 

`http://143.177.112.110:8383/api/trends?source=twitter-sample&&topic=love`


![Alt text](architecture.png?raw=true "architecture")


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




### Future improvements

- better controling of running order of python scripts by adding a ```wait-and-run.sh```
- json error handling (instead of ignoring) for ```twitter-sample.json```
- implementing gunicorn for production-ready api service
- configuring resource allocations in Spark clusters and among docker containers
- maturing CI/CD workflows
- adding scripts and service logs
- HA Spark Cluster with zookeeper
- immigrating to K8s
- mongodb data persistence
- mongodb encriptions
- HA mongodb clusters

- from batch analyis to streaming analysis
- more data cleaning to support analysis beyond ```text``` field
- add more api parms like locations, special crowds and languages






