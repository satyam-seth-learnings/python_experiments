- Offical Doc Link: [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)

- [YouTube Tutorial](https://www.youtube.com/watch?v=zDYL22QNiWk)

- Initialize project 

```sh
pipenv install
```

- Install packages

```sh
pipenv install <package-name>
```

- Install development packages

```sh
pipenv install <package-name> --dev
```

- Uninstall packages

```sh
pipenv uninstall <package-name>
```

- Run your script

```sh
pipenv run python <script-name>.py
```

- Activate the virtual environment

```sh
pipenv shell
```

- Deactivate the virtual environment

```sh
exit
```

- Remove vertual environment

```sh
pipenv --rm
```

- Check for security vulnerabilities

```sh
pipenv check
```

- Update packages

```sh
pipenv update
```

- Update python version

```sh
pipenv --python <python-version>
```

- Generate requirements.txt

```sh
pipenv lock -r > requirements.txt
```

- Viertual environment location

```sh
pipenv --venv
```

- Generate development requirements.txt

```sh
pipenv lock -r -d > dev-requirements.txt
```

- Show dependency graph

```sh
pipenv graph
```

- Generate Pipfile.lock file

```sh
pipenv lock
```

- Install packages from Pipfile.lock

```sh
pipenv install --ignore-pipfile
```
