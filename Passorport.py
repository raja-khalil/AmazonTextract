import boto3
import csv
import json

# Configurar o cliente do Textract
client = boto3.client('textract', region_name='us-east-1', 
                      aws_access_key_id='SEU_ACESS_KEY', 
                      aws_secret_access_key='SEU_SECRET_KEY')

# Função para processar um documento de passaporte
def process_passport(image_bytes):
    response = client.detect_document_text(Document={'Bytes': image_bytes})
    return response

# Função para extrair informações relevantes
def extract_info(response):
    extracted_data = {}
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            text = block['Text']
            if 'Passport No:' in text:
                extracted_data['Passport_Number'] = text.split(':')[1].strip()
            elif 'Name:' in text:
                extracted_data['Name'] = text.split(':')[1].strip()
            elif 'Date of Birth:' in text:
                extracted_data['Date_of_Birth'] = text.split(':')[1].strip()
            elif 'Nationality:' in text:
                extracted_data['Nationality'] = text.split(':')[1].strip()
            elif 'Expiration Date:' in text:
                extracted_data['Expiration_Date'] = text.split(':')[1].strip()
    return extracted_data

# Função para salvar os dados em um arquivo CSV
def save_to_csv(data, filename='passports_db.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data['Passport_Number'], data['Name'], data['Date_of_Birth'], 
                         data['Nationality'], data['Expiration_Date']])

# Main
if __name__ == "__main__":
    # Carregar imagem do passaporte
    with open('path/to/your/passport_image.jpg', 'rb') as image_file:
        image_bytes = image_file.read()

    # Processar a imagem do passaporte
    textract_response = process_passport(image_bytes)

    # Extrair informações
    passport_info = extract_info(textract_response)

    # Salvar informações no banco de dados (CSV)
    save_to_csv(passport_info)

    print("Informações do passaporte extraídas e salvas com sucesso!")
