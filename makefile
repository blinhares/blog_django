build-docker:
	sudo docker compose up --build --force-recreate

run:
	sudo docker compose up

run-silently:
	sudo docker compose up -d

remote-sh:
	sudo docker compose up -d && docker exec -it djangoapp sh

exit:
	sudo docker compose down

