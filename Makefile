build:
	docker build -t andrequeiroz2/app-card:latest .

push:
	docker push andrequeiroz2/app-card:latest

pull:
	docker pull andrequeiroz2/app-card:latest

run:
	docker run -p 5000:5000 andrequeiroz2/app-card:latest
