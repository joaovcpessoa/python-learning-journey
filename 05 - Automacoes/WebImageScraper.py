from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urlparse

def is_valid_url(url):
    """
    Verifica se a URL fornecida é válida.
    """
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)

def folder_create(images):
    """
    Cria uma pasta para armazenar as imagens.
    """
    try:
        folder_name = input("Enter Folder Name: ")
        os.mkdir(folder_name)
    except FileExistsError:
        print("Folder already exists!")
        folder_create(images)
    download_images(images, folder_name)

def download_images(images, folder_name):
    """
    Faz o download das imagens e as salva na pasta criada.
    """
    count = 0
    print(f"Total {len(images)} Images Found!")
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image.get("data-srcset") or image.get("data-src") or image.get("data-fallback-src") or image.get("src")
                if image_link is None:
                    continue

                response = requests.get(image_link)
                response.raise_for_status()  # Verifica se houve algum erro na solicitação HTTP

                with open(f"{folder_name}/image{i+1}.jpg", "wb") as f:
                    f.write(response.content)
                    count += 1
            except requests.RequestException as e:
                print(f"Error downloading image {i+1}: {str(e)}")
                continue

        if count == len(images):
            print("All Images Downloaded!")
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")

def main(url):
    """
    Função principal do programa.
    """
    if not is_valid_url(url):
        print("Invalid URL!")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na solicitação HTTP
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        folder_create(images)
    except requests.RequestException as e:
        print(f"Error accessing URL: {str(e)}")
        return

url = input("Enter URL: ")
main(url)