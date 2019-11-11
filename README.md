In order to start a new python project, create a virtual environment and do the following. The creation of the virtual environment can be deferred until the make command

```bash
$ PROJ=<actual_project_name>
$ git clone git@github.com:spapanik/python-lib-template.git $PROJ
$ cd $PROJ
$ rm -rf .git
$ find . -type f ! -name "README.md" -print0 | xargs -0 sed -i "s/{{project_name}}/$PROJ/g"
$ mv src/project_name/ src/$PROJ/
$ make install
```
