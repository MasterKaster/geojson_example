import girder_client
import girder_worker_utils
from script import largest_counties

API_KEY='vhR2Wwya707mkkZzoFRxstBgCV0Z3xfvzk5DNJyg'  # Set to your own API key
ITEM_ID='59a5b0fe4f2ae5377cd5a1d4'  # Set to your own item ID

client = girder_client.GirderClient(apiUrl='https://resonant-demo.kitware.com/api/v1')
client.authenticate(apiKey=API_KEY)
girder_worker_utils.set_item_task(client=client, item_id=ITEM_ID, fn=largest_counties)
