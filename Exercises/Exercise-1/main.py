import requests
import os
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def create_dir(dir_name, path = ''):
    current_path = path or os.getcwd()
    dir = os.path.join(current_path, dir_name)
    
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    return dir

def download_file(uri, file_path):
    request = requests.get(uri)
    if request.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(request.content)

def unzip_file(file_path, dir_path):
     if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            csv_filename = [name for name in zip_ref.namelist() if name.endswith('.csv')][0]
            zip_ref.extract(csv_filename, dir_path)
    

def main():
    # your code here
    if not len(download_uris):
        return
    
    # Create download file directory
    dir_path = create_dir('downloads')
    file_path = f'{dir_path}/' 
    
    # Download the files and save the files
    for uri in download_uris:
        file_name = uri.split("/")[-1]
        path = file_path + file_name
        download_file(uri, path)
    
    # Unzip the files and remove the files
    for uri in download_uris:
        file_name = uri.split("/")[-1]
        path = file_path + file_name
        unzip_file(path, dir_path)
                
        os.remove(path)

if __name__ == "__main__":
    main()
