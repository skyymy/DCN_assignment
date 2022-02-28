1. Open 4 terminal instances.
2. Instance-I: Create a common docker network
```bash
docker network create dns_app_network
```
3. Instance-II Goto to `AS` folder from terminal, run these commands
```bash
docker build -t dns_app/as:latest
docker container prune
docker run --network dns_app_network --name AS -p 53533:53533/udp -it dns_app/as:latest 
```
4. Instance-III Goto `FS` folder from terminal, run these commands
```bash
docker build -t dns_app/fs:latest
docker container prune
docker run --network dns_app_network --name FS -p 9090:9090  -it dns_app/fs:latest
```
5. Intance-IV Goto `US` folder from terminal, run these commands
```bash
docker build -t dns_app/fs:latest
docker container prune
docker run --network dns_app_network --name US -p 8080:8080 -it dns_app/us:latest
```
6. Go Back to Instance-I and run `docker inspect dns_app_network` to get IP addresses of the 3 servers

7. In Instance-I start testing

a. US responds to requests on /fibonacci url, run the following command as one single command
```bash
curl --location --request GET 'http://0.0.0.0:8080/fibonacci?hostname=fibonacci.com&fs_port=9090&number=5&as_ip=172.19.0.4&as_port=53533'
```

b. FS accepts a registration request on /register url, run the following command as one single command
```bash
curl --location --request PUT 'http://0.0.0.0:9090/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "hostname": "fibonacci.com",
    "ip": "172.19.0.2",
    "as_ip": "172.19.0.4",
    "as_port": 53533
}'
```
 
c. FS responds to requests on /fibonacci url, run the following command as one single command
```bash
curl --location --request GET 'http://0.0.0.0:9090/fibonacci?number=5'
```

d. AS performs a registration request 
Note: when /register happens in b. AS is registering that , so you can see its logs in Instance-II where AS is running.

e. AS provides a DNS record  
Note: when /fibonacci happens in a. or c. AS is registering that , so you can see its logs in Instance-II where AS is running.
