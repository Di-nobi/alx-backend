import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient();

const message = () => {
    client.on('connect', () => {
        console.log('Redis client connected to the server');
    }).on('error', (error) => {
        console.log('Redis client not connected to the server:' + error);
    });
}
message();
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
};

const  async_get = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
    try {
        const output = await async_get(schoolName);
        console.log(output);
    }   catch (err) {
        console.log(err);
    }
    
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');