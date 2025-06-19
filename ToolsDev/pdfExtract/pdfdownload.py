
import requests
import subprocess
import json
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import logging
from datetime import datetime


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('crawler.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Defined Output Directory 
PDF_DIR = Path('pdfs')
METADATA_DIR = Path('metadata')
PDF_DIR.mkdir(exist_ok=True)
METADATA_DIR.mkdir(exist_ok=True)

# Defiend MetaData 
IMPORTANT_FIELDS = [
    'Author', 'Creator', 'DocumentID', 'Title', 'CreateDate', 'ModifyDate',
    'Producer', 'CreatorTool', 'FilePermissions', 'FileModifyDate', 'PDFVersion'
]

def validate_url(url):
    """Domain Check """
    return url.startswith('https://www.esunbank.com') and url.endswith('.pdf')

def download_pdf(url, output_dir):
    """Donwload PDF"""
    try:
        # Extract FileName from URL 
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        output_path = output_dir / filename

        # Download File 
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Save files 
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        logger.info(f"Downloaded: {url} to {output_path}")
        return output_path
    except requests.RequestException as e:
        logger.error(f"Failed to download {url}: {e}")
        return None

def extract_metadata(pdf_path):
    """使用 exiftool 提取元數據並儲存為 JSON"""
    try:
        # Ensure file exists 
        if not pdf_path.exists():
            logger.error(f"PDF not found: {pdf_path}")
            return None

        # Using exiftools 
        output_json = METADATA_DIR / f"{pdf_path.stem}.json"
        cmd = ['exiftool', '-j', str(pdf_path)]

        # run 
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        metadata = json.loads(result.stdout)

        # Save meatadata file name 
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        logger.info(f"Extracted metadata for {pdf_path} to {output_json}")
        return metadata
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        logger.error(f"Failed to extract metadata for {pdf_path}: {e}")
        return None

def filter_important_metadata(metadata):
    """filter"""
    if not metadata:
        return None
    filtered = {key: metadata[0].get(key, '') for key in IMPORTANT_FIELDS}
    filtered['SourceFile'] = metadata[0].get('SourceFile', '')
    return filtered

def process_url(url):
    """Download and extract """
    if not validate_url(url):
        logger.warning(f"Invalid URL: {url}")
        return None

    # download 
    pdf_path = download_pdf(url, PDF_DIR)
    if not pdf_path:
        return None

    # extract 
    metadata = extract_metadata(pdf_path)
    if not metadata:
        return None

    return filter_important_metadata(metadata)

def main():
    # read pdfurl.txt
    try:
        with open('pdfurl.txt', 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logger.error("pdfurl.txt not found")
        return

    all_metadata = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(process_url, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                if result:
                    all_metadata.append(result)
            except Exception as e:
                logger.error(f"Error processing {url}: {e}")

    # Save All metadata 
    if all_metadata:
        output_file = METADATA_DIR / f"all_metadata_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_metadata, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved all metadata to {output_file}")
    else:
        logger.warning("No metadata extracted")

if __name__ == "__main__":
    main()
