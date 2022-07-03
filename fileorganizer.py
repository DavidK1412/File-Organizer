import os

downloads_folder = 'C:/Users/david/Downloads/'
base_folder = 'C:/Users/david/OneDrive/Documentos/'

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(downloads_folder + filename)

        if extension in ['.jpg', '.jpeg', '.png', '.gif']:
            os.rename(downloads_folder + filename, 'C:/Users/david/OneDrive/Imágenes/' + filename)
        
        if extension in ['.exe']:
            os.rename(downloads_folder + filename, base_folder + 'Ejecutables/' + filename)
        
        if extension in ['.cpp', '.py', '.js', '.css', '.java']:
            os.rename(downloads_folder + filename, base_folder + 'TestsProgramacion/' + filename)