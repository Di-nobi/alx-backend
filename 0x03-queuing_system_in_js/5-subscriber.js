import { createClient } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) {
    console.log('Redisclient not connected to the server: ' + error);
});

client.subscribe('holberton school channel');
client.on('data', (channel, message) => {
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
    }
    console.log(message);
});