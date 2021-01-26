#!/bin/bash

case "$1" in
    bash|/bin/bash)
        /bin/bash
        ;;
    ash|/bin/ash)
        /bin/ash
        ;;
    migrate)
        python manage.py migrate
        ;;
    *)
        eval "$@"
esac