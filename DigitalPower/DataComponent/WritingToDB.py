import logging
from xml.dom import ValidationErr
import dropbox


class WritingToDB:
    def __init__(self, name: str, target_path: str, key: str, file_format: str):
        ''' This class writes files in JSON format toward Dropbox

            Args:
                name: The name that the JSON file should have
                target_path: the directory in which it needs to be saved on Dropbox
                key: The access token that can be generated via the app
                file_format: indicates what type file it is to be written to Dropbox
        '''
        self.dbx = dropbox.Dropbox(key)

        try:
            file_json = open(f'{name}.{file_format}', 'rb')
            if self.check_target_path_exists(target_path):
                self.dbx.files_upload(
                    file_json.read(),
                    f'{target_path}/{name}.{file_format}',
                    mode=dropbox.files.WriteMode("overwrite")
                    )
                print('Saving to the Cloud success') #needs to be replaced by logging in the future
            else:
                print(f'Partition directory {name} does not exist. We make this directory')
                self.dbx.files_create_folder_v2(target_path)
                self.dbx.files_upload(
                    file_json.read(),
                    f'{target_path}/{name}.{file_format}',
                    mode=dropbox.files.WriteMode("overwrite")
                    )
                print('Saving to the Cloud success') #needs to be replaced by logging in the future

        except ValidationErr:
            print('Saving to the Cloud failed') #needs to be replaced by logging in the future

    def check_target_path_exists(self, target_path: str):
        ''' This method checks if the directory already exists
            It will return a boolean value if it exists and a false otherwise
        '''
        try:
            self.dbx.files_get_metadata(target_path)
            return True
        except BaseException:
            return False
