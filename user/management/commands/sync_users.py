from django.core.management.base import BaseCommand
from user.models import User, Car, Fine, Driver  # Import your User model from your Django app
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Command(BaseCommand):
    help = 'Sync user data from Google Sheets to User model'

    def handle(self, *args, **kwargs):
        # Define the function to populate users from Google Sheets
        def populate_users_from_google_sheets():
            scope = ['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive']
            
            creds = ServiceAccountCredentials.from_json_keyfile_name('user/gspread-410110-716bd833f25d.json', scope) 
            
            client = gspread.authorize(creds)
            sheet = client.open('Gspread').sheet1 
            
            records = sheet.get_all_records()
            
            for record in records:
                user = User(
                    id=record['id'],
                    email=record['email'],
                    first_name=record['first_name'],
                    last_name=record['last_name'],
                    profile_picture=record['profile_picture_url']  # Adjust according to your model
                    # Add more fields as per your Google Sheet columns and User model
                )
                user.save()
        
        # Call the function to sync data
        populate_users_from_google_sheets()
        self.stdout.write(self.style.SUCCESS('Data synchronization completed successfully.'))
