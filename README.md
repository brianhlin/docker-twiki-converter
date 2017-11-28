OSG TWiki Converter
===================

Requirements
------------

* A host with a running docker service
* `sudo` or membership in the `docker` group

Building the image
------------------

If you have access to `osghost`, skip this step. To build this image for another docker host:

```console
$ git clone https://github.com/brianhlin/docker-twiki-converter
$ docker build -t twiki:latest docker-twiki-converter
```

Start up the mkdocs server
--------------------------

Run the following command on a host with a running docker service (this requires `sudo` or membership in the `docker` group):

```console
$ docker run -d -v <PATH TO LOCAL GIT REPO>:/source -p 8000 twiki
```

Where `<PATH TO LOCAL GIT REPO>` is your local copy of:

* https://github.com/opensciencegrid/technology - for `SoftwareTeam` web docs
* https://github.com/opensciencegrid/docs/ - for `Release3` web docs

The above command should return the container ID, which can be used to find the port that the mkdocs server is listening to on the docker host:

```console
$ docker port <CONTAINER ID>
```

For example:

```console
$ docker port c87a9760e526
8000/tcp -> 0.0.0.0:32774
```

Meaning that the mkdocs server should be accessible on port 32774 of the docker host.

Convert documents
------------------

1. Create a link map file in the root of your local git repository with the following format:

        <TWIKI URL> <PATH TO MARKDOWN FILE>

    Where `<TWIKI URL>` is the link to the TWiki document that you want to convert, e.g. https://twiki.opensciencegrid.org/bin/view/SoftwareTeam/SoftwareDevelopmentProcess, and `<PATH TO MARKDOWN FILE>` is the path to the converted markdown file, relative to the `docs` directory.

1. Run the conversion script available in your docker container using the link map file created above:

        $ docker exec <CONTAINER ID> convert-twiki-list <LINK MAP FILE>


