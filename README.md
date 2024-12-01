# A Guide to The Galaxy

A self-paced space tour app.

## Start development

```shell
# clone this repo
git clone https://github.com/Mase3206/group-awesome

# prepare environment
python -m venv venv

# install requirements
python -m pip -r requirements.txt
npm install

# run the dev server
python manage.py runserver
```

### Extra commands

If you are editing the custom theme of the Allauth screens, you will need to run `npm run-script build-allauth` after each edit (or `build-allauth:watch` to watch for changes).
```shell
npm run-script build-allauth
```

If you just want to quickly build and compile everything, run `npm run-script build`. This will build the Allauth themes and run `manage.py collectstatic --noinput`. 
```shell
npm run-script build
```

## Deployment Notes

- Make sure you have the latest version of the secrets.yml file. This is intentionally not committed to the repository, so you'll need to get it from a contributor.
- Before deploying, run `npm run-script build` to ensure the server gets the latest versions of the stylesheets.
