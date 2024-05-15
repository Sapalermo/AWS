import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Users')

def createUser(event, context):
    try:
        body = json.loads(event['body'])
        username = body['username']
        # Esegue la logica per la creazione dell'utente
        # Aggiunge l'utente a DynamoDB
        table.put_item(Item={'username': username})
        return {
            'statusCode': 200,
            'body': json.dumps({'messaggio': f'User {username} creato'})
        }
    except:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Errore durante la creazione dell\'utente'})
        }         

def getUserById(event, context):
    try:
        user_id = event['pathParameters']['id']
        # Esegue la logica per ottenere l'utente da DynamoDB
        response = table.get_item(Key={'username': user_id})
        if 'Item' not in response:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'User not found'})
            }
        user = response['Item']
        return {
            'statusCode': 200,
            'body': json.dumps(user)
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Errore durante l\'ottenimento dell\'utente: ' + str(e)})
        }