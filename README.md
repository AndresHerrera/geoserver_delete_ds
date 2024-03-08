# FIX AT Geoserver

Este script permite borrar los datastores bloqueados en el servidor de mapas de AT

## Pasos a realizar

### Crear ambiente en Anaconda

```sh
$ conda create --name at_geoserver python=3.8
$ conda activate at_geoserver
```

### Instalar geoserver rest 

```sh
$ conda install -c iamtekson geoserver-rest
$ conda install -c conda-forge python-dotenv
$ conda install -c conda-forge requests
```

#### .env

```ini
GEOSERVER_HOST=http://127.0.0.1:8080/geoserver
GEOSERVER_USER=admin
GEOSERVER_PASSWORD=geoserver
```

#### Ejecutar Script

```sh
$ python fix_geoserver.py
```

