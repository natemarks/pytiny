## pytiny

```bash

cd ~/projects
cookiecutter  https://github.com/natemarks/pytiny
full_name [Nate Marks]: 
email [npmarks@example.com]: 
github_username [natemarks]: 
project_name [Python Boilerplate]: iii jjj
project_slug [iii_jjj]: 
project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: 


cd iii_jjj
git init .
git add -A
git commit -v -a -m "initial commit"
git branch -m master main

make clean-venv
make static
```


.vscode/launch.json
```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "purpose": [
        "debug-test"
      ],
      "console": "integratedTerminal",
      "justMyCode": true,"env": {
        "AWS_PROFILE": "imprivata-sandbox"
      }
    },
  ]
}```