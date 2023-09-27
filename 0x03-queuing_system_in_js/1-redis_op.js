import { createClient, print } from "redis";

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

function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, result) => {
        if (error) {
            console.log(err);
        }
        console.log(result);
    });
    
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');