# Seedcase Registry

## Installing and using

You will need to have [these software](https://seedcase-project.org/community/guide-entries/required-software/) installed in order to continue. After that, make sure Docker is running and then open a Terminal (while in the root of this project) and run this command:

``` {.bash}
just start-docker
```

This will build the docker for Seedcase. To stop Docker:

``` {.bash}
just stop-docker
```

There are several other project-specific commands contained in the `justfile` that you can view by running:

``` {.bash}
just
```

## Contributing

See the [contributing guidelines](CONTRIBUTING.md) for how to work with and
contribute to this project.
