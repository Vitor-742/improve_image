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

## Exemplos de Prompts

- "Transforme esta imagem em um estilo de pintura a óleo"
- "Adicione um céu noturno com estrelas"
- "Faça a imagem parecer mais vintage"
- "Adicione um efeito de neblina"
- "Transforme em um desenho animado"
- "Adicione um filtro de verão"

## Tecnologias Utilizadas

- Flask - Framework web
- Google Gemini API - Modelo de IA para processamento de imagens
- Python-dotenv - Gerenciamento de variáveis de ambiente
- Pillow - Processamento de imagens
- HTML/CSS/JavaScript - Interface do usuário

## Estrutura do Projeto

```
.
├── server.py          # Servidor Flask e lógica principal
├── index.html         # Interface do usuário
├── requirements.txt   # Dependências do projeto
├── .env              # Configurações e chaves de API
└── README.md         # Este arquivo
```

## Limitações

- O tamanho máximo da imagem é limitado pela API do Gemini
- A qualidade da edição depende da clareza do prompt
- Requer conexão com a internet para funcionar
- Necessário ter uma chave de API válida do Google Gemini

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## Suporte

Se você encontrar algum problema ou tiver alguma dúvida, por favor abra uma issue no repositório.
