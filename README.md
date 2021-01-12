# Flask Base
[![Python](https://img.shields.io/badge/python-3.8--slim-blue.svg)]() [![](https://img.shields.io/badge/flask--restplus-0.13.0-red.svg)]() 

My template base to build Flask RESTful APIs using [Flask RESTPlus](https://flask-restplus.readthedocs.io/en/stable/index.html), [JWT Extended](https://flask-jwt-extended.readthedocs.io/en/latest/) and [PyMongo](https://flask-pymongo.readthedocs.io/en/latest/).

You can just clone this repo and start to create/customize your own RESTful API using this code as your template base :)

# Localhost

### Installing

```
pip3 install -r requirements.txt
```

### Usage

```
export MONGO_URI="mongodb://<your_mongo_host>:27017/<your_database>"
export JWT_SECRET_KEY="<randomic_key>"
python3 entrypoint.py
```

# Docker

### Installing

```
docker build -t flask-app --target develop .
```

### Usage

```
docker run -d \
-p 5000:5000 \
-e MONGO_URI="mongodb://<your_mongo_host>:<your_mongo_port>/<your_mongo_database>" \
-e JWT_SECRET_KEY="<your_randomic_key>" \
flask-app
```

# Swagger

After the application goes up, open your browser on `localhost:5000/api/v1/docs` to see the self-documented interactive API.

# Project Structure

The project structure is based on the official [Scaling your project](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-apis-with-reusable-namespaces) doc with some adaptations (e.g `v1` folder to agroup versioned resources).


```
.
├── app
│   ├── helpers
│   │   ├── __init__.py
│   │   ├── parsers.py
│   │   └── password.py
│   ├── __init__.py
│   └── v1
│       ├── __init__.py
│       └── blueprints
│           ├── auth
│           │   ├── __init__.py
│           │   ├── routes.py
│           │   └── serializers.py
│           ├── __init__.py
│           └── users
│               ├── __init__.py
│               ├── services.py
│               ├── serializers.py
│               └── routes.py
├── config.py
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
├── entrypoint.py
└── entrypoint.sh

```

### Folders

* `app` - All the RESTful API implementation is here.
* `app/helpers` - Useful function/class helpers for all modules.
* `app/v1` - Resource agroupment for all `v1` [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces).
* `app/v1/blueprints` - All `v1` resources are implemented here.


### Files

* `app/__init__.py` - The Flask Application factory (`create_app()`) and it's configuration are done here. Your [Blueprints](https://flask-restplus.readthedocs.io/en/stable/scaling.html#use-with-blueprints) are registered here.
* `app/v1/__init__.py` - The Flask RESTPlus API is created here with the versioned Blueprint (e.g `v1`). Your [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces) are registered here.
* `config.py` - Config file for envs, global config vars and so on.
* `Dockerfile` - Dockerfile used to build a Docker image (using [Docker Multistage Build](https://docs.docker.com/develop/develop-images/multistage-build/))
* `LICENSE` - MIT License, i.e. you are free to do whatever is needed with the given code with no limits.
* `.dockerignore` - Lists files and directories which should be ignored while Docker build process.
* `.gitignore` - Lists files and directories which should not be added to git repository.
* `requirements.txt` - All project dependencies.
* `entrypoint.py` - The application entrypoint.
* `entrypoint.sh` - Starting script before application

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
