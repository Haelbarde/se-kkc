from azure.cosmos import exceptions, CosmosClient, PartitionKey
import orders
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize the Cosmos client
# Requires: https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator
# Requires: azure-cosmos
#   python -m pip install azure-cosmos

endpoint = 'https://localhost:8081'
key = 'C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=='

# <create_cosmos_client>
client = CosmosClient(endpoint, key)
# </create_cosmos_client>

# Create a database
# <create_database_if_not_exists>
database_name = 'GameDatabase'

databases = list(client.query_databases({
        "query": "SELECT * FROM r WHERE r.id=@id",
        "parameters": [
            { "name":"@id", "value": database_name }
        ]
    }))

if (len(databases) > 0):
    client.delete_database(database_name)

database = client.create_database_if_not_exists(id=database_name)
# </create_database_if_not_exists>



orders_name = "Orders"
orders_db = database.create_container_if_not_exists(
    id=orders_name, 
    partition_key=PartitionKey(path="/username"),
    offer_throughput=400
)

order_items_to_create = [orders.vulture_1_1(), orders.vulture_1_2(), orders.scorpion_1_1(), orders.scorpion_1_2(), orders.swan_1_1(), orders.swan_1_2()]

for item in order_items_to_create:
    orders_db.create_item(body=item)


def get_cycle(turn):

    query = "SELECT * FROM c WHERE c.turn = {}".format(turn)
    print(query)
    items = list(orders_db.query_items(
        query=query,
        enable_cross_partition_query=True
        )
    )
    return items
