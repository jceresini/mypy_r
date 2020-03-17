## mypy_r

Search the current path recursively for python packages, and run mypy on each package

This was built to be used in CI pipelines, without having to know where the python packages are in the project. Example gitlab-ci template job:

```
.mypy
  stage: test
  image: python
  script:
    - pip install mypy_r
    - mypy-r --ignore-missing-imports --follow-imports=skip --no-strict-optional
```

