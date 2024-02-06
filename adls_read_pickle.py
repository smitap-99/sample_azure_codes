from azure.storage.filedatalake import DataLakeServiceClient
import pickle

# Replace these with your own values
account_name = "readwriteadlsgen2"
account_key = "<key>"
file_system_name = "pricing"
directory_name = "/"
file_name = "model_inputs_dict.pkl"

# Create a DataLakeServiceClient
service_client = DataLakeServiceClient(account_url=f"https://{account_name}.dfs.core.windows.net", credential=account_key)

# Get a reference to the file system
file_system_client = service_client.get_file_system_client(file_system=file_system_name)

# Get a reference to the directory
directory_client = file_system_client.get_directory_client(directory=directory_name)

# Get a reference to the file
file_client = directory_client.get_file_client(file_name)

# Download the file content
downloaded_content = file_client.download_file()

# Deserialize the pickle content
unpickled_data = pickle.loads(downloaded_content.readall())

# Now you can use 'unpickled_data' as your Python object

# Example: Print the contents
print(unpickled_data)