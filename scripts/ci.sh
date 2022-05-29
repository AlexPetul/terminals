function docker_hub_login () {
  echo "$DOCKER_HUB_PASSWORD"
  echo "$DOCKER_HUB_PASSWORD" | docker login --username alexpetul --password-stdin
}

is_push=$1

if [ "$is_push" == "push" ]
then
  docker_hub_login
else
  docker_hub_login
fi
