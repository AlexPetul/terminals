function docker_hub_login () {
  echo "$DOCKER_HUB_PASSWORD"
  echo "$DOCKER_HUB_PASSWORD" | docker login --username alexpetul --password-stdin
}

function build () {
  echo "Building backend image"
  docker-compose -f build/staging/docker-compose.staging.yml build --pull --force-rm
  echo "Build backend image complete"
}

function push() {
  echo "Pushing backend image"
  docker-compose -f build/staging/docker-compose.staging.yml push
}

function test() {
    docker-compose -f build/staging/docker-compose.staging.yml pull
    docker-compose -f build/staging/docker-compose.staging.yml run --rm django python -m pytest
}

is_push=$1

if [ "$is_push" == "push" ]
then
  docker_hub_login
  build
  push
else
  docker_hub_login
  build
fi
