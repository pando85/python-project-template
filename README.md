# __MY_APP__

This is a template for python projects.

Exists different branchs for aiohttp projects. You can use it replacing `master` by `{branch_name}` in next steps.

Branchs availables:
- aiohttp
- aiohttp-postgres
- aiohttp-rabbitmq

Set this repo as remote and merge to yours.
And then, replace `__MY_APP__` with your python package desired name.
```bash
git remote add template https://github.com/pando85/python-project-template.git
git pull --all
git merge template/master
APP_NAME={desired_name}
mv __MY_APP__ $APP_NAME
find ./ -type f -not -path "./.git/*" -exec sed -i "s/__MY_APP__/$APP_NAME/g" {} \;
```

For travis magic you need [travis-cli](https://github.com/travis-ci/travis.rb).

If you want to grant travis access to update your requirements you will need to replace `__GITHUB_TOKEN__` with next command:

```bash
# Get token from Github with public repo access
GITHUB_TOKEN={token}
SECURE_SECRET=$(travis encrypt GITHUB_TOKEN=$GITHUB_TOKEN)
sed -i "s/__GITHUB_TOKEN__/$SECURE_SECRET/g" .travis.yml
```

To get dockerhub build working when merge something into master you will need to replace `__DOCKERHUB_TOKEN__` with next command:


```bash
# Get token from dockerhub repo-> Build Settings -> Build triggers -> Trigger token
DOCKERHUB_TOKEN_TRIGGER={token}
SECURE_SECRET=$(travis encrypt DOCKERHUB_TOKEN=$DOCKERHUB_TOKEN_TRIGGER)
sed -i "s/__DOCKERHUB_TOKEN__/$SECURE_SECRET/g" .travis.yml
```

## Lint

Lint: `make lint`

## Dev

Run app: `make run`

## Tests

Run tests: `make test`
