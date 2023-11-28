from main import Main

def lambda_handler(event, context):
    main = Main()
    main.execute(event['url'])