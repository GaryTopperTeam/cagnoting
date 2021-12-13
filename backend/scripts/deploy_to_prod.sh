#!/bin/bash
set -e

git fetch
git checkout dev
if [ -z "$(git diff dev origin/dev)" ]; then
    echo "Merging dev onto master"
    git checkout master
    git pull
    NOW=`date`
    git merge dev --no-ff -m "[DEPLOY] $NOW"
    git push
    git checkout dev
    echo "--> DEPLOYMENT DONE."
else
  echo "La branche dev n'est pas à jour avec le serveur."
  echo "MERCI de corriger ça d'abord."
  echo " "
  echo "--> FAILED TO DEPLOY"
fi

