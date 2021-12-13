#!/bin/bash
set -e

cd /usr/src/app/
if [ ! -d "common" ]; then
  echo " You should clone 'be-common' folder in src/commun folder before start working."
  echo "git clone git@git.aiotools.ovh:aio/be-common.git common"
  echo "Abort"
  exit 1
fi

case "$1" in
    prod)
        echo "---> Starting in PRODUCTION mode"
        cd /usr/src/app/
        exec /usr/local/bin/gunicorn --worker-class eventlet  --timeout 3600  server_app:app -w 10 -b :9009
        # exec /usr/local/bin/gunicorn server_app:app -w 5 -b :9009
        ;;
    dev)
        echo "---> Starting in DEV mode"
        cd /usr/src/app/
        export FLASK_DEBUG=1
        echo "---> Start EXEC"
        FLASK_APP=server_app.py flask run --port 9009  --with-threads --host '0.0.0.0'
        echo "---> END"
        ;;
    *)
        echo "Please specify argument (prod|dev) [ARGS..]";
        exit 1;
        ;;
esac

exit 0;
