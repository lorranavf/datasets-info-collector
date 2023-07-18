# Datasets Info Collector
Dataset Info Collector is a Python library that provides a DatasetDownloader class for downloading datasets based on a list of accessions. It simplifies the process of retrieving dataset information and managing the download process from NCBI.

### Usage
Here's an example of how to use the DatasetDownloader class:

´´´python
Copy code
from dataset_info_collector import DatasetDownloader
´´´
accessions_list = ['accession1', 'accession2', 'accession3']
downloader = DatasetDownloader(accessions_list)
downloader.download_datasets()
The DatasetDownloader class takes a list of dataset accessions as a parameter during initialization. The download_datasets() method is then called to initiate the download process. The method handles the downloading of datasets for the given accessions and prints any accessions that were not successfully downloaded.
