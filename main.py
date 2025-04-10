from PIL import Image
import pytesseract

# Caminho da imagem
imagem_path = "exemplo_ocr.jpg"
saida_txt_path = "texto_extraido.txt"

# (Se necessário) Defina o caminho do executável do Tesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abrir imagem
imagem = Image.open(imagem_path)

# Extração de texto
texto_extraido = pytesseract.image_to_string(imagem, lang='por')

# Salvar no TXT
with open(saida_txt_path, "w", encoding="utf-8") as f:
    f.write(texto_extraido)

print("Texto salvo em:", saida_txt_path)
