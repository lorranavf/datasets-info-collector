import os
import time
import requests
import subprocess
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

    def __init__(self, accessions, outdir='in.datasets'):

        if not isinstance(accessions, list):
            raise ValueError("Accessions must be a list.")
        
        self.accessions = accessions
        self.outdir = outdir

    def is_internet(self):
        url = 'https://www.google.com'
        try:
            requests.get(url, timeout=5)
            return True
        except requests.exceptions.ConnectionError:
            return False

    def check_internet(self):

        while not self.is_internet():
            time.sleep(5)

    def is_accession_missing(self, acession):


        return not os.path.exists(f'{self.outdir}/{acession}')

    def download_datasets(self):
                
        print('Starting download.')

        os.makedirs(self.outdir, exist_ok=True)

        for i in trange(len(self.accessions), ncols=100):

            self.check_internet()

            while self.is_accession_missing(self.accessions[i]):

                filezip = f'{self.outdir}/{self.accessions[i]}.zip'

                cmd = [
                    'datasets', 'download', 'genome', 'accession', self.accessions[i],
                    '--include', 'gff3,rna,cds,protein,genome,seq-report',
                    '--filename', filezip
                ]

                try:
                    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                    if os.path.exists(filezip):
                        subprocess.run(['unzip', '-qq', filezip, '-d', f'{self.outdir}/{self.accessions[i]}'], check=True)
                        os.remove(filezip)

                except subprocess.CalledProcessError as e:
                    print(f'Error downloading accession {self.accessions[i]}: {e}')

                if not self.is_accession_missing(self.accessions[i]):
                    break
