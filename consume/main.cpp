#include <stdlib.h>
#include <stdio.h>
#include <SimpleAmqpClient/SimpleAmqpClient.h>
#include <iostream>
#include <chrono>
#include <thread>


using namespace AmqpClient;
using namespace std;
 

int main()
{
    cout << "Subscriber started" << endl;

    //added delay for rabbit mq start to avoid failing with socket error
    std::this_thread::sleep_for(std::chrono::milliseconds(10000));

    char *szBroker = getenv("AMQP_BROKER");
    Channel::ptr_t channel;
    if (szBroker != NULL)
        channel = Channel::Create(szBroker);
    else
        channel = Channel::Create("172.28.0.2", 5672);//host rabbit shoould work here from compose file, but had to define ip
   
    std::string queue = "my_queue";

    //make sure exclusive set to false otherwise noone else can publish/consume the queue
    channel->DeclareQueue(queue, false, false, false, false);
    channel->BindQueue(queue, "amq.fanout","");
    channel->BasicConsume(queue, queue);


    //keep pooling, not sure if there is a better way
    while(1)
    {  
		string a;
		Envelope::ptr_t envelope;
		bool flag = channel->BasicConsumeMessage(queue, envelope, 7000);
		if (flag == false)
		{
			//cout << "timeout\n" << endl;
		    //break;
            continue;
		}

		a = envelope->Message()->Body();

		cout << a << endl;        
    }



    cout << "OK"<<endl;    
}