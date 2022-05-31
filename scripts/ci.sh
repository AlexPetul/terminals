function docker_hub_login () {
  echo "$DOCKER_HUB_PASSWORD"
  echo "$DOCKER_HUB_PASSWORD" | docker login --username alexpetul --password-stdin
}

function build () {
  echo "Building backend image"
  docker build -t "$BACKEND_IMAGE" -f Dockerfile .
  echo "Build backend image complete"
}

function push() {
  echo "Pushing backend image"
  docker push "$BACKEND_IMAGE"
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
