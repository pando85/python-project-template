# __MY_APP__

This is a template for python projects.

Exists a branch for aiohttp projects. You can use it replacing `master` by `aiohttp` in next steps.

Set this repo as remote and merge to yours.
And then, replace `__MY_APP__` with your python package desired name.
```bash
git remote add template https://github.com/pando85/python-project-template.git
git pull --all
git merge template/master 
APP_NAME=desired_name
mv __MY_APP__ $APP_NAME
find ./ -type f -not -path "./.git/*" -exec sed -i "s/__MY_APP__/$APP_NAME/g" {} \;
```

## Lint

Lint: `make lint`

## Dev

Run app: `make run`

## Tests

Run tests: `make test`

### Production

**Warning**: aiohttp is [slower with gnunicorn](https://docs.aiohttp.org/en/stable/deployment.html#start-gunicorn). Basic `python -m my_app` execution is prefered.
