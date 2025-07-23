"""
Management command to upload stellar images to Google Cloud Storage
Run this in production to sync local media files to GCS
"""
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from google.cloud import storage

class Command(BaseCommand):
    help = 'Upload stellar images to Google Cloud Storage'

    def handle(self, *args, **options):
        if not settings.DEBUG:  # Only run in production
            client = storage.Client()
            bucket = client.bucket(settings.GS_BUCKET_NAME)
            
            # Local media/static directory
            local_static_dir = os.path.join(settings.BASE_DIR, 'media', 'static')
            
            if os.path.exists(local_static_dir):
                for filename in os.listdir(local_static_dir):
                    local_file = os.path.join(local_static_dir, filename)
                    if os.path.isfile(local_file):
                        blob_name = f'static/{filename}'
                        blob = bucket.blob(blob_name)
                        
                        with open(local_file, 'rb') as f:
                            blob.upload_from_file(f)
                        
                        self.stdout.write(
                            self.style.SUCCESS(f'Uploaded {filename} to {blob_name}')
                        )
            else:
                self.stdout.write(
                    self.style.ERROR(f'Directory {local_static_dir} does not exist')
                )
        else:
            self.stdout.write(
                self.style.WARNING('This command only runs in production')
            )
