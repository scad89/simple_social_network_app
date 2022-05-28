# simple_social_network_app

In this project, a simple REST API of a social network is implemented.

The following stack was used for implementation:

```
- sqlparse
- coreapi
- coreschema
- Django
- djangorestframework
- djangorestframework-simplejwt
- drf-yasg
- gunicorn
- pip-compile-multi
- psycopg2
- psycopg2-binary
- python-dateutil
- python-dotenv
```

## Usage

1. Add a file with environment variables (.env_docker) to the root of the project.
2. Run command:

```
   - sudo docker-compose up -d
```

If you need to rebuild containers (make some changes), use command:

```
   - sudo docker-compose up --build
```

If you run a project on Windows, and docker from under a virtual machine (like VirtualBox), the project
address 0.0.0.0:8000 may not open. Then you need to use the address 192.168.99.100:8000.

To stop containers, use the command:

```
   - docker-compose down
```

- http://0.0.0.0:8000/api/v1/registration/ - new user registration
- http://0.0.0.0:8000/api/v1/login/ - registered user login
- http://0.0.0.0:8000/api/v1/logout - registered user logout
- http://0.0.0.0:8000/api/v1/new_post/ - add new post
- http://0.0.0.0:8000/api/v1/new_like/ - add like or dislike
- http://0.0.0.0:8000/api/v1/posts/ - output all posts with his likes/dislikes/number of likes and dislikes/number of only likes/number of only dislikes
- http://0.0.0.0:8000/docs/ - documentation

## Contacts

- Instagram: [@igor*komkov*](https://www.instagram.com/igor_komkov_/)
- Vk.com: [Igor Komkov](https://vk.com/zzzscadzzz)
- Linkedin: [Igor Komkov](https://www.linkedin.com/in/igor-komkov/)
- email: **scad200@gmail.com**
- Telegram: **@zzzSCADzzz**
