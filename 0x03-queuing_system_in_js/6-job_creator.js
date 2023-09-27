import { createQueue } from "kue";

const qeue = createQueue();

const data = {
    phoneNumber: '070600410366',
    message: 'latest',
};

const create_job = qeue.create('push_notification_code', data).save((error) => {
    if (error) {
        throw Error('Notification job failed');
    }
    console.log('Notification job created: ' + create_job.id);

});

create_job.on('complete', () => {
    console.log('Notification job completed');
});
