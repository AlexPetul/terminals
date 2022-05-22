function docker_hub_login () {
  docker login -u alexpetul -p "$DOCKER_HUB_PASSWORD"
}

is_push=$1

if [ "$is_push" == "push" ]
then
  docker_hub_login
else
  docker_hub_login
fi
