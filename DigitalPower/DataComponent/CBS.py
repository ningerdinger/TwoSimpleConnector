import json
import cbsodata
import WritingToDB as wDB


class CBS:
    ''' This connector retrieves all the generic description including the identifier.
        After that it will retrieve the data corresponding to the identifier.
        Finallly, it will write everything, as raw data, to a dropbox storage

        Args:
            key: the token you can generate from dropbox app
    '''
    def __init__(self, key: str):
        self.key = key
        print("retrieving all the indentifiers")
        #self.tables = cbsodata.get_table_list()
        #self.list_of_identifier = [value['Identifier'] for value in self.tables]
        self.list_of_identifier = ['84669NED', '83583NED', '83582NED']
        self.writing_to_json(self.list_of_identifier)

    def save_dict_to_json(self, data_dict: dict, identifier: str):
        ''' Converts a dictionary to JSON file and also saves it on your local drive

            Args:
                data_dict: the dictionary that needs to be converted to JSON file
                identifier: the identifier under which the data is stored
        '''
        with open(f'{identifier}.json', 'w', encoding="utf8") as file:
            json.dump(data_dict, file, indent=1)

    def writing_to_json(self, list_identifier: list):
        ''' This method first retrievers the data based on the identifier.
            It will then convert the dictionary into a JSON format on your local drive
            It will then proceed to upload from your local drive toward Dropbox.
            NOTE: reason why it doesn't save directly to Dropbox Cloud is because
            Dropbox doesn't support this functionality

            Args:
                list_identifier: a list of all the id under which data are stored in
        '''
        for identifier in list_identifier:
            print(f'retrieving data for table {identifier}')
            data = cbsodata.get_data(identifier)
            print(f'converting data to {identifier}.json')
            self.save_dict_to_json(data, identifier)
            target_path = f'/DigitalPowerCBSData/Bronze/{identifier}'
            print('writing data to storage')
            wDB.WritingToDB(
                name=identifier,
                target_path=target_path,
                key=self.key,
                file_format='json'
                )


token = "sl.BNH69B2MA5XIZSMl-qPMKSA-8Y6SDUROKMZ8M2fsX6hwimRh3V5d61roUnXNcypEg5mzk9ngMNBqY74qdGHkbfGGURbO4QSI-x_1u4R3tuzqiaS3NHzg3EwwJ3rlHylbzBwWXUpecSOq"
CBS(token)
