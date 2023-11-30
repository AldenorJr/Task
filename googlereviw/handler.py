from source.main import Main


def execute(event, context):
    url = event.get('url')
    main = Main()
    main.execute(url)
    return {"statusCode": 200, "body": "All sucess!"}
