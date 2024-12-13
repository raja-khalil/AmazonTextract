# Amazon Textract Passport Data Extractor

Este projeto utiliza o Amazon Textract para identificar informações presentes em passaportes e gerar um banco de dados. O script em Python processa imagens de passaportes, extrai dados relevantes como número do passaporte, nome, data de nascimento, nacionalidade e data de expiração, e armazena essas informações em um arquivo CSV.

## Pré-requisitos

- Python 3.x
- AWS CLI configurado com as credenciais de usuário
- Biblioteca `boto3`
- Imagem do passaporte em formato JPG

## Configuração

1. **Instalar as dependências necessárias:**
   ```bash
   pip install boto3

