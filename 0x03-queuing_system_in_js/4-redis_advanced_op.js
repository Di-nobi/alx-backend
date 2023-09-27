import { createClient, print } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log('Redis client not connected to the server: ' + error);
});

const data = {'Portland': 50, 'Seattle': 80, 'New York': 20, 'Bogota': 20, 'Cali': 40, 'Paris': 2};

for (let [key, value] of Object.entries(data)) {
    client.hset('HolbertonSchools', key, value, print);
}

client.hgetall('HolbertonSchools', function (error, result) {
    if (error) {
        console.log(error);
    }
    console.log(result);
});