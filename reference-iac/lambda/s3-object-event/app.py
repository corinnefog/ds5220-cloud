import os

from chalice import Chalice

app = Chalice(app_name='s3-object-event')
app.debug = True

# Set the value of BUCKET_NAME in the .chalice/config.json file.
S3_BUCKET = os.environ.get('BUCKET_NAME', '')

@app.on_s3_event(bucket=S3_BUCKET, events=['s3:ObjectCreated:*'])
def s3_handler(event):
    app.log.debug("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)
