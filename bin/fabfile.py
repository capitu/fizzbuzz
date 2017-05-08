#! /usr/bin/env python
# coding=utf-8

from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm
from fabric.api import run, env
import xml.etree.ElementTree as ET
import sys, traceback
from time import gmtime, strftime
import time
from utils import *


COMMIT_MESSAGE = "Auto-commit for build # "
working_dir = "/Users/alsu/IdeaProjects/fizz/"
rio_modules = []


@task
def deploy(version=''):
    if confirm(yellow("Create new maven build and zip archive?")):
        pushToMaster(version)
        mvnbuild()
        local("git checkout develop")
        build_version = getPomVersion()


@task
def changeDeployVersion(version=''):
    """updates pom version in all project pom files"""
    print(yellow("change_application_version start"))
    print(yellow("changing version of main pom"))
    update_pom_version(working_dir, version)
    for rio_module in rio_modules:
        print(yellow("changing version of module " +rio_module ))
        rio_module_dir = working_dir + rio_module + "/"
        update_pom_version(rio_module_dir, version)
    print(green("change_application_version end"))


@task
def pushToMaster(version):
    print(yellow("prepare_branch start"))
    local("git stash")
    local("git checkout develop")
    local("git pull --rebase -p")
    print(green("prepare_branch end"))

    print(yellow("commit_build start"))
    changeDeployVersion(version)
    currentVersion = getPomVersion()
    print("current version: " + currentVersion)
    addPomFilesToGit()

    local("git commit -m\"" + COMMIT_MESSAGE + currentVersion + "\"")
    local("git tag -a jar" + currentVersion + " -m '" + COMMIT_MESSAGE + currentVersion + "'")
    local("git push origin develop --follow-tags")

    print(green("commit_build end"))

    print(yellow("bring_changes_master start"))
    local("git checkout master")
    local("git merge develop --no-ff --no-edit")
    local("git push origin master --follow-tags")
    print(green("push to master end"))

def addPomFilesToGit():
    with lcd(working_dir):
        local("git add " + POM)
        for rio_module in rio_modules:
            local("git add " + rio_module + "/" + POM)

def mvnbuild():
    print(yellow("MVN CLEAN"))
    time.sleep(2)
    cmd = "cd " + working_dir + " && mvn clean"
    local(cmd)

    if confirm(yellow('skip test?')):
        cmd = "cd "+ working_dir + " && mvn package -DskipTests"
        print(yellow("MVN PACKAGE (skip test)"))
    else:
        cmd = "cd "+ working_dir + " && mvn package"
        print(yellow("MVN PACKAGE"))

    time.sleep(2)

    local(cmd)


@task
def prepare_build(version=''):

    current_version = str(get_war_version(VERSION_FILE_NAME))
    next_version = str(version if version != '' else int(current_version) + 1)
    print(green("Start build script"))
    print(green("current build: ") + current_version)
    print(yellow("next build: ") + next_version)
    if confirm(yellow('Do you wish to continue?')):

        print(green("Let's start"))

        print(yellow("prepare_branch start"))
        local("git stash")
        local("git checkout develop")
        local("git pull --rebase -p")
        print(green("prepare_branch end"))

        print(yellow("change_application_version start"))
        file_put_contents(next_version, VERSION_FILE_NAME)
        regex_sed = "s/app.version=[0-9].*/app.version=" + next_version + "/g"
        # sed  s/app.version=[0-9].*/\app.version=158/g ../../application.properties
        sed_command = "sed -i " + regex_sed + " " + APPLICATION_PROPERTIES
        local(sed_command)
        print(green("change_application_version end"))

        print(yellow("commit_build start"))
        local("git add " + VERSION_FILE_NAME)
        local("git add " + APPLICATION_PROPERTIES)
        local("git commit -m\"" + COMMIT_MESSAGE + next_version + "\"")
        local("git tag -a war" + next_version + " -m '" + COMMIT_MESSAGE + next_version + "'")
        local("git push origin develop --follow-tags")

        print(green("commit_build end"))

        print(yellow("bring_changes_master start"))
        local("git checkout master")
        local("git merge develop --no-ff")
        local("git push origin master --follow-tags")
        local("git checkout develop")
        print(green("bring_changes_master end"))

        print(green("Finished!!"))

    else:
        print(red("Aborted by user"))