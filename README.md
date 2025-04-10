Este projeto realiza a extração de texto de uma imagem utilizando OCR (Reconhecimento Óptico de Caracteres) com a biblioteca `pytesseract`, salvando o conteúdo extraído em um arquivo `.txt`.

---


Ler uma imagem com texto digitado e converter esse conteúdo para um arquivo `.txt`, possibilitando a visualização e reutilização do texto em formato editável.

---

- Python 3
- [Pillow](https://pillow.readthedocs.io/) - para abrir a imagem
- [pytesseract](https://pypi.org/project/pytesseract/) - interface para o Tesseract OCR
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - motor de reconhecimento de texto

---


```bash
pip install pillow pytesseract
