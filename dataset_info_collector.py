import os
import time
import requests
import shutil
from tqdm import trange


class DatasetDownloader:
    """
    A class for downloading datasets based on a list of accessions.

    Args:
        accessions (list): A list of dataset accessions.

    Methods:
        check_internet(): Checks if there is an internet connection.
        download_datasets(): Downloads the datasets for the given accessions.
        
    """
    def __init__(self, accessions):
        self.accessions = accessions

    def check_internet(self):
        url = 'https://www.google.com'
        timeout = 5
        try:
            requests.get(url, timeout=timeout)
            return True
        except requests.exceptions.ConnectionError:
            return False

    def download_datasets(self):
        
        if os.path.exists('in.datasets'):
            shutil.rmtree('in.datasets')
        os.mkdir('in.datasets')
        
        error = []
            
            
        for i in trange(len(self.accessions), ncols = 100):
            internet = 'offline'
            while internet == 'offline':
                if not self.check_internet():
                    internet = 'offline'
                    time.sleep(10)
                else:
                    internet = 'online'
                if internet == 'online':
                    break
                    

            filezip = f'in.datasets/{self.accessions[i]}.zip'

            cmd = f'datasets download genome accession {self.accessions[i]} --include gff3,rna,cds,protein,genome,seq-report --filename {filezip} > /dev/null 2>&1'

            os.system(cmd)

            
            if os.path.exists(filezip):
                os.system(f'unzip -qq {filezip} -d in.datasets/{self.accessions[i]}')
                os.remove(filezip)
            else:
                error.append(self.accessions[i])

        if error:
            print('The datasets for the following accessions were not downloaded:')
            for accession in error:
                print(accession)



