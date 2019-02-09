# Politico

[![Build Status](https://travis-ci.org/simbaa1/Politico.svg?branch=develop)](https://travis-ci.org/simbaa1/Politico) [![Coverage Status](https://coveralls.io/repos/github/simbaa1/Politico/badge.svg)](https://coveralls.io/github/simbaa1/Politico) [![Maintainability](https://api.codeclimate.com/v1/badges/415c9cac895b5cacc783/maintainability)](https://codeclimate.com/github/simbaa1/Politico/maintainability) 

Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency.

## Requirements
- [VS code](https://code.visualstudio.com/)
- [Python 3.x](https://www.python.org/)
- [Postman](https://www.getpostman.com/downloads/)

<details><summary>Installation</summary>
<p>

#### installation steps

- clone the git repo
```
$ git clone https://github.com/simbaa1/politico.git
```
- cd into the project directory
```
$ cd politico
```
- create the virtual environment and activate it
```
$ python3 -m venv env
$ source env/bin/activate
```

- install dependencies
```
$ pip install -r requirements.txt
```
- Run the app
``` $ flask run ```

</p>
</details>


<p></p>
<p></p>


  | **Endpoint** | **Functionality** | **Route** |
| --- | --- | --- |
| **POST** /parties | Creates a political party | `/api/v1/parties/` |
| **GET** /parties/`<int:party-id>` | Gets a specific political party | `/api/v1/parties/<int:party_id>` |
| **GET** /parties | Gets all political parties | `/api/v1/parties/` |
| **PATCH** /parties/`<party-id>`/name | Edit the name of a specific political party. | `/api/v1/parties/<int:party-id>/<string:name>` |
| **DELETE** /parties/`<party-id>` | Delete a political party | `/api/v1/parties/<int:party-id>` |
| **POST** /offices | Create a political office. | `/api/v1/offices/` |
| **GEt** /offices | Fetch all political offices records | `api/v1/offices/` |
| **GET** /offices | Fetch a specific political office record | `api/v1/offices/<int:office_id>` |

# Author
Christopher Simba

