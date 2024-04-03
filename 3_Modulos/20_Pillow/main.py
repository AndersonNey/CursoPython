import os
from pickletools import optimize
from PIL import Image

def main(main_imagens_folder, new_width=800):
    if not os.path.isdir(main_imagens_folder):
        raise NotADirectoryError (f'{main_imagens_folder} não existe.')

    for root , dirs , files in os.walk(main_imagens_folder):
        for file in files:
            file_full_path = os.path.join(root,file)
            file_name , extension = os.path.splitext(file)

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root , new_file)

            #SE EU QUISER APAGAR AS FOTOS CONVERTIDAS (FAZ ISSO CHECANDO O '_CONVERTED')
            # if converted_tag in file_full_path:
            #     os.remove(file_full_path)
            # continue



            if converted_tag in file_full_path:  #se a imagem ja foi convertida nao converter de novo
                continue

            
            img_pillow = Image.open(file_full_path)


            width , height = img_pillow.size
            new_height = round((new_width * height) / width)
            #print(width , new_width , height , new_height)
            """
            width         height
            new_width     ??
            """
            new_image = img_pillow.resize((new_width,new_height),Image.LANCZOS)
            
            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70
            )

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()

if __name__ == '__main__':
    caminho = os.path.dirname(os.path.realpath(__file__))
    
    main_imagens_folder = caminho + r'\imagens'
    main(main_imagens_folder,new_width=1920)
















