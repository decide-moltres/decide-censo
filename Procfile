% prepara el repositorio para su despliegue. 
release: sh -c 'cd decide && python manage.py migrate'
release: sh -c 'cd decide && python manage.py compilemessages'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'
