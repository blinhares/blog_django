build-docker:
	sudo docker compose up --build --force-recreate

run:
	sudo docker compose up

run-silently:
	sudo docker compose up -d
