import requests
import os
import zipfile
import shutil

def actualizar_ffmpeg_opera():
    # Repository configuration
    owner = "nwjs-ffmpeg-prebuilt"
    repo = "nwjs-ffmpeg-prebuilt"
    api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    dest_path = "/usr/lib/x86_64-linux-gnu/opera-stable/libffmpeg.so"
    
    # 1. Get the latest Linux x64 release
    print("Buscando la última versión para Linux x64...")
    response = requests.get(api_url)
    if response.status_code != 200:
        print("Error al conectar con GitHub.")
        return

    assets = response.json().get('assets', [])
    download_url = None
    filename = ""

    # Look specifically for the linux-x64 asset
    for asset in assets:
        if "linux-x64" in asset['name']:
            download_url = asset['browser_download_url']
            filename = asset['name']
            break

    if not download_url:
        print("No se encontró un archivo compatible con Linux x64.")
        return

    # 2. Download the file
    print(f"Descargando {filename}...")
    with requests.get(download_url, stream=True) as r:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    # 3. Extract the archive and search for libffmpeg.so
    print("Extrayendo archivo...")
    extract_dir = "temp_ffmpeg"
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    # Search for the .so file inside the extracted folder
    source_file = None
    for root, dirs, files in os.walk(extract_dir):
        if "libffmpeg.so" in files:
            source_file = os.path.join(root, "libffmpeg.so")
            break

    # 4. Move it to the destination path (requires sudo)
    if source_file:
        try:
            print(f"Instalando en {dest_path}...")
            # copy2 overwrites the destination file and preserves metadata
            shutil.copy2(source_file, dest_path)
            print("¡Éxito! libffmpeg.so ha sido actualizado.")
        except PermissionError:
            print("ERROR: Permiso denegado. Ejecuta el script con 'sudo'.")
        except Exception as e:
            print(f"Error inesperado: {e}")
    else:
        print("No se encontró libffmpeg.so dentro del paquete descargado.")

    # 5. Cleanup
    print("Limpiando archivos temporales...")
    if os.path.exists(filename): os.remove(filename)
    if os.path.exists(extract_dir): shutil.rmtree(extract_dir)

if __name__ == "__main__":
    actualizar_ffmpeg_opera()
