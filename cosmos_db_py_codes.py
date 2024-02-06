from azure.cosmos import CosmosClient,PartitionKey

ENDPOINT = "<endpoint-url>"
KEY = "<key>"
DATABASE_NAME = "Toyota"
CONTAINER_NAME = "products"

## Create cosmosDB client
client = CosmosClient(url=ENDPOINT, credential=KEY)

## Create Database and partition key
database = client.create_database_if_not_exists(id=DATABASE_NAME)
key_path = PartitionKey(path="/categoryId")

## Create container
container = database.create_container_if_not_exists(id=CONTAINER_NAME, 
                                                    partition_key=key_path, 
                                                    offer_throughput=400
                                                    )
print("Container\t", container.id)

## Insert items to the container
new_item1 = {"id": "80b63682-b93a-4c77-aad2-65501347265f",
             "categoryId": "61dba35b-4f02-45c5-b173-c6badc0cbd79",
             "categoryName": "SUV",
             "name": "Brezza",
             "Drive": "2WD",
             }

new_item2 = {"id": "80b63683-b93b-4c77-agd2-65501384965f",
             "categoryId": "61dsc35b-4e50-45c5-b728-c6banm8cbd79",
             "categoryName": "Hatchback",
             "name": "Baleno",
             "Drive": "2WD",
             }

container.create_item(new_item1)
container.create_item(new_item2)

## Fetch items from containers
item = container.read_item(item = "80b63683-b93b-4c77-agd2-65501384965f",
                           partition_key = "61dsc35b-4e50-45c5-b728-c6banm8cbd79")

print("output",item["name"])

## Reference - https://www.linkedin.com/pulse/interacting-cosmos-db-through-python-arun-ramaswamy



