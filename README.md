# local development virtual env
    # clone/update/checkout your "working" branch from main
    
    # activate python environment
    
    # run dev server
    
    # push your "working" branch and create pull request

# local developerment docker/docker-compose
    I. install docker and docker-compose
    		# sudo docker-compose up -d
    		#sudo docker-compose ps ( to see if it is fine)
    
    II. add-django-multitenant
    	For example, if you want to use this domain: 'local-cgito.net', do two things:
		1) add or replace this line in your .env: ALLOWED_HOSTS=local-cgito.net
		2) add this entry '127.0.0.1 local-cgito.net' to your host's /etc/hosts file
	
	Then login into the web container and run this comand to recreate the tenane: python src/manage.py create_tenant

# staging/production
    ## tbd