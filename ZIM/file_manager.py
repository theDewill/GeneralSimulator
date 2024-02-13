import os
from datetime import datetime
import uuid
import json


class FileHandler:
    def __init__(self, SAVE_FOLDER):
        self.SAVE_FOLDER = SAVE_FOLDER
        self.INPUT_FOLDER = os.path.join(SAVE_FOLDER, "input")
        self.OUTPUT_FOLDER = os.path.join(SAVE_FOLDER, "output")
        self.INPUT_FOLDER_CONFIG = os.path.join(self.INPUT_FOLDER, "config")
        self.OUTPUT_FOLDER_DATA = os.path.join(self.OUTPUT_FOLDER, "data")

        self.check_folder_tree()

    def check_folder_tree(self):
        '''
        Check if the folder tree exists. If not, create it.
        '''

        for dir in [self.INPUT_FOLDER, self.OUTPUT_FOLDER, self.INPUT_FOLDER_CONFIG, self.OUTPUT_FOLDER_DATA]:
            if not os.path.exists(dir):
                print(f'{dir} does not exist. Creating...')
                os.makedirs(dir)
            else:
                print(f'{dir} exists.')

    def create_input_structure(self, inputStructPath, inputStruct):

        '''
        Create the input structure file
        '''

        filename = os.path.join(inputStructPath, "input_struct.json")

        with open(filename, "w") as file:
            json.dump(inputStruct, file)

        return filename

    def create_output_data_folder(self):
        '''
        Create a folder for the output data files
        '''

        folder_name = self.create_odf_name()
        folder_path = os.path.join(self.OUTPUT_FOLDER_DATA, folder_name)
        os.makedirs(folder_path)

        return folder_name, folder_path

    def create_odf_name(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_id = str(uuid.uuid4())

        return f'odf_{timestamp}_{unique_id}'
        

class InputHandler:
    def __init__(self):

        '''
            Handles input data from API
        '''

        self.input_structure = None
        self.input_data_path = None

    def setInput(self, input_struct_path):

        '''
        Set the input structure and input data path
        '''

        self.input_data_path = input_struct_path
        try:

            with open(self.input_data_path, "r") as file:
                input_struct = json.load(file)

        except FileNotFoundError:
            print(f"File {input_struct_path} not found.")
            return False

        self.input_structure = input_struct

        return self.input_structure

    def getInput(self, input_group: str, input_name: str):

        '''
        Get the input value from the input structure
        args(
            input_group: str,
            input_name: str
        )
        '''

        Data = self.input_structure[input_group][input_name]
        if Data["value"] == "":
            return Data["default"]
        else:
            return Data["value"]

        
    def checkInput(self):

        '''
        Check if the input structure and input data path are set
        '''

        if self.input_structure is None:
            if self.input_data_path is None:
                print("No input data path set.")
            return False
        
    
