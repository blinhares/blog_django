build-docker:
	sudo docker compose up --build --force-recreate

run:
	sudo docker compose up

run-silently:
	sudo docker compose up -d

remote-sh:
	sudo docker compose up -d && docker exec -it djangoapp sh

get-permissions:
	sudo chown bruno:bruno -R  djangoapp/

exit:
	sudo docker compose down

