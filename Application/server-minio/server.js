import * as Minio from 'minio'
import express from 'express';

// Create an Express application
const app = express();
const port = 3000;

const s3Client = new Minio.Client({
    endPoint: 'poc-minio-api-route-poc-thesis-bram-terlouw.apps.cluster-nvtcj.sandbox1725.opentlc.com',
    useSSL: true,
    accessKey: 'minio',
    secretKey: 'minio123',
  })

app.get('/', (req, res) => {
res.send('Hello, World!');
});

app.get('/buckets', async (req, res) => {
    try {
        const buckets = await s3Client.listBuckets()
        res.json(buckets);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.get('/objects/:bucket', (req, res) => {
    const bucketName = req.params.bucket;
    const objectsList = [];

    const stream = s3Client.listObjectsV2(bucketName, '', true);
    stream.on('data', obj => objectsList.push(obj));
    stream.on('error', err => res.status(500).json({ error: err.message }));
    stream.on('end', () => res.json(objectsList));
});

app.get('/object/image/*', (req, res) => {
    const bucketName = 'images'
    const objectName = req.params[0];

    s3Client.getObject(bucketName, objectName, (err, dataStream) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }

        dataStream.pipe(res);
    });
});


app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
