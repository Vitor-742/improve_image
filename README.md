## Requisitos

- Python 3.8 ou superior
- Chave de API do Google Gemini
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Gemini:
```
GEMINI_API_KEY=sua_chave_api_aqui
```

## Como Usar

1. Inicie o servidor:
```bash
python server.py
```

2. Abra seu navegador e acesse:
```
http://localhost:5000
```

3. Para editar uma imagem:
   - Arraste e solte uma imagem ou clique para selecionar
   - Digite um prompt descrevendo como quer editar a imagem
   - Clique em "Enviar"
   - Aguarde o processamento da IA
   - A imagem editada será exibida na área de preview


Original:

![input](https://github.com/user-attachments/assets/cd484faf-31eb-4b99-829f-23d0154b6567)

Google Gemini 2.0 Flash:

![imagem melhorada](https://github.com/user-attachments/assets/ae70a600-c219-4471-9a51-0d87ab83756b)

 - Geração de corpo da personagem

![imagem personagem](https://github.com/user-attachments/assets/5093c882-2e07-4c58-8516-2b430198355e)

Real-ESRGAN:

![output](https://github.com/user-attachments/assets/2a05b118-4036-4316-85bb-a7522a2fdc44)



