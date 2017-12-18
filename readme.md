# Rabbitmq Client C++ example with docker

This is a simple example how to consume rabbitmq messages using C++ SimpleAmqpClient library and docker

Install docker and docker compose. Run the following commands to test the queue:

    #start all contaienrs
    docker-compose -f docker-compose.yml up --force-recreate --build -d

    #get ip address of publisher or use localhost
    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' cpprabbitexample_publisher_1

    #trigger publisher to send the message from the browser
    http://<ip>:8000/ or http://localhost:8000

    #check consumer console, the message should show up
    sudo docker logs cpprabbitexample_consumer_1

    #cleanup
    docker-compose -f docker-compose.yml down --rmi local | true

References
----------------
SimpleAmqpClient: https://github.com/alanxz/SimpleAmqpClient

rabbitmq-c: https://github.com/alanxz/rabbitmq-c