import { createClient } from 'redis';
const client = createClient();
const message = () => {
    client.on('connect', () => {
        console.log('Redis client connected to the server');
    }).on('error', (error) => {
        console.log('Redis client not connected to the server:' + error);
    });
}
message();