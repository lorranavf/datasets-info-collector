# Datasets Info Collector
Dataset Info Collector is a Python library that provides a DatasetDownloader class for downloading datasets based on a list of accessions. It simplifies the process of retrieving dataset information and managing the download process from [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/).

### Usage
Here's an example of how to use the DatasetDownloader class:

```python
from datasets_info_collector import DatasetDownloader
accessions_list = ['accession1', 'accession2', 'accession3']
downloader = DatasetDownloader(accessions_list)
downloader.download_datasets()
```

The DatasetDownloader class takes a list of dataset accessions as a parameter during initialization. The download_datasets() method is then called to initiate the download process. 
The method handles the downloading of datasets for the given accessions and prints any accessions that were not successfully downloaded after 3 attempts.

## Requirements
To use de  script you need to have Python 3.x, along with following programs installed:

- datasets (from NCBI)
- unzip
- tqdm
- requests

Note that this script was developed for research purposes and may require modifications to adapt to different scenarios.
