# FastAPI + MongoDB

```bash
docker run -d --name mongo-academia \
	-e MONGO_INITDB_ROOT_USERNAME=academia \
	-e MONGO_INITDB_ROOT_PASSWORD=academia \
    -e MONGO_INITDB_DATABASE=academia \
    -p 27017:27017 \
	mongo:4.4.6
```
