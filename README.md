# __MY_APP__

First of all replace `__MY_APP__` with your python package desired name.
```bash
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
